# 🔧 IoT Predictive Maintenance System

## 🚀 Overview
This project simulates a real-time IoT predictive maintenance system using MQTT, microservices, and a Streamlit dashboard.

It demonstrates an **event-driven architecture** similar to real-world industrial systems (e.g., ENGIE Smart O&M), with real-time data ingestion, anomaly detection, and monitoring.

---

## 🧱 Architecture

**End-to-End Data Flow**

Sensor Simulator → MQTT (Mosquitto) → Consumer → Flask API → Streamlit Dashboard → Prometheus → Grafana

<p align="center">
  <img src="images/workflow.png" width="800"/>
  <br/>
  <em>Figure: End-to-end IoT data pipeline architecture</em>
</p>

---

## ⚙️ Tech Stack

- MQTT (Mosquitto)
- Python (Flask, Paho-MQTT)
- Streamlit (Dashboard)
- Prometheus (Metrics collection)
- Grafana (Monitoring dashboard)
- Docker & Docker Compose

---

## ▶️ How to Run

### 1. Clone repo

```bash
git clone https://github.com/yansong2025/iot-predictive-maintenance.git
cd iot-predictive-maintenance
```

### 2. Start the system

```bash
docker-compose up --build
```

---

## 🌐 Access

- 📊 Streamlit Dashboard: http://localhost:8501  
- 🔧 API Endpoint: http://localhost:5000/alerts  
- 📈 Prometheus: http://localhost:9090  
- 📉 Grafana: http://localhost:3000  

---

## 📊 Features

- Real-time IoT data simulation  
- MQTT-based event streaming  
- Anomaly detection engine  
- Microservices architecture  
- Live monitoring dashboard (Streamlit)  
- System observability with Prometheus & Grafana  

---

## 📸 Screenshots

### 🔧 Dashboard
<p align="center">
  <img src="images/dashboard.png" width="800"/>
</p>

### 📊 Monitoring (Grafana)
<p align="center">
  <img src="images/grafana.png" width="800"/>
</p>

---

## 🧠 Key Concepts

- Event-driven architecture  
- Pub/Sub messaging (MQTT)  
- Microservices design  
- Real-time data processing  
- Observability & monitoring  

---

## 🏆 Future Improvements

- Add authentication & API gateway  
- Implement retry & fault tolerance  
- Secure MQTT with TLS  
- Deploy to cloud (AWS/GCP)  
