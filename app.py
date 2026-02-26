import streamlit as st
import datetime
from collections import Counter
from floor import render_floor

st.set_page_config(page_title="SeatSense UW - College Library", layout="wide")

st.title("SeatSense UW")
st.subheader("College Library - Floor 2 Prototype")

zones = {
    "Z1 - Silent Study Core": "Very quiet, focus-heavy area. Best for deep work.",
    "Z2 - Scenic Lake View Window": "Natural light and calming lake views.",
    "Z3 - Open Table Collaborative Center": "Moderate noise, flexible seating.",
    "Z4 - Computer & Media Center": "Desktop computers and docking stations.",
    "Z5 - Premium Scenic Media Studios (2252A/B)": "Smaller scenic media space."
}

if "zone_reports" not in st.session_state:
    st.session_state.zone_reports = {zone: [] for zone in zones.keys()}

st.sidebar.header("Select Zone")
selected_zone = st.sidebar.selectbox("Choose a zone:", list(zones.keys()))

st.write("### Zone Description")
st.write(zones[selected_zone])

st.write("### Report Seat Availability")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🟢 Plenty", use_container_width=True):
        st.session_state.zone_reports[selected_zone].append(
            {"status": "plenty", "time": datetime.datetime.now()}
        )

with col2:
    if st.button("🟡 Limited", use_container_width=True):
        st.session_state.zone_reports[selected_zone].append(
            {"status": "limited", "time": datetime.datetime.now()}
        )

with col3:
    if st.button("🔴 Full", use_container_width=True):
        st.session_state.zone_reports[selected_zone].append(
            {"status": "full", "time": datetime.datetime.now()}
        )

st.write("### Current Status")

overlay_color = None

reports = st.session_state.zone_reports[selected_zone]

if reports:
    now = datetime.datetime.now()
    recent_reports = [
        r for r in reports
        if (now - r["time"]).total_seconds() <= 1800
    ]

    if recent_reports:
        statuses = [r["status"] for r in recent_reports]
        counts = Counter(statuses)
        most_common = counts.most_common(1)[0][0]
        total = len(statuses)

        confidence = round((counts[most_common] / total) * 100)

        if most_common == "plenty":
            st.success("🟢 Plenty of seats available")
            overlay_color = "rgba(0, 200, 0, 0.5)"

        elif most_common == "limited":
            st.warning("🟡 Limited seats available")
            overlay_color = "rgba(255, 200, 0, 0.5)"

        else:
            st.error("🔴 Area is full")
            overlay_color = "rgba(255, 0, 0, 0.5)"

        st.caption(f"Confidence: {confidence}%")

    else:
        st.info("No recent reports in last 30 minutes.")
else:
    st.info("No reports yet for this zone.")

st.write("### Floor Layout")

render_floor(selected_zone, overlay_color)