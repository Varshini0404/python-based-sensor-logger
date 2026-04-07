import matplotlib.pyplot as plt

time = []
temp = []
hum = []

with open("sensor.log") as f:
    for line in f:
        t, te, h = line.strip().split(",")
        time.append(int(t))
        temp.append(float(te))
        hum.append(float(h))

plt.plot(time, temp, label="Temperature")
plt.plot(time, hum, label="Humidity")
plt.xlabel("Time (s)")
plt.ylabel("Value")
plt.legend()
plt.grid()
plt.show()
