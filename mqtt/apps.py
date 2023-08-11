from django.apps import AppConfig
from datetime import datetime
import json
import paho.mqtt.client as mqtt_client
import uuid 

class MqttConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mqtt'

# def ready(self):
    #     from .models import Device

    #     def mqttConsts():
    #         data = {
    #             "broker": "95.70.201.96",
    #             "port": 39039,
    #             "username": "gesk",
    #             "password": "gesk2022",
    #             "client_id": str(uuid.uuid4()),
    #             "topic_sub": "test/topic"
    #         }
    #         return data

    #     broker = mqttConsts()['broker']
    #     port = mqttConsts()['port']
    #     topic_sub = mqttConsts()['topic_sub']
    #     client_id = mqttConsts()['client_id']
    #     username = mqttConsts()['username']
    #     password = mqttConsts()['password']

    #     my_client = mqtt_client.Client(client_id)
    #     my_client.username_pw_set(username, password)


    #     def on_connect(client, userdata, flags, rc):
    #         if rc == 0:
    #             print("CONTAINER:Successfully connected to MQTT broker",)
    #             my_client.subscribe(topic_sub)
    #         if rc != 0:
    #             print("CONTAINER:Failed to connect, return code %d", rc)


    #     def on_message(client, userdata, msg):
    #         try:
    #             # Gelen message değerini parse ediyorum.
    #             json_value = json.loads(str(msg.payload.decode()).replace('#', '').replace('True', '"True"').replace('False', '"False"').strip().replace('\'', '\"').replace('": "', '":"').replace('$', ''))



    #             Device.objects.create(
    #                 topic=topic_sub,
    #                 message=str(msg.payload.decode()),
    #             )


    #             print("json_value : " ,json_value)
    #             print("json_value['device'] : " ,json_value['device']['deltaTemp'])


    #         except Exception as e:
    #             print("ERROR : ", e)
    #             now = datetime.now()
    #             errorData = f'{now}, {str(msg.topic)}, {str(e)}, {msg.payload} \n'
                
    #             f = open('ContainerConfigError.txt', 'a')
    #             f.write(errorData)
    #             f.close()

    #     def on_disconnect(client, userdata, rc):
    #         print(rc)
    #         print("CONTAINER:DİSCONNECTED")
    #         # my_client.reconnect()
        
    #     my_client.on_disconnect = on_disconnect
    #     my_client.on_connect = on_connect
    #     my_client.connect(broker, port)
    #     my_client.on_message = on_message
    #     my_client.loop_start()