# 01 – System Overview

## Ziel

Eine FPV-Drohne soll eine Nutzlast zu einem Ziel transportieren und nach visueller Zielbestätigung abwerfen.

## Ebenen

### Flight Controller

ArduPilot übernimmt:
- Stabilisierung
- Motorsteuerung
- Sensorfusion
- Flight Modes
- Navigation

### Companion Computer

Der Raspberry Pi übernimmt:
- Kameraverarbeitung
- KI-Objekterkennung
- ArUco-Verifizierung
- Servo-Steuerung
- optional MAVLink-Kommandos

## State Machine

```text
SEARCH_AI
   ↓ MobileNet-SSD findet Zielklasse
VERIFY_ARUCO
   ↓ Marker gefunden
DROP
   ↓ Servo
FINISHED
```

## Wichtig

Die direkte autonome Flugsteuerung ist als experimenteller Code separat gekennzeichnet. Die Vision-/Servo-Pipeline und die ArduPilot-Sensor-/Flight-Mode-Konfiguration sind getrennt dokumentiert.
