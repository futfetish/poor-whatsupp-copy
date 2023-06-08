from channels.generic.websocket import AsyncWebsocketConsumer
from django.shortcuts import get_object_or_404

from .models import C_user


class LsConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.ls_id = self.scope["url_route"]["kwargs"]["pk"]
        self.ls_instance = await self.get_ls_instance()
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        # Обработка полученного сообщения от клиента
        # Возможно, отправка нового сообщения обратно через WebSocket
        await self.send_message()

    async def send_message(self):
        # Отправка обновленных данных через WebSocket
        await self.send(text_data="update")

    async def get_ls_instance(self):
        # Получение экземпляра ls
        ls_id = self.ls_id
        return get_object_or_404(C_user, pk=ls_id)