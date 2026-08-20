# KI-Drohnen – Autonomous Target Search & Payload Delivery
## 👥 Group Members

- **Ranime Ben Afia**
- **Adina Ritter**
- **Algis**
- **Anja Kraushaar**
## Zweck

Dieses Repository ist die vollständige, reproduzierbare Online-Dokumentation des KI-Drohnenprojekts.

Das Projekt kombiniert:

- FPV-Drohne
- Flywoo GOKU GN745 Flight Controller
- ArduPilot / Mission Planner
- GPS und externen Compass
- MicroAir MTF-01P LiDAR mit Optical Flow
- Raspberry Pi Zero 2 W
- Raspberry-Pi-Kamera
- MobileNet-SSD zur KI-Objekterkennung
- ArUco zur deterministischen Zielverifizierung
- Servo zur Payload-Freigabe
- MAVLink / MAVProxy

## Wichtig: Implementiert vs. experimentell

Die Dokumentation trennt bewusst zwischen Funktionen, die im Projekt konfiguriert/getestet wurden, und experimentellen Integrationsschritten.

### Konfiguriert bzw. getestet

- ArduPilot auf Flywoo GOKU GN745
- Mission Planner
- Sensor-Kalibrierungen
- Custom Board Orientation
- DShot600
- PID- und Filterkonfiguration
- LiDAR
- Optical Flow
- Altitude Hold
- Position Hold
- Raspberry-Pi-Umgebung
- MAVLink/MAVProxy-Verbindung
- Servo-Abwurf
- MobileNet-SSD-Objekterkennung
- ArUco-Verifizierung
- State Machine `SEARCH_AI → VERIFY_ARUCO → DROP`

### Experimentell

Die direkte autonome Flugsteuerung des Raspberry Pi über MAVLink ist separat dokumentiert. Sie darf nicht ohne zusätzliche Sicherheits- und Flugtests als flugerprobte Funktion betrachtet werden.

**MobileNet-SSD ist die KI-Komponente. ArUco ist keine neuronale KI, sondern eine Computer-Vision-Verifizierung.**

---

## Architektur

```text
 GPS / Compass ───────────────┐
 LiDAR ───────────────────────┤
 Optical Flow ────────────────┤
                              ▼
                     ┌──────────────────┐
                     │ Flywoo GN745     │
                     │ ArduPilot        │
                     │ EKF3 + Control   │
                     └────────┬─────────┘
                              │ MAVLink
                              ▼
                     ┌──────────────────┐
                     │ Raspberry Pi     │
                     │                  │
 Camera ────────────►│ MobileNet-SSD    │
                     │      ↓           │
                     │ ArUco Verify     │
                     │      ↓           │
                     │ Servo Trigger    │
                     └────────┬─────────┘
                              │ GPIO 18
                              ▼
                       Payload Servo
```

## Reproduktionsreihenfolge

```text
1. Hardware prüfen
2. ArduPilot installieren
3. Kalibrieren
4. Board Orientation
5. Motor/ESC
6. Filter + PID
7. Altitude Hold
8. LiDAR
9. Optical Flow
10. Position Hold
11. Raspberry Pi
12. MAVLink
13. Kamera
14. MobileNet-SSD
15. ArUco
16. Servo
17. Kombination
18. autonome Flugsteuerung erst zuletzt
```

## Repository-Struktur

```text
.
├── README.md
├── index.md
├── mkdocs.yml
├── requirements-pi.txt
├── CONTRIBUTING.md
├── CHANGELOG.md
├── LICENSE
├── config/
│   ├── drone-parameters.param
│   └── mavproxy.service.example
├── scripts/
│   ├── init_libs.py
│   ├── servo_test.py
│   ├── ki_autonom_abwurf.py
│   └── autonomous_search_aruco_experimental.py
├── docs/
│   ├── 01-system-overview.md
│   ├── 02-hardware.md
│   ├── 03-ardupilot-installation.md
│   ├── 04-autopilot-configuration.md
│   ├── 05-altitude-hold.md
│   ├── 06-position-hold.md
│   ├── 07-lidar-optical-flow.md
│   ├── 08-raspberry-pi-setup.md
│   ├── 09-mavlink-mavproxy.md
│   ├── 10-ai-object-detection.md
│   ├── 11-aruco-verification.md
│   ├── 12-servo-payload-drop.md
│   ├── 13-autonomous-mission.md
│   ├── 14-testing-results.md
│   ├── 15-troubleshooting.md
│   └── 16-full-parameter-reference.md
└── assets/
    └── README.md
```

## Final Parameter Export

`config/drone-parameters.param` ist der unveränderte Final Export mit **1180 Parameterzeilen**.

Diese Datei ist die Source of Truth für die aufgezeichnete ArduPilot-Konfiguration.

## Schnellstart Raspberry Pi

```bash
sudo apt update
sudo apt install -y git python3-pip python3-numpy libcamera-apps python3-libcamera
TMPDIR=/var/tmp python3 -m pip install opencv-contrib-python pymavlink dronekit mavsdk MAVProxy --user --break-system-packages --no-cache-dir
sudo apt install -y python3-gpiozero python3-rpi.gpio
```

## Sicherheit

Bench-Tests mit Motoren nur im sicheren Zustand durchführen. Für Tests der autonomen Flugsteuerung zunächst Propeller entfernen bzw. eine geeignete kontrollierte Testumgebung verwenden. Flight Modes, Failsafe, RC und Notabschaltung vor jedem autonomen Test prüfen.

## Dokumentation

Die ausführlichen Kapitel befinden sich im Ordner `docs/`. Die Seite `docs/04-autopilot-configuration.md` und `docs/16-full-parameter-reference.md` enthalten die Parameter nach Funktionsgruppen.
