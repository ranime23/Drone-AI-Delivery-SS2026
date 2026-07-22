# Position Hold

## Overview

After working on the basic ArduPilot configuration and Altitude Hold, the project continued with the preparation and testing of **Position Hold (PosHold)**.

The objective of this development step is to improve the ability of the drone to maintain its horizontal position during flight.

For this purpose, the flight stability, altitude measurement and sensor configuration first had to be improved.

Position Hold is currently part of the ongoing development and testing process and is therefore not considered fully completed.

---

## Objectives

The work related to Position Hold currently focuses on:

- preparing the drone for stable Position Hold operation,
- improving the general flight stability,
- using the LiDAR configuration developed during the Altitude Hold work,
- working with Optical Flow for horizontal movement estimation,
- reducing vibrations,
- calibrating the required sensors,
- performing flight tests,
- observing the behaviour of the drone,
- progressively improving the configuration.

---

# 1. Prerequisites

Before starting the Position Hold work, several other parts of the drone had to be configured.

The project group therefore first worked on:

- ArduPilot installation,
- flight controller configuration,
- motor configuration,
- board orientation,
- accelerometer calibration,
- compass calibration,
- PID adjustment,
- filter configuration,
- vibration reduction,
- LiDAR installation,
- LiDAR calibration,
- Altitude Hold testing.

The main objective was to make the drone fly as calmly as possible before evaluating Position Hold.

---

# 2. Flight Stability

Flight stability was one of the most important requirements for the Position Hold tests.

During the previous flight tests, oscillations and vibrations had to be reduced.

Several ArduPilot parameters were therefore adjusted.

The current configuration includes, among others:

| Parameter | Current Value |
|-----------|--------------:|
| `INS_GYRO_FILTER` | 80 |
| `INS_ACCEL_FILTER` | 20 |
| `INS_HNTCH_ENABLE` | 1 |
| `INS_HNTCH_MODE` | 3 |
| `INS_HNTCH_FREQ` | 80 |
| `INS_HNTCH_BW` | 40 |
| `INS_HNTCH_ATT` | 40 |

The initial Roll and Pitch PID values were also reduced.

### Pitch

```text
ATC_RAT_PIT_P = 0.06
ATC_RAT_PIT_I = 0.06
ATC_RAT_PIT_D = 0.002
```

### Roll

```text
ATC_RAT_RLL_P = 0.06
ATC_RAT_RLL_I = 0.06
ATC_RAT_RLL_D = 0.002
```

These settings are documented in more detail in:

```text
autopilot.md
```

---

# 3. Altitude Information

Position Hold testing is connected to the previous Altitude Hold work.

Initially, the internal barometer of the flight controller was tested for altitude estimation.

The results were not satisfactory for the intended AltHold operation.

A LiDAR sensor was therefore mounted and calibrated.

The current Range Finder configuration includes:

| Parameter | Current Value |
|-----------|--------------:|
| `RNGFND1_MAX_CM` | 700 |
| `RNGFND1_MIN_CM` | 20 |
| `RNGFND1_GNDCLEAR` | 10 |
| `RNGFND1_ORIENT` | 25 |
| `RNGFND1_POS_X` | 0.05 |
| `RNGFND1_POS_Z` | 0.01 |
| `EK3_RNG_USE_HGT` | -1 |

The detailed LiDAR configuration is documented in:

```text
altitude-hold.md
```

and

```text
lidar-optical-flow.md
```

---

# 4. Optical Flow

Optical Flow is part of the Position Hold development.

The sensor is intended to provide information about the horizontal movement of the drone during Position Hold testing.

In contrast to the LiDAR configuration, the currently available project documentation does not contain a complete list of confirmed Optical Flow parameter changes.

For this reason, no additional Optical Flow parameter values are documented here unless they can be confirmed from the exported drone configuration or from further project documentation.

This avoids documenting configuration changes that were not actually performed by the project group.

---

# 5. Vibration Reduction

Vibration reduction remained important during the Position Hold development.

The project group therefore worked on both software and mechanical improvements.

## Software Measures

The software-related measures included:

- Gyroscope filter adjustment,
- Accelerometer filter adjustment,
- Dynamic Harmonic Notch Filter activation,
- PID adjustment.

## Mechanical Measures

Mechanical vibration damping was also introduced.

The 3D-printed landing feet were equipped with damping material.

A second version of the landing feet was later produced because more space was required underneath the drone for the servo.

This version again included damping material.

The mechanical changes were important because excessive vibration also affected the mounting of the LiDAR sensor.

---

# 6. Calibration

A considerable amount of calibration work was required during the project.

The project documentation specifically records repeated calibration work for the flight controller and sensors.

This included:

- accelerometer calibration,
- compass calibration,
- LiDAR calibration,
- verification after hardware changes.

Hardware replacement and mechanical modifications required parts of the configuration to be checked again.

---

# 7. Flight Tests

Flight tests were performed during the development process to evaluate the behaviour of the drone.

For the Position Hold preparation, particular attention was paid to:

- general flight stability,
- hover behaviour,
- vibrations,
- altitude behaviour,
- sensor behaviour.

The configuration is still being evaluated and adjusted based on the results of these tests.

---

# 8. Relation Between AltHold and PosHold

The project development log specifically identifies stable flight as an important requirement for both Altitude Hold and Position Hold.

The development sequence was therefore:

```text
Flight Controller Configuration
            ↓
Flight Stability
            ↓
Vibration Reduction
            ↓
LiDAR Installation and Calibration
            ↓
Altitude Hold Testing
            ↓
Position Hold Preparation and Testing
```

This means that Position Hold could not be treated as an isolated feature.

Problems with flight stability, vibrations or altitude measurement also influenced the Position Hold development.

---

# 9. Work Performed So Far

The following work relevant to Position Hold has been performed so far:

- ArduPilot installed and configured.
- Flight controller replaced and recalibrated.
- Board orientation corrected.
- Motor configuration adapted.
- PID values adjusted.
- Gyroscope and accelerometer filters adjusted.
- Dynamic Harmonic Notch Filter activated.
- Flight stability tested and improved.
- Internal barometer tested for Altitude Hold.
- LiDAR installed.
- LiDAR calibrated.
- Range Finder parameters configured.
- Vibration problems investigated.
- Mechanical vibration damping introduced.
- Flight tests performed.
- Preparation and testing for Position Hold started.

---

# 10. Current Status

Position Hold is currently still part of the ongoing development process.

The project group has already completed several necessary preparation steps, especially:

- flight-controller configuration,
- flight-stability improvements,
- LiDAR integration,
- sensor calibration,
- vibration reduction.

The drone is currently being tested and further adjusted to improve the conditions required for reliable Position Hold.

Therefore, Position Hold is **not documented as a fully completed function at the current project stage**.

Further results and parameter changes will be added to this documentation as the testing continues.
