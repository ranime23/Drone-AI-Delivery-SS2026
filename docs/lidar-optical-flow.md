# LiDAR and Optical Flow Integration

## Overview

Reliable autonomous indoor flight requires accurate altitude and position estimation. Since GPS signals are often unavailable or unreliable indoors, additional sensors are necessary to stabilize the drone.

To achieve this, two complementary sensors were integrated into the system:

- A LiDAR sensor for altitude measurement
- An Optical Flow sensor for horizontal position estimation

Together, these sensors provide the information required for stable autonomous flight modes such as Altitude Hold and Position Hold.

---

# Objectives

The objectives of this work package were:

- Improve indoor flight stability
- Enable GPS-independent navigation
- Integrate LiDAR for precise altitude measurement
- Integrate Optical Flow for horizontal motion estimation
- Support autonomous flight modes

---

# Hardware

| Component | Description |
|-----------|-------------|
| LiDAR Sensor | MicroAir MTF-01P |
| Optical Flow Sensor | Optical Flow Module |
| Flight Controller | Flywoo GOKU GN745 |
| Software | ArduPilot + Mission Planner |

---

# LiDAR Sensor

## Purpose

The LiDAR sensor continuously measures the distance between the drone and the ground.

Unlike the internal barometer, LiDAR provides highly accurate altitude measurements at low flight heights, making it especially suitable for indoor environments.

The sensor became the primary altitude source during autonomous indoor flight.

---

## Installation

The LiDAR sensor was mounted underneath the drone frame.

Several mounting positions were evaluated before selecting the final configuration.

After installation, the sensor was fixed securely to minimize movement caused by vibrations.

The sensor was then calibrated using Mission Planner.

---

## Advantages

The LiDAR sensor provides:

- High measurement accuracy
- Fast distance updates
- Reliable operation indoors
- Stable altitude estimation
- Improved hover performance

---

# Optical Flow Sensor

## Purpose

The Optical Flow sensor measures the horizontal movement of the drone by tracking visual features on the ground.

Instead of using GPS coordinates, it calculates the relative movement between consecutive images captured below the drone.

This information allows the Flight Controller to maintain the current position while hovering.

---

## Integration

The Optical Flow sensor was connected to the Flight Controller and configured in ArduPilot.

Its measurements were combined with the LiDAR altitude information to improve the accuracy of Position Hold.

Both sensors work together continuously during flight.

---

# Sensor Fusion

Neither sensor alone is sufficient for reliable indoor navigation.

The Flight Controller combines information from both sensors.

| Sensor | Function |
|---------|----------|
| LiDAR | Altitude measurement |
| Optical Flow | Horizontal movement estimation |

This sensor fusion allows the drone to maintain both altitude and position without GPS.

---

# Flight Testing

Several indoor test flights were performed after integrating both sensors.

The following aspects were evaluated:

- Sensor communication
- Altitude estimation
- Position stability
- Hover performance
- Sensor reliability

The sensors were recalibrated whenever mechanical modifications affected their alignment.

---

# Challenges

During development several difficulties occurred.

## Vibrations

Flight vibrations affected both LiDAR measurements and Optical Flow performance.

To solve this problem:

- vibration damping was improved,
- landing gear was redesigned,
- sensor mounting was reinforced.

---

## Sensor Alignment

Correct alignment of the sensors was essential.

Even small mounting errors influenced altitude estimation and position stability.

Several adjustments were therefore necessary during testing.

---

# Results

The integration of both sensors was successful.

The following improvements were achieved:

- Reliable altitude measurement
- Stable indoor hovering
- GPS-independent Position Hold
- Improved flight stability
- Better autonomous flight performance

The combination of LiDAR and Optical Flow significantly increased the overall performance of the drone during indoor flight.

---

# Lessons Learned

The development process showed that:

- LiDAR is more reliable than the internal barometer for low-altitude indoor flight.
- Optical Flow requires stable lighting conditions and a textured surface.
- Flight stability strongly influences sensor performance.
- Careful calibration is essential for reliable autonomous flight.

---

# Future Work

Future development will focus on:

- Further optimization of sensor parameters
- Raspberry Pi integration
- AI Camera integration
- Autonomous navigation
- AI-supported object delivery
