# 14 – Test Results

## Initial Flight Tests

Mehrere frühe Flugversuche führten zu Abstürzen und Hardwarebeschädigungen. Daraus entstand die Erkenntnis, vor Realflugtests Simulatortraining und Pilottraining einzusetzen.

## Hardware Changes

- Flight Controller durch Flywoo GOKU GN745 ersetzt
- GPS ersetzt
- VTX-Antenne ersetzt
- Power-Kabel neu verlötet
- Schrumpfschlauch zur mechanischen Sicherung

## ArduPilot

Erfolgreich installiert und mit Mission Planner verbunden.

## MAVProxy

Erfolgreicher Heartbeat und Empfang aller 1180 Parameter.

## Altitude Hold

Erfolgreich getestet.

Probleme:
- Vibration
- Barometerleistung
- Sensor-/Filterabstimmung

Verbesserungen:
- LiDAR
- Filter
- PID
- gedämpfte Landefüße

## Position Hold

Erfolgreich getestet.

Voraussetzungen:
- Altitude Hold
- LiDAR
- Optical Flow
- Vibrationsreduktion

## Raspberry Pi

Das Environment wurde vorbereitet. Ein Speicherproblem wurde durch rootfs expansion und Cache-Clearing gelöst.

## Servo

GPIO-18-Servo wurde getestet. `detach()` reduzierte Zittern/Brummen.

## KI

MobileNet-SSD wurde als vortrainierte Objekterkennung eingesetzt.

## Lessons Learned

1. Stabilität zuerst.
2. Vibrationen sind kritisch.
3. Sensoren einzeln testen.
4. Servo unabhängig testen.
5. KI und ArUco unabhängig testen.
6. Erst danach integrieren.
7. Parameter-Export versionieren.
