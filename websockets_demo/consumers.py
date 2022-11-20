from asyncio import sleep
import json
import random
from channels.generic.websocket import WebsocketConsumer


class CounterConsumer(WebsocketConsumer):

    def connect(self):
        self.accept()
        print("Socket is connected")
        counter = 0
        while True:
            data = {
                'counter': random.randint(1, 1000)
            }

            self.send(json.dumps(data))
            counter += 1
            sleep(1)
        

    def disconnect(self, code):
        print("Socket disconnected with code", code)


    
