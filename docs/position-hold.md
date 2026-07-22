# Position Hold

## Overview

Position Hold is one of the most important autonomous flight modes of the project. Unlike Altitude Hold, which only controls the flight altitude, Position Hold enables the drone to maintain both its altitude and its horizontal position.

Since the project was designed for indoor autonomous navigation, GPS could not be used reliably. Therefore, Position Hold was implemented using the combination of a LiDAR sensor for altitude estimation and an Optical Flow sensor for horizontal position estimation.

The successful implementation of Position Hold was an important milestone towards autonomous package delivery.

---

# Objectives

The objectives of this work package were:

- Maintain a stable position during hover
- Reduce pilot corrections
- Enable GPS-independent indoor flight
- Integrate Optical Flow with LiDAR
- Prepare autonomous navigation

---

# Required Components

| Component | Purpose |
|-----------|----------|
| Flywoo GOKU GN745 | Flight Controller |
| LiDAR MTF-01P | Altitude measurement |
| Optical Flow Sensor | Position estimation |
| ArduPilot | Flight control software |
| Mission Planner | Configuration and testing |

---

# Prerequisites

Before Position Hold could be activated, several requirements had to be fulfilled.

The following milestones had already been completed:

- Successful ArduPilot installation
- Stable Flight Controller configuration
- Sensor calibration
- Successful Altitude Hold
- LiDAR integration
- Reduction of flight vibrations

Only after these steps could reliable Position Hold testing begin.

---

# Sensor Fusion

Position Hold combines information from multiple sensors.

## LiDAR

The LiDAR continuously measures the distance between the drone and the ground.

Its measurements are used to maintain a constant flight altitude.

---

## Optical Flow

The Optical Flow sensor observes the ground below the drone.

By tracking visual features between consecutive images, it estimates horizontal movement without requiring GPS.

This information allows the Flight Controller to compensate for small movements caused by air turbulence or pilot input.

---

# Flight Testing

Several indoor flight tests were carried out.

Each flight evaluated:

- Hover stability
- Position accuracy
- Sensor behaviour
- Influence of vibrations
- Optical Flow performance

Whenever unstable behaviour was observed, the parameters were adjusted before the next flight.

---

# Challenges

During development several problems had to be solved.

## Flight Vibrations

Strong vibrations reduced the quality of both LiDAR and Optical Flow measurements.

Additional vibration damping was therefore implemented before continuing Position Hold testing.

---

## Sensor Calibration

Both sensors required repeated calibration after hardware modifications.

Accurate calibration was essential for reliable position estimation.

---

## Stable Hover

Position Hold only worked reliably after achieving a stable hover using Altitude Hold.

For this reason, flight controller tuning and vibration reduction were completed first.

---

# Results

The following milestones were successfully achieved:

- Successful integration of Optical Flow
- Successful integration of LiDAR
- Stable indoor hovering
- Reliable Position Hold
- GPS-independent position stabilization

The drone was able to maintain its position significantly better than during manual flight.

---

# Lessons Learned

Several important observations were made during testing.

- Position Hold depends heavily on a stable Altitude Hold.
- Optical Flow performs best at low indoor flight altitudes.
- Reducing vibrations greatly improves position estimation.
- Proper sensor calibration is essential for stable autonomous flight.

---

# Future Improvements

Future work focuses on:

- Further optimization of Optical Flow parameters
- Raspberry Pi integration
- AI Camera integration
- Autonomous waypoint navigation
- AI-based object delivery
