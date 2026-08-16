# KI-Drohnenprojekt – Autonome Objektauslieferung

## 1. Projektziel

Ziel des Projekts ist die Entwicklung einer FPV-Drohne für eine automatisierte Objektauslieferung.

Die Drohne soll:
1. eine definierte Suchroute autonom abfliegen,
2. ein Zielobjekt mit einer Kamera und einem KI-Modell erkennen,
3. das Ziel zusätzlich über einen ArUco-Marker verifizieren,
4. die Drohne während der Verifikation stabil anhalten,
5. die Nutzlast über einen Servo freigeben,
6. anschließend zum Startpunkt zurückkehren.

## 2. Hardware

- FPV-Drohne
- Flywoo GOKU GN745 / FlywooF745 Flight Controller
- ELRS Receiver
- GPS-Modul
- Raspberry Pi Zero 2 W / WH
- Raspberry Pi AI Camera
- MicroAir MTF-01P LiDAR / Optical-Flow-Sensor
- Miuzei Micro Servo 9g MS18
- Li-Ion/LiPo power supply
- FPV camera and video transmitter

## 3. Software

- ArduPilot / ArduCopter
- Mission Planner
- MAVProxy
- MAVLink
- Python
- OpenCV
- MobileNet-SSD
- ArUco
- pymavlink
- DroneKit
- MAVSDK

## 4. Project status

### Flight Controller
- ArduPilot installed and configured.
- FlywooF745 identified by ArduPilot.
- Board orientation adapted for the 45° mounting.
- DShot600 configured.
- Motor order adapted.
- Gyro/accelerometer filters and PID values tuned.
- Dynamic Harmonic Notch Filter configured.

### Sensors
- GPS replaced.
- LiDAR installed and calibrated.
- Internal barometer tested.
- LiDAR used to improve altitude estimation.
- Optical Flow integrated and tested.
- Vibration reduction measures implemented.

### Flight modes
- Altitude Hold successfully tested.
- Position Hold successfully tested.
- Position Hold works best with sufficiently stable flight and reduced vibration.

### Raspberry Pi / MAVLink
The Raspberry Pi communication with the Flight Controller was successfully established.

MAVProxy detected:
- ArduCopter V4.6.3
- FlywooF745
- QUAD/X frame
- 1180 parameters
- live battery telemetry

The communication path was tested through the Raspberry Pi and Mission Planner.

### Payload mechanism
The Miuzei MS18 servo was tested from the Raspberry Pi. A 90° release movement was implemented. The servo signal can be detached after movement to reduce vibration and unnecessary holding current.

### AI / target verification
The intended software architecture uses:
- MobileNet-SSD for object detection.
- ArUco for target verification.
- MAVLink/ArduPilot for flight-mode control.
- Servo control for payload release.

## 5. Autonomous mission concept

```text
TAKEOFF
   |
   v
SEARCH ROUTE / AUTO
   |
   v
MobileNet-SSD detects target
   |
   v
BRAKE / position stabilization
   |
   v
ArUco verification
   |
   +---- marker not found ----> AUTO / continue search
   |
   v
SERVO RELEASE
   |
   v
RTL
   |
   v
START POSITION
```

## 6. Important note

The project documentation distinguishes between components that were physically tested and the complete end-to-end autonomous delivery mission.

A complete autonomous mission should only be reported as successfully demonstrated after an actual integrated flight test confirms the complete sequence from takeoff through detection, verification, release and return.
