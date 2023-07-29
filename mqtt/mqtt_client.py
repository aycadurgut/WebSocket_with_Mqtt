from django.http import HttpResponse
import paho.mqtt.client as mqtt
import datetime
from .models import Device
import json

def on_message(client, userdata, msg):
    print("msg.payload : " , str(msg.payload).replace("b'",'').replace(".'",''))
    Device.objects.create(topic=msg.topic, message=str(msg.payload).replace("b'",'').replace(".'",''))

def on_connect(client, userdata, flags, rc):
    try:
        print("Bağlandı: " + str(rc))
        client.subscribe("test/topic")
        client.loop()
    except Exception as error:
        print(error)

client = mqtt.Client("gesk_listeneaaaar")
client.username_pw_set(username="ayca", password="kiviseverim")
client.on_connect = on_connect
client.on_message = on_message
client.connect('', )
client.loop_start()