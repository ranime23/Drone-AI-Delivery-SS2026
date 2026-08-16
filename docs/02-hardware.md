# 02 – Hardware

## Flight Controller

**Flywoo GOKU GN745**

Projektangaben:
- STM32F745
- 216 MHz
- 1 MB Flash
- 45A AIO
- 2–6S
- AM32

Der dokumentierte MAVProxy-Test erkannte `FlywooF745`, `ArduCopter V4.6.3` und `QUAD/X`.

## Komponenten

| Komponente | Aufgabe |
|---|---|
| FPV-Drohne | Flugplattform |
| GN745 | Flight Controller |
| ELRS | RC-Link |
| GPS | Navigation |
| externer Compass | Heading |
| MicroAir MTF-01P | LiDAR / Höhe |
| Optical Flow | relative X/Y-Bewegung |
| Raspberry Pi Zero 2 W | Companion Computer |
| Raspberry Pi AI Camera | Vision |
| Miuzei MS18 | Payload Servo |

## Servo-Verkabelung

| Servo | Anschluss |
|---|---|
| Rot | 5V FC |
| Braun | GND FC |
| Orange | GPIO 18 / Pin 12 Pi |

## Pi-Modell prüfen

```bash
cat /proc/device-tree/model
```

Die dokumentierte Raspberry-Pi-Integrationsumgebung wurde mit einem Zero 2 W vorbereitet.
