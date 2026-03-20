def detect(data):
    alerts = []

    if data["temperature"] > 85:
        alerts.append(f"High temperature: {data['temperature']}")

    if data["vibration"] > 0.8:
        alerts.append(f"High vibration: {data['vibration']}")

    return alerts