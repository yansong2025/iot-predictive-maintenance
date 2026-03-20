import streamlit as st
import requests
import pandas as pd
from streamlit_autorefresh import st_autorefresh

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="IoT Monitoring Dashboard",
    layout="wide"
)

st.title("🔧 IoT Predictive Maintenance Dashboard")

API_URL = "http://api:5000/alerts"

# ---------------- Sidebar ----------------
st.sidebar.header("⚙️ Controls")

refresh_rate = st.sidebar.slider("Refresh rate (seconds)", 1, 10, 2)
selected_device = st.sidebar.text_input("Filter by Device ID (optional)")

# ---------------- Auto Refresh (FIXED) ----------------
st_autorefresh(interval=refresh_rate * 1000, key="refresh")

# ---------------- Fetch Data ----------------
try:
    res = requests.get(API_URL, timeout=3)
    data = res.json()
except Exception as e:
    st.error(f"❌ API Error: {e}")
    data = []

# ---------------- Process Data ----------------
if data:
    df = pd.DataFrame(data)

    # Ensure timestamp formatting
    if "timestamp" in df:
        df["timestamp"] = pd.to_datetime(df["timestamp"], unit="s")

    # Apply device filter
    if selected_device:
        df = df[df["device_id"] == selected_device]

    # ---------------- Metrics ----------------
    st.subheader("📊 System Summary")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Alerts", len(df))

    if "device_id" in df:
        col2.metric("Devices", df["device_id"].nunique())

    if "severity" in df:
        high_alerts = df[df["severity"] == "HIGH"].shape[0]
        col3.metric("High Severity Alerts", high_alerts)

    # ---------------- Alerts Table ----------------
    st.subheader("🚨 Alerts")

    if "timestamp" in df:
        df = df.sort_values(by="timestamp", ascending=False)

    st.dataframe(df, use_container_width=True)

    # ---------------- Charts ----------------
    st.subheader("📈 Analytics")

    col1, col2 = st.columns(2)

    # Temperature trend
    if "temperature" in df and "timestamp" in df:
        col1.write("🌡️ Temperature Trend")
        col1.line_chart(df.set_index("timestamp")["temperature"])

    # Alerts by device
    if "device_id" in df:
        col2.write("📊 Alerts by Device")
        device_counts = df["device_id"].value_counts()
        col2.bar_chart(device_counts)

    # ---------------- Severity Breakdown ----------------
    if "severity" in df:
        st.subheader("⚠️ Severity Distribution")
        severity_counts = df["severity"].value_counts()
        st.bar_chart(severity_counts)

else:
    st.info("No alerts yet...")