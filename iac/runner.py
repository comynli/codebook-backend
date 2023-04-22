import os
import shutil
import uuid
import threading
import functools
from datetime import datetime

import ansible_runner
from asgiref.sync import async_to_sync, AsyncToSync
from channels.layers import get_channel_layer
from git import Repo
from django.conf import settings
from django.utils import timezone
from .models import Task, TaskState, RunnerEvent
from .consumers import EventConsumer


class AnsibleRunner:
    _semaphore = threading.Semaphore(settings.IAC_EXECUTE_CONCURRENCY)

    def __init__(self, task: Task):
        self.task = task
        self.repository = task.repository
        self.uid = uuid.uuid4().hex
        self.workspace = settings.IAC_WORKSPACE.joinpath(self.uid)
        self._event_handlers = {
            'runner_on_start': self._create_event,
            'runner_on_ok': functools.partial(self._set_event_state, TaskState.COMPLETED),
            'runner_on_failed': functools.partial(self._set_event_state, TaskState.FAILED)
        }
        # self._send_event = AsyncToSync(self._send_event, force_new_loop=True)

    def prepare_env(self, parent, filename, content):
        if not content:
            return
        path = self.workspace.joinpath(parent)
        path.mkdir(exist_ok=True)
        with open(path.joinpath(filename), 'w') as w:
            w.write(content)

    def prepare(self):
        os.makedirs(self.workspace)
        repo = Repo.clone_from(self.repository.git_url, self.workspace)
        self.task.commit_id = repo.head.commit.hexsha
        self.prepare_env('inventory', 'hosts', self.task.inventories)
        self.prepare_env('env', 'envvars', self.task.envvars)
        self.prepare_env('env', 'extravars', self.task.extravars)

    def cleanup(self):
        shutil.rmtree(self.workspace)

    def _create_event(self, event_data: dict):
        RunnerEvent.objects.create(
            task=self.task,
            host=event_data['host'],
            playbook=event_data['playbook'],
            playbook_uuid=event_data['playbook_uuid'],
            play=event_data['play'],
            play_uuid=event_data['play_uuid'],
            task_name=event_data['task'],
            task_uuid=event_data['task_uuid'],
        )

    def _set_event_state(self, state: TaskState, event_data: dict):
        obj = RunnerEvent.objects.get(
            task=self.task,
            host=event_data['host'],
            playbook_uuid=event_data['playbook_uuid'],
            play_uuid=event_data['play_uuid'],
            task_uuid=event_data['task_uuid']
        )
        obj.state = state
        obj.remote_addr = event_data.get('remote_addr')
        obj.start = timezone.make_aware(datetime.fromisoformat(event_data['start']))
        obj.end = timezone.make_aware(datetime.fromisoformat(event_data['end']))
        obj.duration = event_data['duration']
        obj.res = event_data.get('res')
        obj.changed = event_data.get('res', {}).get('changed', False)
        obj.save()
        self._send_event()

    @async_to_sync
    async def _send_event(self, close=False):
        channel_layer = get_channel_layer()
        payload = {
            "type": "on_event",
            "task_id": self.task.id,
            "close": close
        }
        await channel_layer.group_send(EventConsumer.group_name(self.task.id), payload)

    def _event_handler(self, event):
        event_type = event['event']
        event_data = event['event_data']
        handler = self._event_handlers.get(event_type)
        if handler:
            handler(event_data)
        # match event_type:
        #     case 'runner_on_start':
        #         self._create_event(event_data)
        #     case 'runner_on_ok':
        #         self._set_event_state(TaskState.COMPLETED, event_data)
        #     case 'runner_on_failed':
        #         self._set_event_state(TaskState.FAILED, event_data)
        # if event_type == 'runner_on_start':
        #     self._create_event(event_data)
        # elif event_type == 'runner_on_ok':
        #     self._set_event_state(TaskState.COMPLETED, event_data)
        # elif event_type == 'runner_on_failed':
        #     self._set_event_state(TaskState.FAILED, event_data)

    def execute(self):
        self.prepare()
        self.task.state = TaskState.RUNNING
        self.task.save()
        r = ansible_runner.run(
            private_data_dir=self.workspace,
            playbook=self.task.playbook,
            event_handler=self._event_handler
        )
        if r.status == 'successful':
            self.task.state = TaskState.COMPLETED
        if r.status == 'failed':
            self.task.state = TaskState.FAILED
        self.task.output = r.stdout.read()
        self.task.save()
        self.cleanup()
        self._send_event(True)
