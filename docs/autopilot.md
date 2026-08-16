# Autopilot Configuration

## Overview

One of the first major tasks of the project was replacing the original flight-control setup with **ArduPilot Copter 4.6.x** on the Flywoo GOKU GN745 flight controller.

ArduPilot was selected because it provides the flight-control and sensor-integration functions required for the project.

Because the drone is a small FPV platform, several configuration changes were required before and during the flight tests.

---

# 1. Hardware

| Component | Description |
|-----------|-------------|
| Flight Controller | Flywoo GOKU GN745 |
| Firmware | ArduPilot Copter 4.6.x |
| ESC | Integrated AM32 ESC |
| Frame | Flywoo FlyLens 85 HD |
| Receiver | ELRS |

---

# 2. ArduPilot Installation

ArduPilot was installed on the Flywoo GN745 flight controller.

After flashing the firmware, the drone was connected to Mission Planner.

The initial configuration included:

- accelerometer calibration,
- compass calibration,
- radio calibration,
- ESC configuration,
- motor verification.

The connection with Mission Planner was successfully established.

---

# 3. Flight Controller Replacement

The original flight controller was completely replaced by the:

**Flywoo GOKU GN745**

After the replacement, the Flight Controller had to be configured and calibrated again.

The replacement was one of the major hardware changes documented during the project.

---

# 4. Board Orientation

Because of the physical mounting position of the Flight Controller, a custom orientation was configured.

The current documented values are:

| Parameter | Value |
|-----------|------:|
| `AHRS_ORIENTATION` | 101 |
| `CUST_ROT1_ROLL` | 180 |
| `CUST_ROT1_PITCH` | 0 |
| `CUST_ROT1_YAW` | 225 |

This configuration allows ArduPilot to interpret the physical orientation of the Flight Controller correctly.

---

# 5. Accelerometer Calibration

A complete accelerometer calibration was performed.

Calibration was particularly important after the Flight Controller replacement.

Several calibration and verification steps were required during the project.

---

# 6. Motor and ESC Configuration

The ESCs were configured to use DShot600.

| Parameter | Value |
|-----------|------:|
| `MOT_PWM_TYPE` | 6 |
| `MOT_SPIN_ARM` | 0.03 |
| `MOT_SPIN_MIN` | 0.06 |

The motor order was adapted for the ArduPilot configuration and checked during testing.

---

# 7. IMU Filters

The gyro and accelerometer filters were adjusted as part of the flight-stability work.

| Parameter | Value |
|-----------|------:|
| `INS_GYRO_FILTER` | 80 |
| `INS_ACCEL_FILTER` | 20 |

These settings were used to reduce the influence of high-frequency noise and vibration on the flight-control system.

---

# 8. Rate Controller Filters

The following additional filter values are documented in the current configuration:

| Parameter | Value |
|-----------|------:|
| `ATC_RAT_PIT_FLTD` | 40 |
| `ATC_RAT_PIT_FLTT` | 40 |
| `ATC_RAT_RLL_FLTD` | 40 |
| `ATC_RAT_RLL_FLTT` | 40 |

---

# 9. Dynamic Harmonic Notch Filter

The Dynamic Harmonic Notch Filter was enabled as part of the vibration-reduction work.

| Parameter | Value |
|-----------|------:|
| `INS_HNTCH_ENABLE` | 1 |
| `INS_HNTCH_MODE` | 3 |
| `INS_HNTCH_REF` | 1.0 |
| `INS_HNTCH_FREQ` | 80 |
| `INS_HNTCH_BW` | 40 |
| `INS_HNTCH_ATT` | 40 |

The documented configuration uses ESC telemetry mode.

---

# 10. PID Configuration

The initial Roll and Pitch PID values were reduced during the flight-stability tuning.

## Pitch

```text
ATC_RAT_PIT_P = 0.06
ATC_RAT_PIT_I = 0.06
ATC_RAT_PIT_D = 0.002
```

## Roll

```text
ATC_RAT_RLL_P = 0.06
ATC_RAT_RLL_I = 0.06
ATC_RAT_RLL_D = 0.002
```

These values were part of the current test configuration. Further optimisation may still be required.

---

# 11. GPS Replacement

The original GPS module was completely replaced.

The replacement required the corresponding configuration and calibration to be checked again.

---

# 12. Compass and Sensor Calibration

A considerable amount of calibration work was required.

The documented calibration work includes:

- accelerometer calibration,
- compass calibration,
- LiDAR calibration,
- configuration checks after hardware replacement.

Repeated calibration was necessary during the development process.

---

# 13. Barometer

The internal barometer of the Flight Controller was tested for Altitude Hold.

The test did not provide satisfactory results for the intended AltHold operation.

The project therefore continued with the external LiDAR integration.

---

# 14. Vibration and Flight Stability

Vibration was one of the recurring problems during development.

The group addressed it through both software and mechanical measures.

### Software

- gyro filtering,
- accelerometer filtering,
- Dynamic Harmonic Notch Filter,
- PID adjustments.

### Mechanical

- damping material,
- modified landing feet,
- improved sensor mounting.

The objective was to obtain a sufficiently calm flight behaviour for the Altitude Hold and Position Hold development.

---

# 15. Parameter Export

The complete parameter configuration was exported from Mission Planner.

The exported file should be stored in the repository as:

```text
drone-parameters.param
```

This file is the authoritative record of the exported drone configuration.

The values manually listed in this document are only the parameters that are currently documented as relevant to the project work.

---

# 16. Current Status

The following work is documented as completed:

- ArduPilot installation,
- Mission Planner connection,
- Flight Controller replacement,
- board orientation,
- motor/ESC configuration,
- DShot600,
- sensor calibration,
- filter configuration,
- Dynamic Harmonic Notch Filter,
- initial PID adjustments.

Further tuning and validation remain connected to the flight tests, Altitude Hold, Position Hold and sensor integration.
