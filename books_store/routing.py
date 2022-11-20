from django.urls import path

from websockets_demo.consumers import  CounterConsumer

websocket_urlpatterns = [
    path("ws/counter/", CounterConsumer.as_asgi())
]
