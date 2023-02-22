# myapp/routing.py
from django.urls import re_path
from . import consumers
websocket_urlpatterns = [
    re_path(r'ws/gps/', consumers.GPSConsumer.as_asgi()),
]




