import streamlit as st
from PIL import Image
import datetime
from collections import Counter

st.set_page_config(page_title="SeatSense UW - College Library", layout="wide")

st.title("SeatSense UW")
st.subheader("College Library - Floor 2 Prototype")

# Load floor map
image = Image.open("floor2.png")
st.image(image, caption="College Library - Floor 2", width="stretch")

st.write("Report real-time seating availability by zone.")

# Define zones
zones = {
    "Z1 - Silent Study Core": "Very quiet, focus-heavy area. Best for deep work, reading, and solo study.",
    "Z2 - Scenic Lake View Window": "Natural light and calming lake views. Ideal for relaxed solo study sessions.",
    "Z3 - Open Table Collaborative Center": "Moderate noise, open seating layout. Good for flexible study or casual collaboration.",
    "Z4 - Computer & Media Center": "Desktop computers (Windows & macOS), docking stations, and equipment checkout nearby. Active study environment.",
    "Z5 - Premium Scenic Media Studios (2252A/B)": "Smaller, quieter scenic space with premium lake views. Limited seating, high demand."
}

# Initialize report storage
if "zone_reports" not in st.session_state:
    st.session_state.zone_reports = {zone: [] for zone in zones.keys()}

# Sidebar zone selector
st.sidebar.header("Select Zone")
selected_zone = st.sidebar.selectbox("Choose a zone:", list(zones.keys()))

st.write("### Zone Description")
st.write(zones[selected_zone])

# Reporting buttons
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

reports = st.session_state.zone_reports[selected_zone]

if len(reports) == 0:
    st.info("No reports yet for this zone.")
else:
    # Only consider last 30 minutes
    now = datetime.datetime.now()
    recent_reports = [
        r for r in reports
        if (now - r["time"]).total_seconds() <= 1800
    ]

    if len(recent_reports) == 0:
        st.info("No recent reports in last 30 minutes.")
    else:
        statuses = [r["status"] for r in recent_reports]
        counts = Counter(statuses)
        most_common = counts.most_common(1)[0][0]
        total = len(statuses)

        plenty_n = counts.get("plenty", 0)
        limited_n = counts.get("limited", 0)
        full_n = counts.get("full", 0)

        confidence = round((counts[most_common] / total) * 100)

        # Display aggregated status
        if most_common == "plenty":
            st.success("🟢 Plenty of seats available")
        elif most_common == "limited":
            st.warning("🟡 Limited seats available")
        else:
            st.error("🔴 Area is full")

        st.write("### Recent Reports (last 30 min)")

        c1, c2, c3 = st.columns(3)
        c1.metric("🟢 Plenty", plenty_n)
        c2.metric("🟡 Limited", limited_n)
        c3.metric("🔴 Full", full_n)

        st.caption(f"Based on {total} report(s). Confidence: {confidence}%")