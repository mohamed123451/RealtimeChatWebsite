import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.generic.websocket import WebsocketConsumer

"""
class chatRoomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'tester_message',
                'tester': 'hello world',
            }
        )

    async def tester_message(self, event):
        tester = event['tester']

        await self.send(text_data=json.dumps({
            'tester': tester,
        }))

    async def disconnect(self, close_code):
        return await self.channel_layer.groupdiscard(
            self.room_group_name,
            self.channel_name
        )
    
    pass

"""
    
"""
This is a synchronous WebSocket consumer that 
    accepts all connections, 
    receives messages from its client, 
    and echos those messages back to the same client. 
For now it does not broadcast messages to other clients in the same room.
"""
class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = "###" + text_data_json["message"] 

        self.send(text_data=json.dumps({"message": message}))