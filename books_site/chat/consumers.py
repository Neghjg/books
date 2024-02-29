#import json

#from channels.generic.websocket import AsyncWebsocketConsumer


#class ChatConsumer(AsyncWebsocketConsumer):
#    async def connect(self):
#        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
#        self.room_group_name = f"chat_{self.room_name}"

        # Join room group
#        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

#        await self.accept()

#    async def disconnect(self, close_code):
        # Leave room group
#        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    #async def receive(self, text_data):
      #  text_data_json = json.loads(text_data)
     #   message = text_data_json["message"]

        # Send message to room group
    #    await self.channel_layer.group_send(
   #         self.room_group_name, {"type": "chat.message", "message": message}
 #       )

    # Receive message from room group
  #  async def chat_message(self, event):
 #       message = event["message"]

        # Send message to WebSocket
#        await self.send(text_data=json.dumps({"message": message}))

import json
import requests
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from django.utils import timezone
from chat.models import ChatMessage2, UserMessege2


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.user = self.scope['user']
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"
        self.room = ChatMessage2.objects.get(id=self.room_name)
        
        
        

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        self.accept()
        
        
        message = UserMessege2.objects.filter(chat_room=self.room).order_by("-id")[:10]
        for mes in reversed(message):
            self.send(text_data=json.dumps({
                "message": mes.text
            }))

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        #UserMessege2.objects.create(chat_room=self.room_name, user=self.user, text=message)
        UserMessege2.objects.create(chat_room=self.room, user=self.user, text=message)
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"type": "chat.message", "message": message,
                                   'user': self.user.username, }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event["message"]

        # Send message to WebSocket
        self.send(text_data=json.dumps({"message": message}))