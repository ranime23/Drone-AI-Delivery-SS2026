# 07 – LiDAR und Optical Flow

## LiDAR

MicroAir MTF-01P.

Aufgabe:
- Abstand zum Boden
- Höheninformation
- Unterstützung Altitude Hold

```text
RNGFND1_TYPE = 10
RNGFND1_MAX_CM = 700
RNGFND1_MIN_CM = 20
RNGFND1_ORIENT = 25
```

## Optical Flow

Aufgabe:
- relative Bodenbewegung
- Unterstützung Position Hold
- GPS-unabhängige Positionsunterstützung im Innenbereich

```text
FLOW_TYPE = 5
EK3_FLOW_USE = 1
```

## Kritische Punkte

- Sensororientierung
- Sensorposition
- Vibrationen
- Beleuchtung
- geeignete Bodenstruktur
- geeignete Flughöhe
