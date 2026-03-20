import paho.mqtt.client as mqtt
import time
import json
import random

BROKER = "localhost"
PORT = 1883
TOPIC = "engie/hvac/001"

client = mqtt.Client()
client.connect("mqtt", PORT, 60)


def generate_data():
    return {
        "device_id": "hvac_001",
        "temperature": random.randint(60, 100),
        "vibration": round(random.uniform(0.1, 1.0), 2),
        "timestamp": time.time()
    }

while True:
    data = generate_data()
    client.publish(TOPIC, json.dumps(data))
    print("📡 Sent:", data)
    time.sleep(2)