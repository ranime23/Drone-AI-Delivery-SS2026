# Autopilot Configuration

# Overview

One of the first tasks of our project was replacing the original Betaflight firmware with **ArduPilot Copter 4.6.x** on the Flywoo GOKU GN745 flight controller.

ArduPilot was selected because it provides flight modes such as Altitude Hold, Position Hold and sensor integration, which are required for the future development of our drone.

Since our platform is a small 3.5-inch ducted FPV drone, the default ArduPilot parameters were not suitable. Therefore, several configuration changes were necessary before starting the first flight tests.

This chapter documents the configuration work completed so far.

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

The first step was installing ArduPilot on the Flywoo GN745 flight controller.

After successfully flashing the firmware, the drone was connected to Mission Planner to perform the initial configuration.

The following tasks were completed:

- Accelerometer calibration
- Compass calibration
- Radio calibration
- ESC configuration
- Motor verification

After the installation, the drone was able to communicate correctly with Mission Planner.

---

# ESC and Motor Configuration

The ESCs were configured to use the DShot600 communication protocol.

The following parameters were applied.

| Parameter | Value |
|-----------|------:|
| MOT_PWM_TYPE | 6 |
| MOT_SPIN_ARM | 0.03 |
| MOT_SPIN_MIN | 0.06 |

These settings improve the communication between the flight controller and the ESCs and provide a more reliable motor response. :contentReference[oaicite:1]{index=1}

---

# IMU Filter Configuration

During the first hover attempts, unstable behaviour was observed.

To reduce vibrations and sensor noise, the IMU filter parameters were modified.

| Parameter | Value |
|-----------|------:|
| INS_GYRO_FILTER | 80 |
| INS_ACCEL_FILTER | 20 |

---

# Rate Controller Filters

Additional filter values were configured for the roll and pitch controllers.

| Parameter | Value |
|-----------|------:|
| ATC_RAT_PIT_FLTD | 40 |
| ATC_RAT_PIT_FLTT | 40 |
| ATC_RAT_RLL_FLTD | 40 |
| ATC_RAT_RLL_FLTT | 40 |

These parameters were introduced as a starting point for improving flight stability.

---

# Dynamic Harmonic Notch Filter

To reduce motor vibrations, the Dynamic Harmonic Notch Filter was enabled.

The current configuration is shown below.

| Parameter | Value |
|-----------|------:|
| INS_HNTCH_ENABLE | 1 |
| INS_HNTCH_MODE | 3 |
| INS_HNTCH_REF | 1.0 |
| INS_HNTCH_FREQ | 80 |
| INS_HNTCH_BW | 40 |
| INS_HNTCH_ATT | 40 |

The filter uses ESC telemetry to suppress motor noise before it affects the flight controller. :contentReference[oaicite:2]{index=2}

---

# PID Configuration

Before continuing the flight tests, the PID controller values were reduced to obtain a safer initial configuration.

## Pitch

| Parameter | Value |
|-----------|------:|
| ATC_RAT_PIT_P | 0.06 |
| ATC_RAT_PIT_I | 0.06 |
| ATC_RAT_PIT_D | 0.002 |

## Roll

| Parameter | Value |
|-----------|------:|
| ATC_RAT_RLL_P | 0.06 |
| ATC_RAT_RLL_I | 0.06 |
| ATC_RAT_RLL_D | 0.002 |

The PID values are still being evaluated during ongoing flight tests.

---

# Flight Controller Orientation

Because of the limited space inside the frame, the flight controller could not be installed in its standard orientation.

Mission Planner was therefore configured to use a custom board orientation.

| Parameter | Value |
|-----------|------:|
| AHRS_ORIENTATION | 101 |
| CUST_ROT1_ROLL | 180 |
| CUST_ROT1_PITCH | 0 |
| CUST_ROT1_YAW | 225 |

This configuration ensures that the software correctly interprets the physical orientation of the flight controller. :contentReference[oaicite:3]{index=3}

---

# Current Configuration Status

At the current stage of the project, the following work has been completed:

- ArduPilot successfully installed
- Flight controller connected to Mission Planner
- ESC configuration updated
- Motor communication configured using DShot600
- IMU filters configured
- Dynamic Harmonic Notch Filter enabled
- Initial PID values adjusted
- Board orientation corrected
- Sensor calibration completed

The complete parameter configuration has been exported and saved for future development.

---

# Flight Testing

After applying the initial configuration, several flight tests were carried out.

The objective of these tests was to:

- verify motor behaviour,
- evaluate the initial PID configuration,
- observe drone stability,
- identify vibrations,
- prepare the next tuning steps.

The parameter values are continuously reviewed after each test flight.

---

# Current Challenges

Although the basic autopilot configuration has been completed, several tasks are still in progress.

Current work includes:

- further PID tuning,
- improving flight stability,
- validating the LiDAR integration,
- testing Position Hold,
- integrating the Raspberry Pi into the complete system.

These tasks will be documented in the following chapters.

---

# Summary

The current autopilot configuration provides the foundation for the remaining project work.

Most of the basic ArduPilot configuration has been completed successfully. However, parameter tuning and flight optimisation are still ongoing as additional hardware components are integrated into the drone.
