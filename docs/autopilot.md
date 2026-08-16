# Autopilot Integration

## 1. Ziel

Integration und Konfiguration eines Autopilot-Systems für die FPV-Drohne.

## 2. Hardware

- Flywoo GOKU GN745 Flight Controller
- ELRS Receiver
- GPS Module
- Raspberry Pi Zero 2 WH
- Raspberry Pi AI Camera

## 3. Software

- ArduPilot / ArduCopter
- Mission Planner
- MAVProxy
- MAVLink

## 4. Durchführung

Zunächst wurde ArduPilot auf dem Flight Controller installiert und konfiguriert.

Anschließend wurden:
- Sensoren kalibriert,
- Flugmodi eingerichtet,
- Motoren getestet,
- Filter und PID-Werte angepasst,
- mehrere Testflüge durchgeführt.

## 5. Flight Controller

Der ursprüngliche Flight Controller wurde durch einen Flywoo GOKU GN745 ersetzt.

Da der Controller mit einer 45°-Drehung montiert wurde, musste die Board-Orientierung angepasst werden.

### Orientierung

```text
AHRS_ORIENTATION = Custom Rotation

CUST_ROT1_ROLL  = 180
CUST_ROT1_PITCH = 0
CUST_ROT1_YAW   = 225
```

## 6. Motor-Konfiguration

DShot600 wurde aktiviert.

```text
MOT_PWM_TYPE = 6
MOT_SPIN_ARM = 0.03
MOT_SPIN_MIN = 0.06
```

Die Motorreihenfolge wurde an die ArduPilot-Konfiguration angepasst.

Ein Motor-Test über MAVProxy wurde erfolgreich durchgeführt.

## 7. Filter

Folgende Einstellungen wurden angepasst:

```text
INS_GYRO_FILTER = 80
INS_ACCEL_FILTER = 20

INS_HNTCH_ENABLE = 1
INS_HNTCH_MODE   = 3
INS_HNTCH_FREQ   = 80
INS_HNTCH_BW     = 40
INS_HNTCH_ATT    = 40
```

Der Dynamic Harmonic Notch Filter wurde zur Reduzierung von Vibrationsproblemen aktiviert.

## 8. PID-Tuning

### Pitch

```text
ATC_RAT_PIT_P = 0.06
ATC_RAT_PIT_I = 0.06
ATC_RAT_PIT_D = 0.002
```

### Roll

```text
ATC_RAT_RLL_P = 0.06
ATC_RAT_RLL_I = 0.06
ATC_RAT_RLL_D = 0.002
```

Die PID-Werte wurden zur Verbesserung der Flugstabilität angepasst.

## 9. Sensoren

- LiDAR installiert und kalibriert.
- GPS-Modul ersetzt.
- Internes Barometer getestet.
- Kompass mehrfach kalibriert.
- Beschleunigungssensor kalibriert.
- Vibrationsprobleme untersucht und reduziert.

## 10. Ergebnis

Die Verbindung mit Mission Planner wurde erfolgreich hergestellt.

ArduPilot erkannte das Board als:

```text
ArduCopter V4.6.3
FlywooF745
QUAD/X
```

MAVProxy empfing erfolgreich 1180 Parameter und Live-Telemetrie.

Damit wurde eine funktionierende Grundlage für autonome Flugsteuerung geschaffen.
