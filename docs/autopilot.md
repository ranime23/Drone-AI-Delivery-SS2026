# Autopilot Integration

## Ziel

Integration und Konfiguration eines Autopilot-Systems für die FPV-Drohne.

## Verwendete Hardware

- Flywoo GOKU GN745 Flight Controller
- ELRS Empfänger
- GPS Modul
- Raspberry Pi Zero 2 WH
- Raspberry Pi AI Camera

## Verwendete Software

- ArduPilot
- Mission Planner
- GitHub

## Durchführung

Zunächst wurde ArduPilot auf dem Flight Controller installiert und konfiguriert.

Anschließend wurden die Sensoren kalibriert und die ersten Flugmodi eingerichtet.

Mehrere Testflüge wurden durchgeführt, um die Stabilität der Drohne zu überprüfen und die Parameter schrittweise anzupassen.

## Ergebnis

Die Verbindung mit Mission Planner konnte erfolgreich hergestellt werden.

Mehrere Flugmodi wurden erfolgreich konfiguriert und getestet.

Eine stabile Grundlage für weitere Entwicklungen wurde geschaffen.

## Wichtige Konfigurationsänderungen

### Flight Controller
- Austausch des ursprünglichen Flight Controllers durch einen Flywoo GOKU GN745.
- Durchführung einer vollständigen 6-Achsen-Kalibrierung des Beschleunigungssensors.
- Anpassung der Board-Orientierung aufgrund einer 45°-Montage.
- AHRS_ORIENTATION wurde auf Custom Rotation gesetzt.
- CUST_ROT1_ROLL = 180
- CUST_ROT1_PITCH = 0
- CUST_ROT1_YAW = 225

### Motor-Konfiguration
- Umstellung auf DShot600.
- Anpassung der Motorreihenfolge für ArduPilot.
- MOT_PWM_TYPE = 6 (DShot600)
- MOT_SPIN_ARM = 0.03
- MOT_SPIN_MIN = 0.06

### Filter und PID-Tuning
- Anpassung der Gyro- und Accelerometer-Filter.
- Aktivierung des Dynamic Harmonic Notch Filters.
- Reduzierung der PID-Werte zur Verbesserung der Flugstabilität.
- INS_GYRO_FILTER = 80
- INS_ACCEL_FILTER = 20
- INS_HNTCH_ENABLE = 1
- INS_HNTCH_MODE = 3 (ESC Telemetry)
- INS_HNTCH_FREQ = 80
- INS_HNTCH_BW = 40
- INS_HNTCH_ATT = 40

### PID-Anpassungen
- ATC_RAT_PIT_P = 0.06
- ATC_RAT_PIT_I = 0.06
- ATC_RAT_PIT_D = 0.002

- ATC_RAT_RLL_P = 0.06
- ATC_RAT_RLL_I = 0.06
- ATC_RAT_RLL_D = 0.002

### Sensoren
- LiDAR-Sensor installiert und kalibriert.
- GPS-Modul ersetzt.
- Test des internen Barometers für Altitude Hold.
- Mehrfache Kalibrierung des Kompasses und Beschleunigungssensors.
- Anpassungen zur Reduzierung von Vibrationsproblemen.

## Nächste Schritte

- Verbesserung der Vibrationsdämpfung
- Integration der Raspberry-Pi-Kommunikation
- Vollständige autonome Navigation
