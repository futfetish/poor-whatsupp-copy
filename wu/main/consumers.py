from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json


from .models import C_user, Channel, Msg


class Ls(WebsocketConsumer):

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.room_pk = None
        self.group_name = None
        self.room = None
        self.other_user = None

    def connect(self):
        self.room_pk = self.scope['url_route']['kwargs']['pk']
        self.group_name = f'channel_{self.room_pk}'
        self.room = Channel.objects.get(id=self.room_pk)
        self.other_user = Channel.objects.get(id=self.room_pk).members.exclude(id=self.scope['user'].id)[0]
        # connection has to be accepted
        self.accept()

        # join the room group
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name,
        )



    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,
            self.channel_name,
        )

    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']



        # send chat message event to the room
        async_to_sync(self.channel_layer.group_send)(
            self.group_name,
            {
                'type': 'chat_message',
                'message': message,
                'user': self.scope['user'].username,
            }
        )
        Msg.objects.create(sent=self.scope['user'], point=self.other_user, text=message,channel=Channel.objects.get(id=self.room_pk))

    def chat_message(self, event):
        self.send(text_data=json.dumps(event))

