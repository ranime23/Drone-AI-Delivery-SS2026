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
- Anpassung der Board-Orientierung aufgrund einer 45°-Montage.

### Motor-Konfiguration
- Umstellung auf DShot600.
- Anpassung der Motorreihenfolge für ArduPilot.

### Filter und PID-Tuning
- Anpassung der Gyro- und Accelerometer-Filter.
- Aktivierung des Dynamic Harmonic Notch Filters.
- Reduzierung der PID-Werte zur Verbesserung der Flugstabilität.

### Sensoren
- LiDAR-Sensor installiert und kalibriert.
- GPS-Modul ersetzt.
- Test des internen Barometers für Altitude Hold.

## Nächste Schritte

- Verbesserung der Vibrationsdämpfung
- Integration der Raspberry-Pi-Kommunikation
- Vollständige autonome Navigation
