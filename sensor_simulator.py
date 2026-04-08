import paho.mqtt.client as mqtt
import time
import random

client = mqtt.Client()
client.connect("localhost", 1883, 60)

t = 0

while True:
    temperature = random.uniform(23, 27)
    humidity = random.uniform(55, 65)

    message = f"{t},{temperature:.2f},{humidity:.2f}"
    client.publish("sensor/data", message)

    print("Sent:", message)

    t += 1
    time.sleep(1)