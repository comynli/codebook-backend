from asgiref.sync import async_to_sync
from channels.db import database_sync_to_async
from channels.generic.websocket import JsonWebsocketConsumer, AsyncJsonWebsocketConsumer
from .models import Task, RunnerEvent
from .serializers import TaskSerializer, RunnerEventSerializer


class EventConsumer(JsonWebsocketConsumer):
    group_name_prefix = "iac_task"

    @classmethod
    def group_name(cls, task_id: int):
        return f'{cls.group_name_prefix}_{task_id}'

    @property
    def task_id(self):
        return self.scope['url_route']['kwargs']['id']

    def connect(self):
        async_to_sync(self.channel_layer.group_add)(self.group_name(self.task_id), self.channel_name)

        self.accept()

    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(self.group_name(self.task_id), self.channel_name)

    def on_event(self, event):
        task_id = event['task_id']
        task = Task.objects.get(pk=task_id)
        events = RunnerEvent.objects.filter(task=task)
        result = {
            "task": TaskSerializer(instance=task).data,
            "events": RunnerEventSerializer(instance=events, many=True).data
        }
        self.send_json(result)


class AsyncEventConsumer(AsyncJsonWebsocketConsumer):
    group_name_prefix = "iac_task"

    @classmethod
    def group_name(cls, task_id: int):
        return f'{cls.group_name_prefix}_{task_id}'

    @property
    def task_id(self):
        return self.scope['url_route']['kwargs']['id']

    async def connect(self):
        await self.channel_layer.group_add(self.group_name(self.task_id), self.channel_name)
        await self.accept()
        result, close = await self.fetch_data(self.task_id)
        await self.send_json(result, close=close)

    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.group_name(self.task_id), self.channel_name)

    @database_sync_to_async
    def fetch_data(self, task_id):
        task = Task.objects.get(pk=task_id)
        events = RunnerEvent.objects.filter(task=task)
        return {
                   "task": TaskSerializer(instance=task).data,
                   "events": RunnerEventSerializer(instance=events, many=True).data
               }, task.state in Task.finalized

    async def on_event(self, event):
        task_id = event['task_id']
        result, close = await self.fetch_data(task_id)
        await self.send_json(result, close=event.get("close", close))
