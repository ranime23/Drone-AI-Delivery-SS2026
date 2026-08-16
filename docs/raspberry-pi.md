# Raspberry Pi Integration

## 1. Ziel

Der Raspberry Pi Zero 2 W/WH dient als zentrale Recheneinheit für:
- Kameraauswertung,
- KI-Objekterkennung,
- ArUco-Erkennung,
- MAVLink-Kommunikation,
- Ansteuerung des Abwurfmechanismus.

## 2. Software-Umgebung

Installiert bzw. vorbereitet wurden:

- OpenCV
- pymavlink
- DroneKit
- MAVSDK
- MAVProxy
- libcamera-related packages

Zusätzlich wurden:
- das Root-Dateisystem erweitert,
- pip- und APT-Caches bereinigt,
- ein DroneKit-Kompatibilitätspatch vorbereitet,
- MAVSDK initialisiert.

## 3. Netzwerk

Für den mobilen Betrieb wurde ein Dual-Mode-WLAN-Konzept vorbereitet.

Verwendete Werkzeuge:

```text
iw
systemd
NetworkManager
nmcli
```

Die virtuelle Schnittstelle `uap0` wurde als Access Point konfiguriert.

Die Konfiguration umfasst:
- Access-Point-Profil
- WPA-PSK
- separates MAC Address Setup
- automatischen Start über systemd

## 4. MAVLink-Verbindung

Die Verbindung zwischen Raspberry Pi und Flight Controller wurde über eine serielle UART-Verbindung aufgebaut.

Verwendet wurde:

```text
/dev/serial0
```

Die Verkabelung erfolgt gekreuzt:

```text
Flight Controller TX4 -> Raspberry Pi RX
Flight Controller RX4 -> Raspberry Pi TX
Flight Controller GND -> Raspberry Pi GND
```

Für SERIAL4 wurde MAVLink konfiguriert.

```text
SERIAL4_PROTOCOL = 2
SERIAL4_BAUD     = 115
SERIAL4_OPTIONS  = 0
```

## 5. Erfolgreicher Verbindungstest

MAVProxy meldete:

```text
Detected vehicle 1:1
online system 1
Mode STABILIZE

AP: ArduCopter V4.6.3
AP: FlywooF745
AP: Frame: QUAD/X

Received 1180 parameters
Saved 1180 parameters to mav.parm

Flight battery 90 percent
```

Damit wurde bestätigt, dass:
- der Heartbeat empfangen wird,
- ArduPilot erkannt wird,
- der Flight Controller erkannt wird,
- Parameter übertragen werden,
- Telemetriedaten empfangen werden.

## 6. Mission Planner

MAVProxy kann als Telemetrie-Bridge verwendet werden, um die MAVLink-Daten vom Raspberry Pi über WLAN an Mission Planner weiterzugeben.

Beispiel:

```bash
mavproxy.py --master=/dev/serial0 --baudrate=115200 --out=udp:<PC-IP>:14550
```

## 7. Motor-Test

Ein Motor-Test wurde erfolgreich über MAVProxy durchgeführt.

Beispiel:

```text
motortest 1 0 5 2
```

Dabei wurde Motor 1 für den Test angesteuert.

Damit wurde die Kommunikationskette praktisch überprüft:

```text
Raspberry Pi
     |
   MAVLink
     |
Flight Controller
     |
    ESC
     |
   Motor
```

## 8. Status

| Component | Status |
|---|---|
| Raspberry Pi environment | Implemented |
| Python dependencies | Installed |
| MAVProxy | Working |
| MAVLink connection | Successfully tested |
| Mission Planner communication | Successfully established |
| Parameter download | 1180 parameters received |
| Motor command | Successfully tested |
| Camera integration | Separate test setup available |
| Complete autonomous mission | Requires integrated final flight test |
