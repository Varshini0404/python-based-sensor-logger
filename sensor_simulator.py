import time
import random

LOG_FILE = "sensor.log"

with open(LOG_FILE, "a") as f:
    for t in range(100):
        temperature = 25 + random.uniform(-2, 2)
        humidity = 60 + random.uniform(-5, 5)

        f.write(f"{t},{temperature:.2f},{humidity:.2f}\n")
        print(f"Logged: {temperature:.2f} C, {humidity:.2f} %")

        time.sleep(0.5)
