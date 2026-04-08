import paho.mqtt.client as mqtt
import matplotlib.pyplot as plt

time_data = []
temp = []
hum = []

# 👉 Only store data here (NO plotting)
def on_message(client, userdata, msg):
    data = msg.payload.decode()
    t, te, h = data.split(",")

    time_data.append(int(t))
    temp.append(float(te))
    hum.append(float(h))

client = mqtt.Client()
client.connect("localhost", 1883, 60)

client.subscribe("sensor/data")
client.on_message = on_message

# 👉 Start MQTT loop
client.loop_start()

# 👉 Plot in MAIN THREAD
plt.ion()
fig, ax = plt.subplots()

while True:
    ax.clear()
    ax.plot(time_data, temp, label="Temperature")
    ax.plot(time_data, hum, label="Humidity")
    ax.legend()
    ax.grid()

    plt.pause(0.5)