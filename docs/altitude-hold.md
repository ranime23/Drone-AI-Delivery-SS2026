# Altitude Hold

## Overview

Altitude Hold (AltHold) was developed after the initial ArduPilot configuration.

The objective was to allow the drone to maintain its altitude with reduced manual throttle correction.

Two altitude-measurement approaches were investigated:

1. the internal Flight Controller barometer,
2. the external LiDAR sensor.

---

# 1. Objective

The work focused on:

- testing Altitude Hold,
- evaluating the internal barometer,
- installing the LiDAR,
- configuring the Range Finder,
- calibrating the sensor,
- reducing vibration effects,
- performing flight tests,
- improving flight stability.

---

# 2. Internal Barometer Test

The internal barometer of the Flight Controller was tested as an altitude source for Altitude Hold.

The test did not provide satisfactory results for the intended AltHold operation.

Therefore, the project continued with the LiDAR sensor.

---

# 3. LiDAR Installation

The LiDAR was mounted underneath the drone.

The sensor was connected to the Flight Controller and configured through Mission Planner.

The sensor was subsequently calibrated and tested.

The mechanical mounting became important because vibrations could affect the sensor attachment.

---

# 4. Range Finder Configuration

The documented current configuration contains:

| Parameter | Value | Function |
|-----------|------:|----------|
| `RNGFND1_MAX_CM` | 700 | Maximum measurement distance |
| `RNGFND1_MIN_CM` | 20 | Minimum measurement distance |
| `RNGFND1_GNDCLEAR` | 10 | Ground clearance |
| `RNGFND1_ORIENT` | 25 | Sensor orientation |
| `RNGFND1_POS_X` | 0.05 | Sensor X offset |
| `RNGFND1_POS_Z` | 0.01 | Sensor Z offset |
| `EK3_RNG_USE_HGT` | -1 | Current EKF rangefinder height setting |

---

# 5. Measurement Range

The configured range is:

```text
Minimum = 20 cm
Maximum = 700 cm
```

The corresponding parameters are:

```text
RNGFND1_MIN_CM = 20
RNGFND1_MAX_CM = 700
```

---

# 6. Ground Clearance

```text
RNGFND1_GNDCLEAR = 10
```

This value is part of the current Range Finder configuration.

---

# 7. Sensor Position

The documented sensor offsets are:

```text
RNGFND1_POS_X = 0.05
RNGFND1_POS_Z = 0.01
```

These values describe the configured position of the sensor relative to the Flight Controller reference.

---

# 8. Sensor Orientation

The documented orientation value is:

```text
RNGFND1_ORIENT = 25
```

This corresponds to the orientation configured for the LiDAR.

---

# 9. Calibration and Testing

The documented work included:

1. mounting the LiDAR,
2. connecting the sensor,
3. configuring the Range Finder,
4. calibrating the sensor,
5. checking distance measurements,
6. performing flight tests,
7. observing AltHold behaviour,
8. investigating vibration problems,
9. modifying mechanical damping where necessary.

---

# 10. Vibration Problems

Vibration was an important problem during Altitude Hold development.

The drone needed to fly as calmly as possible for reliable sensor measurements.

The LiDAR mounting could also be affected by vibration.

For this reason, damping material was introduced into the landing gear and the mechanical design was modified.

---

# 11. Relation to Flight Controller Tuning

Altitude Hold testing was performed together with the ArduPilot tuning work.

Relevant configuration included:

- PID adjustment,
- gyro filtering,
- accelerometer filtering,
- Dynamic Harmonic Notch Filter,
- mechanical vibration damping,
- LiDAR calibration.

The detailed parameters are documented in `autopilot.md`.

---

# 12. Current Status

The LiDAR has been installed and calibrated, and the Range Finder configuration has been entered in Mission Planner.

The internal barometer was tested but did not provide satisfactory results for the intended AltHold operation.

According to the current test documentation, Altitude Hold remains part of the ongoing tuning and flight-test process.

Therefore, this file should only be changed to **completed** if the group has a final documented test showing that the required AltHold behaviour was successfully achieved.

---

# 13. Next Steps

- final AltHold validation,
- additional flight tests,
- further vibration reduction if required,
- final parameter verification.
