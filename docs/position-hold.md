# Position Hold

## Overview

Position Hold (PosHold) was developed after the initial ArduPilot configuration and the Altitude Hold work.

The objective is to improve the ability of the drone to maintain its horizontal position during flight.

Position Hold depends on stable flight behaviour and reliable sensor information.

---

# 1. Prerequisites

The following work was performed before or during Position Hold preparation:

- ArduPilot installation,
- Flight Controller replacement,
- board orientation,
- motor configuration,
- accelerometer calibration,
- compass calibration,
- PID adjustment,
- filter configuration,
- vibration reduction,
- LiDAR installation,
- LiDAR calibration,
- Altitude Hold development.

---

# 2. Flight Stability

Stable flight behaviour was an important prerequisite.

The documented configuration includes:

| Parameter | Value |
|-----------|------:|
| `INS_GYRO_FILTER` | 80 |
| `INS_ACCEL_FILTER` | 20 |
| `INS_HNTCH_ENABLE` | 1 |
| `INS_HNTCH_MODE` | 3 |
| `INS_HNTCH_FREQ` | 80 |
| `INS_HNTCH_BW` | 40 |
| `INS_HNTCH_ATT` | 40 |

Initial Roll and Pitch PID values were also reduced.

---

# 3. PID Values

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

These values are part of the current documented flight-test configuration.

---

# 4. Altitude Information

Position Hold development is connected to the Altitude Hold work.

The internal barometer was tested first but did not provide satisfactory results for the intended AltHold operation.

The LiDAR was then installed and calibrated.

Current Range Finder values include:

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

# 5. Optical Flow

Optical Flow is intended to provide information about horizontal movement and support Position Hold.

However, the current documentation does not contain a complete, verified list of Optical Flow parameter changes.

Therefore, no additional Optical Flow parameters are listed here without evidence from the exported drone parameters or a documented test.

---

# 6. Vibration Reduction

Vibration reduction included:

### Software

- gyro filtering,
- accelerometer filtering,
- Dynamic Harmonic Notch Filter,
- PID adjustment.

### Mechanical

- damping material,
- modified landing feet,
- improved mechanical mounting.

---

# 7. Calibration

The documented calibration work includes:

- accelerometer,
- compass,
- LiDAR,
- configuration checks after hardware changes.

---

# 8. Flight Testing

The development tests focused on:

- general flight stability,
- hover behaviour,
- vibration,
- altitude behaviour,
- sensor behaviour.

---

# 9. Development Sequence

```text
Flight Controller Configuration
            ↓
Flight Stability
            ↓
Vibration Reduction
            ↓
LiDAR Installation and Calibration
            ↓
Altitude Hold Development
            ↓
Position Hold Development
```

---

# 10. Current Status

The current project documentation describes Position Hold as still being part of the development and testing process.

The preparation work has been performed, but the available documentation does not contain enough evidence to mark the complete Position Hold implementation as finished.

Therefore, this file should only be changed to **completed** after a final documented Position Hold test.

---

# 11. Next Steps

- final Position Hold flight test,
- verify horizontal position stability,
- verify Optical Flow behaviour,
- record final parameters,
- document final test results.
