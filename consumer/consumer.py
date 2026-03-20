import paho.mqtt.client as mqtt
import json
import requests
from anomaly import detect

BROKER = "mqtt"
PORT = 1883
TOPIC = "engie/hvac/001"
API_URL = "http://api:5000/alerts"


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("✅ Connected to MQTT broker")
        client.subscribe(TOPIC)
    else:
        print(f"❌ Failed to connect, return code {rc}")


def on_message(client, userdata, msg):
    try:
        data = json.loads(msg.payload.decode())
        print("📥 Received:", data)

        alerts = detect(data)

        for alert in alerts:
            payload = {
                "message": alert,
                "device_id": data.get("device_id"),
                "temperature": data.get("temperature"),
                "vibration": data.get("vibration"),
                "timestamp": data.get("timestamp"),
                "severity": "HIGH" if "High" in alert else "MEDIUM",
            }

            try:
                res = requests.post(API_URL, json=payload, timeout=2)
                print(f"📡 Sent to API: {payload} | Status: {res.status_code}")
            except requests.exceptions.RequestException as e:
                print(f"❌ API Error: {e}")

    except json.JSONDecodeError:
        print("❌ Invalid JSON received")


client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message

try:
    client.connect(BROKER, PORT, 60)
except Exception as e:
    print(f"❌ MQTT Connection Error: {e}")
    exit(1)

print("🚀 Consumer started...")
client.loop_forever()
