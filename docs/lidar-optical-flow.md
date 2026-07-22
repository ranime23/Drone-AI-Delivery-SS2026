# LiDAR and Optical Flow

## Overview

LiDAR and Optical Flow are part of the sensor integration work for the drone.

The LiDAR was installed and calibrated during the project to provide distance measurements between the drone and the ground. This work was particularly important for the ongoing Altitude Hold tests.

Optical Flow is intended to support horizontal position estimation for Position Hold. The complete Position Hold configuration and testing are documented separately.

This document describes the sensor-related work that has been carried out so far.

---

## Objectives

The work in this part of the project focused on:

- integrating the LiDAR sensor,
- configuring the Range Finder in ArduPilot,
- calibrating the LiDAR,
- testing distance measurements,
- investigating vibration problems,
- improving the mechanical mounting of the sensor,
- preparing the sensor configuration required for further Altitude Hold and Position Hold testing.

---

# 1. LiDAR Integration

## 1.1 Installation

The LiDAR sensor was mounted on the drone and connected to the flight controller.

The sensor is positioned so that it measures the distance between the drone and the ground.

After the mechanical installation, the corresponding Range Finder settings were configured in Mission Planner.

---

## 1.2 Calibration

The LiDAR was calibrated after installation.

Several calibration and testing steps were necessary because the sensor measurements are directly affected by:

- sensor orientation,
- mounting position,
- drone vibrations,
- mechanical stability.

The calibration was therefore not treated as a single configuration step. Measurements and flight behaviour were checked again during the development process.

---

# 2. Range Finder Configuration

The LiDAR was configured in ArduPilot through the Range Finder parameters.

The current drone configuration contains the following important settings:

| Parameter | Current Value | Purpose |
|-----------|--------------:|---------|
| `RNGFND1_MAX_CM` | 700 | Maximum configured measurement distance |
| `RNGFND1_MIN_CM` | 20 | Minimum configured measurement distance |
| `RNGFND1_GNDCLEAR` | 10 | Ground clearance |
| `RNGFND1_ORIENT` | 25 | Orientation of the sensor |
| `RNGFND1_POS_X` | 0.05 | X-position of the sensor |
| `RNGFND1_POS_Z` | 0.01 | Z-position of the sensor |
| `EK3_RNG_USE_HGT` | -1 | Current EKF Range Finder height setting |

These values correspond to the configuration currently entered for the drone.

---

## 2.1 Measurement Limits

The minimum and maximum measurement distances were configured as follows:

```text
RNGFND1_MIN_CM = 20
RNGFND1_MAX_CM = 700
```

The configured measurement range is therefore **20 cm to 700 cm**.

---

## 2.2 Ground Clearance

The following ground-clearance value was configured:

```text
RNGFND1_GNDCLEAR = 10
```

This parameter is part of the Range Finder configuration in Mission Planner.

---

## 2.3 Sensor Orientation

The current orientation parameter is:

```text
RNGFND1_ORIENT = 25
```

This setting corresponds to the orientation entered for the LiDAR in the current drone configuration.

---

## 2.4 Sensor Position

The position of the sensor relative to the flight controller was also configured:

```text
RNGFND1_POS_X = 0.05
RNGFND1_POS_Z = 0.01
```

These values represent the configured sensor offset.

---

# 3. Vibration Problems

Vibrations became an important issue during the sensor integration.

The project group observed that the drone needed to fly as calmly as possible for the sensor measurements and the subsequent Altitude Hold and Position Hold tests.

The mechanical installation of the LiDAR was also affected by vibrations.

According to the project development log, excessive vibrations could cause problems with the LiDAR attachment.

For this reason, vibration reduction became part of both the sensor integration and the mechanical frame development.

---

# 4. Mechanical Improvements

Several mechanical modifications were carried out to reduce vibrations.

## Landing Feet – Version 1

The first version of the 3D-printed landing feet was equipped with damping material.

Foam/pool-noodle material was used to absorb vibrations and landing impacts.

---

## Landing Feet – Version 2

A second version with longer landing feet was later required because additional space underneath the drone was needed for the servo.

Vibration damping was again added to this version.

The damping was also important for the LiDAR because the sensor mounting had to remain stable during flight.

---

# 5. Relation to Flight Controller Tuning

Sensor testing could not be considered independently from the flight-controller configuration.

The project group simultaneously worked on:

- PID adjustment,
- Gyroscope filtering,
- Accelerometer filtering,
- Dynamic Harmonic Notch filtering,
- vibration damping.

The objective was to obtain a sufficiently calm flight behaviour for reliable sensor testing.

The detailed flight-controller settings are documented in:

```text
autopilot.md
```

---

# 6. LiDAR and Altitude Hold

Before using the LiDAR, the internal barometer of the flight controller was tested for Altitude Hold.

The results were not satisfactory for the intended application.

The LiDAR was therefore installed and calibrated as an additional distance sensor.

The work performed for Altitude Hold includes:

- barometer testing,
- LiDAR installation,
- LiDAR calibration,
- Range Finder configuration,
- vibration investigation,
- flight testing.

The complete development status is documented in:

```text
altitude-hold.md
```

---

# 7. Optical Flow

Optical Flow belongs to the Position Hold part of the project.

Its purpose within the project is to provide information about horizontal movement when testing position stabilization.

At the current documentation stage, the available project information does not contain the same level of detailed parameter documentation for Optical Flow as it does for the LiDAR.

For this reason, no additional Optical Flow parameters are listed here without evidence from the actual drone configuration or project documentation.

The corresponding Position Hold work is documented separately in:

```text
position-hold.md
```

---

# 8. Work Performed So Far

The following sensor-related work has been documented so far:

- LiDAR physically installed.
- LiDAR connected to the flight controller.
- LiDAR calibrated.
- Range Finder configuration entered in Mission Planner.
- Minimum measurement distance configured.
- Maximum measurement distance configured.
- Sensor orientation configured.
- Sensor position configured.
- Internal barometer tested for Altitude Hold.
- Vibration problems investigated.
- Landing gear modified to improve vibration damping.
- Flight stability improved in parallel with sensor testing.
- Preparation and testing related to Altitude Hold and Position Hold continued.

---

# 9. Current Status

The LiDAR installation and its basic Range Finder configuration have been carried out.

The sensor has also been calibrated and used during the current Altitude Hold development.

Vibration reduction and flight-controller tuning are still relevant because sensor performance depends on stable flight behaviour.

Optical Flow belongs to the ongoing Position Hold development. The currently available documentation does not justify marking the complete Optical Flow/Position Hold integration as finished.

Therefore, this sensor integration work remains part of the ongoing development and testing process.
