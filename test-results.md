# Test Results and Development Progress

## Overview

Throughout the project, multiple tests were performed after hardware changes, software configuration changes and mechanical modifications.

The tests were not carried out only at the end of the project. Instead, testing was part of the complete development process.

After each important modification, the behaviour of the drone was evaluated and further adjustments were made when necessary.

This document summarizes the tests and observations documented so far.

---

# 1. Initial Flight Tests and Pilot Selection

At the beginning of the project, the group first had to determine who would operate the drone during the flight tests.

All group members were given the opportunity to fly the drone.

This process was used to select the pilot for the following test flights.

## Observations

During these first flight attempts, several crashes occurred.

As a result, some components were damaged and had to be repaired or replaced.

Propellers were also replaced during this phase.

## Consequence

The group identified pilot training as an important factor for reducing unnecessary crashes during future development.

The selected pilot therefore continued practicing using a simulator.

## Lesson Learned

For future projects, simulator training should be performed before the first real flight tests.

A recommended procedure would be:

```text
Simulator Training
        ↓
Basic Flight Practice
        ↓
Pilot Selection
        ↓
Additional Simulator Training
        ↓
Real Drone Testing
```

This would reduce the risk of damaging hardware during the early project stages.

---

# 2. Hardware Replacement

Several hardware components had to be replaced during the development process.

## Flight Controller

The original flight controller was completely replaced.

The drone was subsequently configured using the Flywoo GOKU GN745 flight controller.

After the replacement, ArduPilot had to be configured and the required calibration procedures had to be performed again.

---

## GPS

The GPS module was also completely replaced.

After replacement, the new hardware had to be integrated into the current drone configuration.

---

## Video Transmitter Antenna

The antenna of the video transmitter was replaced after hardware problems.

According to the project development log, the antenna later became damaged again.

This remained a hardware issue during the development process.

---

## Power Cables

The power cables were re-soldered.

Additional heat-shrink tubing was installed to improve the mechanical protection of the electrical connections.

---

# 3. ArduPilot Installation Test

ArduPilot was successfully installed on the flight controller.

After installation, communication with Mission Planner was established.

This allowed the group to continue with:

- sensor calibration,
- motor configuration,
- ESC configuration,
- filter configuration,
- PID adjustment,
- flight-mode testing.

---

# 4. Flight Controller Orientation Test

Because of the physical installation of the flight controller, a custom board orientation had to be configured.

The current configuration includes:

```text
AHRS_ORIENTATION = 101
CUST_ROT1_ROLL = 180
CUST_ROT1_PITCH = 0
CUST_ROT1_YAW = 225
```

The orientation configuration was required so that ArduPilot could correctly interpret the physical orientation of the flight controller.

---

# 5. Motor and ESC Configuration Test

The motor configuration was adapted for ArduPilot.

DShot600 was configured as the ESC protocol.

The current relevant parameters include:

```text
MOT_PWM_TYPE = 6
MOT_SPIN_ARM = 0.03
MOT_SPIN_MIN = 0.06
```

After configuration, motor behaviour was checked as part of the ongoing flight-controller testing.

---

# 6. Initial Flight Stability Tests

One of the main objectives during the flight tests was to make the drone fly as calmly as possible.

Stable flight behaviour was necessary before continuing with Altitude Hold and Position Hold testing.

During the initial tests, vibration and stability problems were observed.

The group therefore modified several flight-controller parameters.

---

# 7. PID Tests

Initial PID values were adjusted for Roll and Pitch.

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

These values formed part of the configuration used during the current flight tests.

PID tuning is still part of the ongoing optimisation process.

---

# 8. Filter Tests

The Gyroscope and Accelerometer filter settings were modified.

The current relevant values include:

```text
INS_GYRO_FILTER = 80
INS_ACCEL_FILTER = 20
```

A Dynamic Harmonic Notch Filter was also enabled.

```text
INS_HNTCH_ENABLE = 1
INS_HNTCH_MODE = 3
INS_HNTCH_FREQ = 80
INS_HNTCH_BW = 40
INS_HNTCH_ATT = 40
```

These modifications were introduced as part of the work to reduce vibration-related problems and improve flight behaviour.

---

# 9. Calibration Tests

A significant amount of calibration work was required during the project.

Calibration was especially important after hardware replacement or configuration changes.

The work included:

- Accelerometer calibration
- Compass calibration
- Flight-controller configuration checks
- LiDAR calibration

Several calibration steps had to be repeated during development.

---

# 10. Internal Barometer Test

The internal barometer of the flight controller was tested for use with Altitude Hold.

## Result

The test did not provide satisfactory results for the intended AltHold operation.

The project therefore continued with the integration of an external LiDAR sensor.

This test was important because it directly influenced the decision to use an additional altitude sensor.

---

# 11. LiDAR Test

The LiDAR sensor was installed on the drone and calibrated.

The current Range Finder configuration includes:

| Parameter | Value |
|-----------|------:|
| `RNGFND1_MAX_CM` | 700 |
| `RNGFND1_MIN_CM` | 20 |
| `RNGFND1_GNDCLEAR` | 10 |
| `RNGFND1_ORIENT` | 25 |
| `RNGFND1_POS_X` | 0.05 |
| `RNGFND1_POS_Z` | 0.01 |
| `EK3_RNG_USE_HGT` | -1 |

The LiDAR configuration and measurements were evaluated as part of the Altitude Hold development.

---

# 12. Altitude Hold Testing

Altitude Hold testing was carried out during the project.

The development included:

1. testing the internal barometer,
2. observing unsatisfactory barometer behaviour,
3. installing the LiDAR,
4. calibrating the LiDAR,
5. configuring the Range Finder,
6. improving flight stability,
7. reducing vibrations,
8. continuing flight tests.

Altitude Hold is still connected to the ongoing tuning and flight-stability work.

It is therefore not documented as completely finished at the current project stage.

---

# 13. Position Hold Preparation and Testing

Position Hold was the next important flight-control objective after working on Altitude Hold.

The project group first focused on obtaining a sufficiently stable flight behaviour.

The relevant preparation included:

- flight-controller tuning,
- PID adjustment,
- filter configuration,
- vibration reduction,
- LiDAR integration,
- sensor calibration.

Position Hold testing is still part of the current development process.

The available project documentation does not justify marking the complete Position Hold implementation as finished.

---

# 14. Vibration Tests

Vibration was one of the recurring problems during the project.

It affected both flight stability and the mechanical installation of additional sensors.

The group addressed vibration using two approaches.

## Software

The following settings were modified:

- Gyroscope filtering
- Accelerometer filtering
- Dynamic Harmonic Notch Filter
- PID values

## Mechanical

The landing feet were equipped with damping material.

The mechanical damping was also important because excessive vibrations could affect the LiDAR attachment.

---

# 15. Landing Gear Test – Version 1

The first version of the landing feet was 3D printed.

Foam/pool-noodle material was added as vibration damping.

## Observation

The damping concept was retained, but the available space underneath the drone was not sufficient for the servo integration.

A second version was therefore required.

---

# 16. Landing Gear Test – Version 2

The second version used longer landing feet.

The objective was to create more space underneath the drone for the servo.

Damping material was again included.

The second version therefore addressed two requirements:

```text
Additional Servo Clearance
          +
Vibration Damping
```

---

# 17. Larger Cage Test

A larger cage was tested during the mechanical development.

## Result

The tested configuration was not suitable for the required component arrangement.

One of the relevant problems was the additional space required for the servo.

The cage design was therefore not continued in the tested form.

---

# 18. Camera Case

A camera case was 3D printed and attached to the drone.

This provided a dedicated mounting solution for the camera during the ongoing mechanical integration.

---

# 19. Raspberry Pi Environment Tests

The Raspberry Pi Zero 2 W environment was also prepared and tested.

The following software components were installed:

- OpenCV
- pymavlink
- DroneKit
- MAVSDK
- MAVProxy
- NumPy
- libcamera

During installation, a storage problem occurred:

```text
OSError: [Errno 28] No space left on device
```

The root filesystem was expanded and package caches were cleaned before continuing the installation. :contentReference[oaicite:0]{index=0}

---

# 20. Raspberry Pi Network Test

A simultaneous Station + Access Point configuration was prepared.

A virtual interface called:

```text
uap0
```

was created.

A NetworkManager Access Point profile called:

```text
Himbeere_AP
```

was also configured.

The setup used:

- `iw`
- `systemd`
- `NetworkManager`
- `nmcli`

The documented Wi-Fi channel during configuration was channel 11 at 2462 MHz. :contentReference[oaicite:1]{index=1}

---

# 21. Raspberry Pi Communication Status

Although the Raspberry Pi environment and network configuration have progressed, communication with the Raspberry Pi remains one of the current project challenges.

Therefore, the complete Raspberry Pi integration is not considered finished.

---

# 22. Test Summary

| Test / Development Step | Current Observation |
|-------------------------|---------------------|
| ArduPilot installation | Installed |
| Mission Planner connection | Established |
| Flight Controller replacement | Performed |
| GPS replacement | Performed |
| Motor configuration | Configured and under flight testing |
| DShot600 | Configured |
| Board orientation | Configured |
| Accelerometer calibration | Performed |
| Compass calibration | Performed |
| PID adjustment | Performed, further tuning ongoing |
| Filter configuration | Performed |
| Internal barometer for AltHold | Tested, result not satisfactory |
| LiDAR installation | Performed |
| LiDAR calibration | Performed |
| Altitude Hold | Testing/optimisation ongoing |
| Position Hold | Development/testing ongoing |
| Vibration damping | Implemented and still evaluated |
| Landing feet V1 | Produced and tested |
| Landing feet V2 | Produced after additional requirements |
| Larger cage | Tested, not retained in tested form |
| Camera case | Printed and attached |
| Raspberry Pi software environment | Prepared |
| Raspberry Pi Access Point | Configured |
| Complete Raspberry Pi communication | Still problematic / ongoing |

---

# 23. Current Project Status

The project is still under development.

A significant amount of hardware integration, ArduPilot configuration, calibration, mechanical development and testing has already been carried out.

The main focus of the current work remains:

- improving flight stability,
- continuing Altitude Hold testing,
- continuing Position Hold development,
- reducing vibration problems,
- resolving Raspberry Pi communication problems,
- integrating the remaining system components.

This document will be updated as additional tests and configuration changes are performed.