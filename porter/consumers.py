from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from .models import BuildTask
from .serializers import BuildTaskSerializer


class BuildTaskConsumer(AsyncJsonWebsocketConsumer):
    group_name_prefix = "port_build_task"

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
        task = BuildTask.objects.get(pk=task_id)
        return BuildTaskSerializer(instance=task).data, task.state in BuildTask.finalized

    async def on_event(self, event):
        data = event['task']
        await self.send_json(data, close=event.get("close", False))
