import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect('95.70.201.96', 39039)

def send_message(topic, message):
    print("Mesaj gönderildi:", topic, "|", message)
    client.publish(topic, message)

send_message("test/topic", "Bu bir test mesajidir.")

client.disconnect()