import time
import paho.mqtt.client as mqtt

broker_address="127.0.0.1"
port = ("1883")
print("creating")
client = mqtt.Client("P1")
print("connecting")
client.connect(broker_address, port)
client.loop_start()
print("Subscribing to topic","house/bulbs/bulb1")
client.subscribe("house/bulbs/bulb1")
print("Publishing message to topic","house/bulbs/bulb1")
client.publish("house/bulbs/bulb1","OFF")
time.sleep(4)
