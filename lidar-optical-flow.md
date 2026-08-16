# LiDAR and Optical Flow

## Overview

LiDAR and Optical Flow are part of the sensor-integration work.

The LiDAR was installed and calibrated to provide distance measurements between the drone and the ground.

Optical Flow is intended to support horizontal movement estimation for Position Hold.

---

# 1. LiDAR Integration

The LiDAR sensor was mounted on the drone and connected to the Flight Controller.

The sensor was positioned to measure the distance between the drone and the ground.

After installation, the Range Finder configuration was entered in Mission Planner.

---

# 2. LiDAR Calibration

The LiDAR was calibrated after installation.

The calibration and testing process considered:

- sensor orientation,
- mounting position,
- vibration,
- mechanical stability.

Several checks were required during development.

---

# 3. Range Finder Configuration

| Parameter | Value |
|-----------|------:|
| `RNGFND1_MAX_CM` | 700 |
| `RNGFND1_MIN_CM` | 20 |
| `RNGFND1_GNDCLEAR` | 10 |
| `RNGFND1_ORIENT` | 25 |
| `RNGFND1_POS_X` | 0.05 |
| `RNGFND1_POS_Z` | 0.01 |
| `EK3_RNG_USE_HGT` | -1 |

---

# 4. Measurement Limits

```text
RNGFND1_MIN_CM = 20
RNGFND1_MAX_CM = 700
```

Configured measurement range:

**20 cm – 700 cm**

---

# 5. Sensor Orientation and Position

```text
RNGFND1_ORIENT = 25

RNGFND1_POS_X = 0.05
RNGFND1_POS_Z = 0.01
```

These are the values documented for the current configuration.

---

# 6. Vibration Problems

Vibration was an important problem during sensor integration.

Excessive vibration could affect both flight stability and the mechanical attachment of the LiDAR.

The group therefore used:

- software filtering,
- PID adjustments,
- Dynamic Harmonic Notch filtering,
- mechanical damping.

---

# 7. Landing Gear and Sensor Stability

The first landing-gear version included damping material.

A second, longer version was later developed because more space was required for the servo.

Damping material was also retained in Version 2.

This was important for the LiDAR mounting as well as for general vibration reduction.

---

# 8. Optical Flow

Optical Flow is intended to support horizontal movement estimation and Position Hold.

The current project documentation does not provide a complete verified list of Optical Flow parameter changes.

Therefore, this document does not invent or assume additional parameter values.

The detailed Position Hold development is documented in:

```text
position-hold.md
```

---

# 9. Current Status

LiDAR installation, calibration and basic Range Finder configuration have been documented as completed.

Optical Flow is part of the Position Hold development, but the available documentation does not justify marking the complete Optical Flow integration as finished.

Further sensor validation may therefore be required.
