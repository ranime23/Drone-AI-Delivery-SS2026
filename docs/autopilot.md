# Autopilot Configuration

# Overview

The first major task of our project was replacing the original Betaflight firmware with **ArduPilot Copter 4.6.x** on the Flywoo GOKU GN745 flight controller.

Unlike Betaflight, ArduPilot provides autonomous flight modes such as Altitude Hold, Position Hold and mission-based navigation, which are required for our project.

However, the default ArduPilot configuration is mainly intended for larger drones. Because our drone is a **3.5-inch ducted FPV platform**, several parameters had to be adapted before stable flight could be achieved.

This chapter describes all important configuration steps that were performed on the flight controller.

---

# Hardware

| Component | Description |
|-----------|-------------|
| Flight Controller | Flywoo GOKU GN745 |
| Firmware | ArduPilot Copter 4.6.x |
| ESC | Integrated AM32 ESC |
| Frame | Flywoo FlyLens 85 HD |

---

# Installing ArduPilot

The first step consisted of installing ArduPilot on the Flywoo GN745 flight controller.

After flashing the firmware, the drone was connected to Mission Planner for the initial setup.

The following configuration tasks were then completed:

- accelerometer calibration
- compass calibration
- radio calibration
- ESC configuration
- frame configuration
- motor verification

After the initial setup the drone was able to arm successfully.

---

# Motor Configuration

The original ESC configuration was adapted to use the DShot600 protocol.

The following parameters were configured.

| Parameter | Value | Description |
|-----------|------:|-------------|
| MOT_PWM_TYPE | 6 | DShot600 protocol |
| MOT_SPIN_ARM | 0.03 | Motor idle speed while armed |
| MOT_SPIN_MIN | 0.06 | Minimum motor speed during flight |

These settings improve motor response and provide more reliable communication between the flight controller and the ESCs. :contentReference[oaicite:1]{index=1}

---

# Initial Flight Behaviour

During the first hover tests, the drone showed unstable behaviour.

The default ArduPilot filter configuration is designed for larger multicopters and therefore generated oscillations on the small FPV frame.

To improve flight stability, several filter parameters were adjusted.

---

# IMU Filter Configuration

The gyroscope and accelerometer filters were modified according to the project configuration.

| Parameter | Final Value |
|-----------|------------:|
| INS_GYRO_FILTER | 80 |
| INS_ACCEL_FILTER | 20 |

These values reduced sensor noise while maintaining a fast controller response.

---

# Rate Controller Filters

Additional rate controller filters were configured for the roll and pitch axes.

| Parameter | Value |
|-----------|------:|
| ATC_RAT_PIT_FLTD | 40 |
| ATC_RAT_PIT_FLTT | 40 |
| ATC_RAT_RLL_FLTD | 40 |
| ATC_RAT_RLL_FLTT | 40 |

These settings reduced high-frequency oscillations during hover.

---

# Dynamic Harmonic Notch Filter

Because the drone uses high-speed brushless motors, a Dynamic Harmonic Notch Filter was enabled.

The filter suppresses motor vibration before it reaches the PID controller.

The following configuration was applied.

| Parameter | Value |
|-----------|------:|
| INS_HNTCH_ENABLE | 1 |
| INS_HNTCH_MODE | 3 |
| INS_HNTCH_REF | 1.0 |
| INS_HNTCH_FREQ | 80 |
| INS_HNTCH_BW | 40 |
| INS_HNTCH_ATT | 40 |

This configuration uses ESC telemetry to automatically adapt the notch filter frequency during flight. :contentReference[oaicite:2]{index=2}

---

# PID Configuration

Before performing flight tests, the default PID values were reduced to create a safe and stable starting point.

## Pitch Controller

| Parameter | Value |
|-----------|------:|
| ATC_RAT_PIT_P | 0.06 |
| ATC_RAT_PIT_I | 0.06 |
| ATC_RAT_PIT_D | 0.002 |

## Roll Controller

| Parameter | Value |
|-----------|------:|
| ATC_RAT_RLL_P | 0.06 |
| ATC_RAT_RLL_I | 0.06 |
| ATC_RAT_RLL_D | 0.002 |

## Yaw Controller

| Parameter | Value |
|-----------|------:|
| ATC_RAT_YAW_P | 0.18 |
| ATC_RAT_YAW_I | 0.018 |
| ATC_RAT_YAW_D | 0 |

These values correspond to the exported project configuration and were used during the flight tests.

---

# Flight Controller Orientation

The Flywoo GN745 could not be mounted in the standard orientation because of the limited space inside the frame.

The flight controller was therefore installed with a rotated orientation.

To compensate for this, a custom board orientation was configured in Mission Planner.

| Parameter | Value |
|-----------|------:|
| AHRS_ORIENTATION | 101 (Custom 1) |
| CUST_ROT1_ROLL | 180 |
| CUST_ROT1_PITCH | 0 |
| CUST_ROT1_YAW | 225 |

Without this correction, the drone interpreted its orientation incorrectly and stable flight was not possible. :contentReference[oaicite:3]{index=3}

---

# Calibration

After all configuration changes, the following calibration procedures were completed.

- Accelerometer calibration
- Compass calibration
- Radio calibration
- ESC verification
- Motor direction verification

These steps ensured that all onboard sensors provided reliable measurements.

---

# Configuration Verification

After applying all parameters, the complete ArduPilot configuration was exported and stored as a parameter file.

This export represents the final flight controller configuration used during the project and served as the basis for all subsequent development stages, including LiDAR integration, Position Hold and Raspberry Pi communication.

---

# Challenges

Several problems occurred during the configuration process.

## Flight Oscillations

The default ArduPilot parameters caused noticeable oscillations during the first flights.

The issue was resolved by adjusting:

- PID values
- IMU filters
- Dynamic Harmonic Notch Filter

---

## Board Orientation

Because the flight controller was mounted at an angle, the measured orientation did not correspond to the physical orientation of the drone.

This issue was solved by configuring a custom board rotation.

---

## Stable Hover

Several hover tests were required before the drone could maintain a stable attitude.

Each test resulted in small parameter adjustments until satisfactory flight behaviour was achieved.

---

# Results

At the end of this configuration phase, the following objectives had been achieved.

✔ ArduPilot successfully installed

✔ ESC configured for DShot600

✔ Motor parameters optimized

✔ IMU filters configured

✔ Dynamic Harmonic Notch Filter enabled

✔ PID values tuned for the project platform

✔ Flight controller orientation corrected

✔ Stable hover achieved

The configured flight controller provided the foundation for the next project phases, including LiDAR integration, Position Hold, Raspberry Pi integration and the delivery mechanism.
