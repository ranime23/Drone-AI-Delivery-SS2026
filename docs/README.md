# AI-Based FPV Drone Delivery System

## Project Overview

This project was developed as part of the Adaptive Knowledge Systems course.

The objective is to extend an FPV drone with autonomous flight capabilities and an AI-supported delivery mechanism. The system combines ArduPilot, LiDAR, Optical Flow, a Raspberry Pi Zero 2 WH and a Raspberry Pi AI Camera to enable autonomous indoor navigation and object delivery.

The project focuses on the integration of flight control, sensor fusion, embedded software and custom 3D-printed components.

---

## Project Objectives

The main objectives of the project are:

- Configure an FPV drone using ArduPilot
- Achieve stable autonomous flight
- Implement Altitude Hold using LiDAR
- Implement Position Hold without GPS
- Integrate a Raspberry Pi Zero 2 WH
- Connect a Raspberry Pi AI Camera
- Develop an AI-supported delivery system
- Design and manufacture custom 3D-printed components
- Document the complete development process

---

# Hardware

The drone consists of the following hardware components.

| Component | Purpose |
|-----------|----------|
| Flywoo GOKU GN745 Flight Controller | Flight control |
| ELRS Receiver | Remote control communication |
| GPS Module | Outdoor positioning |
| LiDAR (MTF-01P) | Altitude measurement |
| Optical Flow Sensor | Indoor position estimation |
| Raspberry Pi Zero 2 WH | Embedded computer |
| Raspberry Pi AI Camera | Object detection |
| Micro Servo | Delivery mechanism |
| FPV Camera & Video Transmitter | Live video transmission |

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
- GitHub

---

# Project Structure

The documentation is divided into several sections.

| Documentation | Description |
|---------------|-------------|
| Autopilot | Flight controller installation and configuration |
| Altitude Hold | Stable altitude control |
| Position Hold | Indoor position stabilization |
| LiDAR & Optical Flow | Sensor integration |
| Raspberry Pi | Embedded software and networking |
| Frame Design | Mechanical development |
| Delivery System | Payload release mechanism |
| Test Results | Flight tests and evaluation |

---

# Development Process

The project was developed iteratively.

Major development milestones included:

- Pilot selection and simulator training
- Replacement of damaged hardware
- Installation of ArduPilot
- Sensor calibration
- Flight controller tuning
- LiDAR integration
- Flight stability optimization
- Altitude Hold implementation
- Position Hold implementation
- Design of 3D-printed components
- Raspberry Pi integration
- Development of the delivery mechanism

---

# Current Project Status

## Completed

- ArduPilot installation
- Flight controller configuration
- Sensor calibration
- LiDAR integration
- Flight testing
- Altitude Hold
- Position Hold
- Mechanical frame extensions
- 3D-printed mounting components

## In Progress

- Raspberry Pi communication
- AI Camera integration
- Autonomous payload delivery
- AI-based object recognition

---

# Repository Structure

```
docs/
│
├── README.md
├── autopilot.md
├── altitude-hold.md
├── position-hold.md
├── lidar-optical-flow.md
├── raspberry-pi.md
├── frame-design.md
├── delivery-system.md
└── test-results.md
```

---

# Technologies

- ArduPilot
- Mission Planner
- MAVSDK
- MAVProxy
- DroneKit
- OpenCV
- Raspberry Pi OS
- Python
- GitHub

---

# Future Work

Future development focuses on:

- Complete Raspberry Pi integration
- AI-based object detection
- Autonomous indoor navigation
- Autonomous package delivery
- Further optimization of flight stability
- Extended flight testing

---

# Authors

Project Group 3

Frankfurt University of Applied Sciences

Adaptive Knowledge Systems
