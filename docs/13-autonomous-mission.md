# 13 – Autonomous Mission

## Zielablauf

```text
AUTO / SEARCH
      ↓
MobileNet-SSD erkennt Ziel
      ↓
VERIFY_ARUCO
      ↓
ArUco bestätigt Ziel
      ↓
STOP / CENTER
      ↓
SERVO DROP
      ↓
RTL / MISSION END
```

## Suchflug

Das Projekt beschreibt ein Raster-/Zick-Zack-Suchmuster.

ArduPilot kann die Wegpunkte abfliegen; der Raspberry Pi analysiert währenddessen das Kamerabild.

## Architektur A – empfohlen für reproduzierbare Entwicklung

```text
Mission Planner / ArduPilot
        ↓
fliegt Suchraster
        ↓
Raspberry Pi
        ↓
KI erkennt Ziel
        ↓
ArUco verifiziert
        ↓
Abwurf
```

## Architektur B – experimentelle Companion-Control

Der experimentelle Code sendet MAVLink-Geschwindigkeitsvektoren.

Er verwendet:
- `set_position_target_local_ned_send`
- `SEARCH_PATTERN`
- `CENTERING`
- `DROP`

Diese Variante ist **experimentell** und muss vor einem echten Flug separat validiert werden.

## Kritischer Punkt

Ein früher Entwicklungsstand bezeichnete den ArUco-basierten Bewegungsregler teilweise als „KI-Steuerung“. Technisch ist die Marker-Erkennung jedoch Computer Vision. Die echte neuronale KI ist MobileNet-SSD.

## Sichere Reihenfolge

```text
Vision → ArUco → Servo → MAVLink read-only
→ MAVLink command ohne Propeller
→ kontrollierter Flug
→ autonome Bewegung
```
