from django.urls import path
from . import views

websocket_urlpatterns = [
    path('ws/gps/', views.GPSConsumer.as_asgi()),
]
