from flask import Flask, jsonify, request
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
import time
REQUEST_COUNT = Counter("api_requests_total", "Total API Requests")
ALERT_COUNT = Counter("alerts_created_total", "Total alerts created")
app = Flask(__name__)

# Temporary in-memory store
alerts = []

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {"Content-Type": CONTENT_TYPE_LATEST}
# GET all alerts / POST new alert
@app.route("/alerts", methods=["GET", "POST"])
def handle_alerts():
    if request.method == "POST":
        data = request.get_json()

        # Validate payload
        if not data or "message" not in data:
            return {"error": "Invalid payload"}, 400

        # Enrich data (ensure consistency)
        alert = {
            "message": data.get("message"),
            "device_id": data.get("device_id", "unknown"),
            "temperature": data.get("temperature"),
            "vibration": data.get("vibration"),
            "severity": data.get("severity", "MEDIUM"),
            "timestamp": data.get("timestamp", time.time())
        }

        alerts.append(alert)

        print(f"📥 Alert stored: {alert}")  # logging

        return {"status": "alert added"}, 201

    return jsonify(alerts)


# Health check
@app.route("/")
def home():
    return {"status": "API running"}


# Optional: readiness endpoint (future scaling / monitoring)
@app.route("/health")
def health():
    return {"status": "healthy", "alerts_count": len(alerts)}


if __name__ == "__main__":
    # 🔥 CRITICAL for Docker
    app.run(host="0.0.0.0", port=5000, debug=True)