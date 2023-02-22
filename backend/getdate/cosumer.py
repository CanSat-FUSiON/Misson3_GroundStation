# myapp/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
class GPSConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("gps_data", self.channel_name)
        await self.accept()
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("gps_data", self.channel_name)
    async def receive(self, text_data):
        data = json.loads(text_data)
        await self.channel_layer.group_send("gps_data", {
            "type": "gps_data",
            "data": data
        })
    async def gps_data(self, event):
        data = event["data"]
        await self.send(text_data=json.dumps(data))
