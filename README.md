# 📊 Sensor Data Logger & Visualization (Python)

## 🚀 Overview

This project simulates real-time sensor data (temperature and humidity), logs the data into a file, and visualizes it using a single graph.

It demonstrates a simple end-to-end data pipeline:

* Data Generation
* Data Logging
* Data Visualization

---

## 🧠 Features

* 🌡️ Simulates temperature data with random variation
* 💧 Simulates humidity data with random variation
* 📝 Logs data into a `.log` file
* 📊 Plots both temperature and humidity on a **single graph**
* ⏱️ Time-based data tracking

---

## 🛠️ Technologies Used

* Python
* Matplotlib
* File Handling

---

## 📂 Project Structure

```
sensor_logger/
│── sensor_simulator.py   # Generates and logs sensor data
│── plot_data.py          # Reads log file and plots graph
│── sensor.log            # Generated data file
│── README.md
```

---

## ▶️ How to Run

### 1️⃣ Run the simulator

```
py sensor_simulator.py
```

This will generate sensor data and store it in `sensor.log`.

---

### 2️⃣ Plot the data

```
py plot_data.py
```

This will display a graph with:

* Temperature (°C)
* Humidity (%)

---

## 📊 Output

The output is a **single graph** showing both:

* Temperature variation over time
* Humidity variation over time

---

## 💡 Example Use Cases

* IoT data simulation
* Sensor data analysis
* Basic data visualization projects
* Learning file handling and plotting in Python

---

## 🔮 Future Improvements

* Real-time plotting
* Threshold-based alerts
* GUI dashboard (Streamlit)
* Integration with actual sensors

---

## 👩‍💻 Author

Varshini
B.Tech ECE Student

---
