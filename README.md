# 📡 Real-Time Sensor Data Monitoring System using MQTT

## 🚀 Overview

This project simulates a real-time IoT system for monitoring temperature and humidity using the MQTT protocol. It demonstrates how data flows from a publisher to a subscriber through a broker and is visualized live.

---

## 🧠 System Architecture

```
Sensor Simulator (Publisher)
        ↓
   MQTT Broker (Mosquitto)
        ↓
Subscriber (Python)
        ↓
Live Graph (Matplotlib)
```

---

## ✨ Features

* 📡 MQTT-based communication using Mosquitto
* 🔄 Real-time data streaming
* 🌡️ Simulated temperature data
* 💧 Simulated humidity data
* 📊 Live plotting using Matplotlib
* 🧠 Publisher–Subscriber architecture

---

## 🛠️ Technologies Used

* Python
* Paho-MQTT
* Mosquitto MQTT Broker
* Matplotlib

---

## 📂 Project Structure

```
sensor_logger/
│── sensor_simulator.py   # MQTT Publisher (generates sensor data)
│── subscriber.py         # MQTT Subscriber (plots live graph)
│── plot_data.py          # (Optional) Old file-based plotting
│── README.md
│── .gitignore
```

---

## ⚙️ Setup Instructions

### 1️⃣ Install Dependencies

```bash
py -m pip install paho-mqtt matplotlib
```

---

### 2️⃣ Install Mosquitto

Download from:
👉 https://mosquitto.org/download/

---

### 3️⃣ Start MQTT Broker

```bash
mosquitto
```

---

### 4️⃣ Run Subscriber (Graph)

```bash
py subscriber.py
```

---

### 5️⃣ Run Publisher (Sensor Data)

```bash
py sensor_simulator.py
```

---

## 📊 Output

* Live graph displaying:

  * Temperature vs Time
  * Humidity vs Time
* Real-time updates using MQTT communication

---

## 💼 Applications

* IoT monitoring systems
* Smart home automation
* Industrial sensor monitoring
* Real-time data visualization

---

## 🔮 Future Improvements

* 🚨 Threshold-based alerts
* 📁 Data storage and logging
* 🌐 Web dashboard (Streamlit)
* 📡 Integration with real hardware (ESP32)

---

## 👩‍💻 Author

Varshini
B.Tech ECE Student

---
