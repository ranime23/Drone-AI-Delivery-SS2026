# Test Results

## 1. Overview

This document summarizes the main tests performed during the project.

## 2. Flight Controller

| Test | Result |
|---|---|
| ArduPilot installation | Successful |
| Mission Planner connection | Successful |
| Board identification | Successful |
| Motor configuration | Tested |
| DShot600 | Configured |
| Sensor calibration | Performed |
| Filter configuration | Performed |
| PID tuning | Performed |

## 3. Sensors

| Test | Result |
|---|---|
| Internal barometer | Tested |
| LiDAR installation | Successful |
| LiDAR calibration | Successful |
| Altitude Hold | Successfully tested |
| Optical Flow | Integrated and calibrated |
| Position Hold | Successfully tested |
| Vibration reduction | Implemented |

## 4. Raspberry Pi / MAVLink

The MAVProxy connection produced:

```text
Detected vehicle 1:1
AP: ArduCopter V4.6.3
AP: FlywooF745
AP: Frame: QUAD/X
Received 1180 parameters
Flight battery 90 percent
```

Result:

**MAVLink communication between Raspberry Pi and Flight Controller successfully tested.**

## 5. Motor control

A motor test was successfully triggered through MAVProxy.

Result:

**Motor command path successfully verified.**

## 6. Servo

The Miuzei MS18 servo was tested using GPIO 18.

A 90° release movement was successfully demonstrated.

The PWM signal can be detached after the movement to reduce servo jitter.

Result:

**Servo movement successfully tested.**

## 7. Camera / ArUco

A separate camera test successfully established a camera pipeline using `libcamerasrc`.

ArUco detection using:

```text
DICT_4X4_50
```

was implemented.

Result:

**Camera and ArUco test setup available.**

## 8. AI

MobileNet-SSD was selected for object detection.

Target configuration:

```text
TARGET_CLASS = "bottle"
CONFIDENCE_THRESHOLD = 0.5
```

The integrated AI/camera pipeline still requires the final hardware-specific camera setup to be validated on the complete drone.

## 9. Planned integrated mission

```text
1. TAKEOFF
2. AUTO SEARCH ROUTE
3. MobileNet-SSD detection
4. BRAKE / stabilize
5. ArUco verification
6. Servo release
7. RTL
8. Return to launch position
```

## 10. Final assessment

The project successfully established and tested the main building blocks:

- autonomous flight control foundation,
- Altitude Hold,
- Position Hold,
- LiDAR,
- Optical Flow,
- Raspberry Pi MAVLink communication,
- Mission Planner communication,
- motor command,
- servo release mechanism,
- camera/ArUco test setup,
- MobileNet-SSD based detection architecture.

The complete end-to-end autonomous delivery sequence should be marked as **demonstrated only after the integrated final flight test has been successfully completed**.
