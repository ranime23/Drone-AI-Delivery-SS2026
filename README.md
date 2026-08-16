# AI FPV Drone Delivery System

## Project Overview

This repository contains the documentation of our university project **AI FPV Drone Delivery System**.

The objective of the project was to transform a commercial FPV drone into an experimental platform for stable automated flight and future AI-assisted package delivery.

During the project, the group focused on:

- replacing the original flight-control setup with ArduPilot,
- configuring the Flywoo GOKU GN745 flight controller,
- improving flight stability through parameter tuning,
- integrating LiDAR,
- preparing Optical Flow for Position Hold,
- developing custom 3D-printed components,
- preparing a Raspberry Pi Zero 2 W for onboard processing,
- testing the camera,
- preparing the mechanical delivery system.

The repository documents the hardware modifications, software configuration, parameter changes, calibration work, mechanical development, tests and problems encountered during the project.

> **Documentation status:** The documents below reflect only work that is supported by the current project documentation. Features that are still described as ongoing are not marked as completed.

---

# Project Objectives

The main objectives were:

- Replace the original flight-control firmware with ArduPilot.
- Configure the Flywoo GOKU GN745 flight controller.
- Improve flight stability by tuning ArduPilot parameters.
- Integrate a LiDAR sensor for distance/altitude information.
- Prepare and test the sensor configuration required for Position Hold.
- Design and manufacture custom 3D-printed drone components.
- Prepare a Raspberry Pi Zero 2 W for onboard processing.
- Test the Raspberry Pi camera.
- Prepare a mechanical payload delivery mechanism.
- Perform flight and hardware tests after important modifications.

---

# Hardware

| Component | Description |
|-----------|-------------|
| Frame | Flywoo FlyLens 85 HD |
| Flight Controller | Flywoo GOKU GN745 |
| Firmware | ArduPilot Copter 4.6.x |
| ESC | Integrated AM32 ESC |
| Receiver | ELRS |
| GPS | GPS module, replaced during the project |
| LiDAR | MicroAir MTF-01P |
| Optical Flow | Sensor intended for position estimation |
| Raspberry Pi | Raspberry Pi Zero 2 W |
| Camera | Raspberry Pi AI Camera |
| Delivery Mechanism | Servo-based mechanical release system |

---

# Software

The project used or prepared the following software:

- ArduPilot
- Mission Planner
- Raspberry Pi OS
- Python
- OpenCV
- pymavlink
- MAVProxy
- MAVSDK
- DroneKit
- libcamera
- Git
- Fusion 360
- Orca Slicer

---

# Project Documentation

| File | Description |
|------|-------------|
| `docs/autopilot.md` | Flight controller installation and configuration |
| `docs/altitude-hold.md` | Altitude Hold development and LiDAR |
| `docs/position-hold.md` | Position Hold preparation and testing |
| `docs/lidar-optical-flow.md` | LiDAR and Optical Flow |
| `docs/raspberry-pi.md` | Raspberry Pi environment and network |
| `docs/camera-test.md` | Raspberry Pi camera test |
| `docs/frame-design.md` | Mechanical and 3D-print development |
| `docs/delivery-system.md` | Servo and payload delivery preparation |
| `docs/test-results.md` | Test results and development progress |

---

# Development Process

## 1. Initial Flight Tests

At the beginning, all group members were given the opportunity to fly the drone in order to select the pilot for the following tests.

Several crashes occurred during the initial flight attempts. Some components were damaged and had to be repaired or replaced. Propellers were also replaced.

The selected pilot subsequently practiced with a simulator.

---

## 2. Hardware Replacement

Several hardware changes were required during development:

- Flight Controller completely replaced.
- GPS completely replaced.
- Video transmitter antenna replaced and later damaged again.
- Power cables re-soldered.
- Additional heat-shrink tubing added for protection.

The new Flight Controller was the Flywoo GOKU GN745.

---

## 3. ArduPilot Configuration

ArduPilot was installed on the new Flight Controller and connected successfully to Mission Planner.

The configuration included:

- board orientation,
- accelerometer calibration,
- compass calibration,
- motor configuration,
- DShot600,
- filter configuration,
- Dynamic Harmonic Notch Filter,
- PID adjustments.

The complete exported parameter file is kept separately as `drone-parameters.param`.

---

## 4. Sensor Integration

The project included work on:

- GPS,
- LiDAR,
- Optical Flow,
- accelerometer,
- gyroscope,
- compass,
- barometer.

The internal barometer was tested for Altitude Hold but did not provide satisfactory results for the intended operation.

The LiDAR was subsequently installed and calibrated.

---

## 5. Mechanical Development

Several 3D-printed components were developed and tested:

- Raspberry Pi mounting plate,
- camera case,
- landing feet Version 1,
- landing feet Version 2,
- larger cage prototype,
- additional mounting components.

The landing feet were redesigned because the servo required more space underneath the drone. Damping material was used in both versions to reduce vibration.

---

## 6. Raspberry Pi

The Raspberry Pi Zero 2 W environment was prepared.

The work included:

- operating-system preparation,
- dependency installation,
- OpenCV,
- pymavlink,
- MAVSDK,
- MAVProxy,
- DroneKit,
- libcamera,
- storage optimisation,
- SSH access,
- persistent Wi-Fi configuration,
- Access Point configuration.

The camera was also successfully tested for basic image capture and local file access.

Complete communication between the Raspberry Pi and the drone system remains a documented challenge.

---

# Current Project Status

According to the current documentation:

### Completed / implemented

- ArduPilot installed.
- Mission Planner connection established.
- Flywoo GOKU GN745 configured.
- Board orientation configured.
- Motor configuration and DShot600 configured.
- Accelerometer and compass calibration performed.
- Gyroscope and accelerometer filters adjusted.
- Dynamic Harmonic Notch Filter enabled.
- Initial PID values adjusted.
- GPS replaced.
- LiDAR installed and calibrated.
- 3D-printed mechanical components developed.
- Landing gear Version 1 and Version 2 produced.
- Camera case produced.
- Raspberry Pi software environment prepared.
- Raspberry Pi network configuration prepared.
- Raspberry Pi camera basic image capture tested.

### Still documented as ongoing

- Further PID and flight optimisation.
- Final validation of Altitude Hold.
- Position Hold development/testing.
- Further vibration reduction.
- Complete Raspberry-Pi-to-drone communication.
- Full autonomous delivery sequence.
- Complete autonomous navigation.

These items should only be changed to **completed** when the group has actual final test evidence.

---

# Repository Structure

```text
AI-FPV-Drone-Delivery-System/
│
├── README.md
├── drone-parameters.param
│
├── docs/
│   ├── autopilot.md
│   ├── altitude-hold.md
│   ├── position-hold.md
│   ├── lidar-optical-flow.md
│   ├── raspberry-pi.md
│   ├── camera-test.md
│   ├── frame-design.md
│   ├── delivery-system.md
│   └── test-results.md
│
└── images/
```

---

# Conclusion

The project resulted in a significantly modified FPV drone platform with an ArduPilot-based flight-control system, additional sensors, custom mechanical components and a prepared Raspberry Pi environment.

The documentation intentionally distinguishes between implemented work and functions that are still under testing. This makes the repository suitable as a development record and avoids claiming functionality that has not yet been demonstrated by a documented test.
