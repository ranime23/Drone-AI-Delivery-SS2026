# Autopilot Integration

## Overview

The flight controller is the central component of the drone and is responsible for flight stabilization, sensor fusion and execution of autonomous flight modes.

Within this project, ArduPilot was selected as the flight control software because it supports advanced autonomous flight functions such as Altitude Hold, Position Hold and sensor integration.

The objective of this work package was to configure the flight controller, calibrate all required sensors and create a stable platform for the remaining project components.

---

# Objectives

The main objectives were:

- Install ArduPilot firmware
- Configure the Flight Controller
- Integrate all required sensors
- Configure ESC communication
- Optimize flight stability
- Prepare autonomous flight modes
- Enable communication with Mission Planner

---

# Hardware

| Component | Description |
|-----------|-------------|
| Flight Controller | Flywoo GOKU GN745 |
| ESC | Integrated 4in1 ESC |
| Receiver | ELRS Receiver |
| GPS | External GPS Module |
| LiDAR | MicroAir MTF-01P |
| Raspberry Pi | Raspberry Pi Zero 2 WH |

---

# Software

- ArduPilot
- Mission Planner
- GitHub

---

# Installation

The original Flight Controller was replaced during the project after hardware issues occurred.

After installing the new Flywoo GOKU GN745 Flight Controller, ArduPilot firmware was flashed using Mission Planner.

Once the installation was completed, communication between the Flight Controller and Mission Planner was verified successfully.

---

# Sensor Calibration

A complete calibration of all required sensors was performed.

This included:

- Accelerometer calibration
- Compass calibration
- Radio calibration
- ESC configuration
- Flight mode configuration

Several calibration procedures had to be repeated after replacing hardware components.

---

# Board Orientation

The Flight Controller is mounted with a 45° offset relative to the drone frame.

To compensate for this mounting position, a custom board orientation was configured inside Mission Planner.

Configuration:

- AHRS_ORIENTATION = Custom Rotation
- CUST_ROT1_ROLL = 180°
- CUST_ROT1_PITCH = 0°
- CUST_ROT1_YAW = 225°

This configuration ensures that the software correctly interprets the physical orientation of the aircraft. :contentReference[oaicite:2]{index=2}

---

# Motor Configuration

After flashing ArduPilot, the motor configuration was adapted to the ArduPilot motor order.

The ESC protocol was changed to DShot600.

Configuration:

- MOT_PWM_TYPE = 6
- MOT_SPIN_ARM = 0.03
- MOT_SPIN_MIN = 0.06

DShot600 provides fast and reliable digital communication between the Flight Controller and ESC while supporting ESC telemetry. :contentReference[oaicite:3]{index=3}

---

# Flight Controller Tuning

The drone uses a 3.5-inch ducted frame.

During the first test flights strong oscillations occurred.

To improve flight stability, several filter parameters were modified.

The following parameters were adjusted:

| Parameter | Value |
|-----------|-------|
| INS_GYRO_FILTER | 80 |
| INS_ACCEL_FILTER | 20 |

Additionally, the Dynamic Harmonic Notch Filter was enabled to suppress motor vibrations before PID calculations.

Configuration:

- INS_HNTCH_ENABLE = 1
- INS_HNTCH_MODE = ESC Telemetry
- INS_HNTCH_FREQ = 80
- INS_HNTCH_BW = 40
- INS_HNTCH_ATT = 40

These modifications significantly reduced vibration-induced noise. :contentReference[oaicite:4]{index=4}

---

# PID Optimization

Before the first stable flights, conservative PID values were selected.

The proportional, integral and derivative gains for Roll and Pitch were reduced to improve stability during hover.

| Parameter | Value |
|-----------|-------|
| ATC_RAT_PIT_P | 0.06 |
| ATC_RAT_PIT_I | 0.06 |
| ATC_RAT_PIT_D | 0.002 |
| ATC_RAT_RLL_P | 0.06 |
| ATC_RAT_RLL_I | 0.06 |
| ATC_RAT_RLL_D | 0.002 |

These values provided a stable starting point for further flight testing. :contentReference[oaicite:5]{index=5}

---

# Hardware Modifications

During the project several hardware components had to be replaced.

The following modifications were carried out:

- Replacement of the Flight Controller
- Replacement of the GPS module
- Replacement of the video transmitter antenna
- Re-soldering of power cables
- Additional heat-shrink tubing for cable protection

After each modification the drone was recalibrated before further testing.

---

# Flight Testing

Following each hardware or software modification, multiple test flights were performed.

The objectives of these flights were:

- Verify sensor functionality
- Improve flight stability
- Reduce vibrations
- Validate controller tuning
- Prepare Altitude Hold
- Prepare Position Hold

Stable hovering was considered the primary milestone before implementing autonomous flight modes.

---

# Results

The following milestones were successfully achieved:

- Successful installation of ArduPilot
- Stable Mission Planner communication
- Complete sensor calibration
- Correct Flight Controller orientation
- Successful ESC configuration
- Stable DShot600 communication
- Improved vibration suppression
- Stable hover
- Successful preparation for Altitude Hold
- Successful preparation for Position Hold

---

# Lessons Learned

Several important observations were made during development:

- Flight stability depends strongly on proper calibration.
- Small drones require different tuning parameters than larger platforms.
- Hardware replacement requires complete recalibration.
- Vibration reduction is essential for reliable autonomous flight.
- Stable hovering is the foundation for all autonomous flight modes.

---

# Next Steps

The configured autopilot system provides the foundation for the remaining work packages.

Future development focuses on:

- LiDAR-based Altitude Hold
- Optical Flow Position Hold
- Raspberry Pi integration
- AI Camera integration
- Autonomous package delivery
