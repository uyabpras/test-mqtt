import paho.mqtt.client as mqtt
import time

broker_address="127.0.0.1"

print("creating new instance")
client = mqtt.Client("P2")

client.connect(broker_address, port=1883)
print("connecting to broker")

client.loop_start()

print("publish something")
for i in range (10):
    time.sleep(1)

print("Publishing message to topic","test")
client.publish("test", "hallo")

client.loop_stop()
