# AI FPV Drone Delivery System

## Project Overview

This repository contains the documentation of our university project **AI FPV Drone Delivery System**.

The objective of the project was to transform a commercial FPV drone into an experimental platform capable of autonomous flight and prepared for future AI-assisted package delivery.

During the project, we focused on integrating ArduPilot, configuring the flight controller, improving the flight stability, integrating additional sensors such as LiDAR and Optical Flow, developing custom 3D-printed components, and preparing a Raspberry Pi for future onboard processing.

The repository documents every important development step, including the hardware modifications, software configuration, parameter tuning, flight tests and the problems encountered during the implementation.

---

# Project Objectives

The main objectives of our project were:

- Replace the original Betaflight firmware with ArduPilot.
- Configure the Flywoo GOKU GN745 flight controller.
- Improve flight stability by tuning ArduPilot parameters.
- Integrate a LiDAR sensor for altitude measurements.
- Integrate an Optical Flow sensor for indoor positioning.
- Design and manufacture custom 3D printed drone components.
- Prepare a Raspberry Pi Zero 2 W for future onboard processing.
- Develop a mechanical payload delivery mechanism.
- Test all implemented components individually.

---

# Hardware

The drone consists of the following main components.

| Component | Description |
|------------|-------------|
| Frame | Flywoo FlyLens 85 HD |
| Flight Controller | Flywoo GOKU GN745 |
| Firmware | ArduPilot Copter 4.6.x |
| ESC | Integrated AM32 ESC |
| GPS | GPS module |
| LiDAR | Distance sensor for altitude measurement |
| Optical Flow | Position estimation sensor |
| Raspberry Pi | Raspberry Pi Zero 2 W |
| Camera | Raspberry Pi AI Camera |
| Delivery Mechanism | Custom designed servo release system |

---

# Software

The following software was used during the project.

- ArduPilot
- Mission Planner
- Raspberry Pi OS
- MAVProxy
- MAVSDK
- DroneKit
- OpenCV
- Python
- Fusion 360
- Orca Slicer

---

# Project Documentation

The documentation is divided into several sections.

| Documentation | Description |
|---------------|-------------|
| Autopilot | Flight controller installation and configuration |
| Altitude Hold | LiDAR integration and altitude stabilization |
| Position Hold | Optical Flow integration and position estimation |
| LiDAR & Optical Flow | Sensor configuration and testing |
| Frame Design | Design and manufacturing of custom drone parts |
| Delivery System | Development of the payload release mechanism |
| Raspberry Pi | Raspberry Pi configuration and software installation |
| Test Results | Summary of all performed flight tests |

---

# Development Process

The project was completed in several stages.

## 1. Flight Controller Configuration

The first step was replacing the original firmware with ArduPilot and configuring the flight controller for the Flywoo platform.

This included:

- motor configuration
- ESC configuration
- board orientation correction
- accelerometer calibration
- parameter tuning

---

## 2. Flight Stabilization

After the first successful flights, several ArduPilot parameters were modified to improve flight stability.

The configuration included:

- PID tuning
- Gyroscope filtering
- Accelerometer filtering
- Dynamic Harmonic Notch Filter
- Motor configuration

The final parameter configuration is documented in the **Autopilot** section.

---

## 3. Sensor Integration

After achieving a stable flight behaviour, additional sensors were integrated.

These included:

- LiDAR
- Optical Flow
- GPS

Each sensor was configured individually and tested using Mission Planner.

---

## 4. Mechanical Design

Several drone components were designed specifically for this project.

These include:

- Raspberry Pi holder
- Camera holder
- Landing gear
- Protective frame
- Delivery mechanism

All parts were designed in CAD software and manufactured using 3D printing.

---

## 5. Raspberry Pi

The Raspberry Pi Zero 2 W was prepared as the onboard computer.

The performed work includes:

- Raspberry Pi OS installation
- OpenCV installation
- MAVSDK installation
- DroneKit installation
- Wireless Access Point configuration
- SSH configuration
- Network testing

---

## 6. Flight Testing

Multiple flight tests were carried out after each major hardware or software modification.

The tests focused on:

- Stable hover
- Altitude Hold
- Position Hold
- LiDAR performance
- Optical Flow performance
- Overall flight stability

The results of these tests are documented in the corresponding chapters.

---

# Current Project Status

At the current stage of the project, the following tasks have been completed.

✔ ArduPilot installed

✔ Flight controller configured

✔ Board orientation corrected

✔ ESC configured

✔ Motor parameters tuned

✔ Flight stabilization improved

✔ LiDAR integrated

✔ Optical Flow integrated

✔ Raspberry Pi configured

✔ Custom 3D printed parts manufactured

✔ Mechanical delivery mechanism developed

✔ Multiple flight tests completed

Some software components, especially the interaction between the Raspberry Pi and the flight controller, are still under further development.

---

# Repository Structure

```
README.md

docs/
│
├── autopilot.md
├── altitude-hold.md
├── position-hold.md
├── lidar-optical-flow.md
├── frame-design.md
├── delivery-system.md
├── raspberry-pi.md
└── test-results.md
```

---

# Conclusion

This repository documents the complete development process of our AI FPV Drone Delivery System.

Instead of presenting only the final result, the documentation describes the hardware modifications, software configuration, parameter tuning, sensor integration, mechanical development and flight testing that were carried out during the project.

Each chapter focuses on one part of the development process and documents the work performed by our project group.
