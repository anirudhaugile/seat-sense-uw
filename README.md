# SeatSense UW

Real-time crowd-sourced seating intelligence for UW–Madison libraries.

---

## Problem

UW–Madison libraries provide floor-level occupancy data, but not zone-level visibility.  
Students waste time walking across entire floors searching for available seating in specific areas (window seats, silent zones, media centers, etc.).

There is no granular, real-time crowd consensus for seating availability.

---

## Solution

SeatSense UW provides:

- Zone-level seating availability
- Real-time crowd reporting
- 30-minute rolling aggregation window
- Majority vote consensus logic
- Confidence scoring
- Vote breakdown metrics

This allows students to quickly assess which specific areas are available before walking across the entire library.

---

## Current Implementation (Prototype v1)

Library: College Library – Floor 2

Features implemented:

- 5 clearly defined seating zones
- Interactive zone selection
- Crowd reporting system (Plenty / Limited / Full)
- Timestamped reports
- 30-minute aggregation filter
- Majority vote status calculation
- Vote breakdown dashboard
- Confidence percentage indicator

Reports are currently stored in session state (non-persistent).

---

## Tech Stack

- Python
- Streamlit
- Session State management
- Time-based filtering (datetime)
- Aggregation logic using `collections.Counter`

---

## How to Run Locally

1. Clone the repository
2. Create virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
