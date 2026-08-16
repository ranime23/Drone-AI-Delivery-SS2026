# Altitude Hold

## 1. Ziel

Stabile Höhenhaltung der Drohne im Innenbereich.

## 2. Verwendete Komponenten

- ArduPilot
- Flight Controller
- MicroAir MTF-01P LiDAR

## 3. Ausgangssituation

Zunächst wurde das interne Barometer des Flight Controllers für die Höhenmessung verwendet.

Während der Tests zeigte sich, dass die Höhenregelung durch Vibrationen beeinflusst wurde und die Ergebnisse nicht ausreichend stabil waren.

## 4. LiDAR-Integration

Zur Verbesserung der Höhenmessung wurde der LiDAR-Sensor installiert und kalibriert.

Wichtige Range-Finder-Parameter:

```text
RNGFND1_MAX_CM  = 700
RNGFND1_MIN_CM  = 20
RNGFND1_GNDCLEAR = 10
RNGFND1_ORIENT  = 25
RNGFND1_POS_X   = 0.05
RNGFND1_POS_Z   = 0.01
EK3_RNG_USE_HGT = -1
```

## 5. Durchführung

Der Altitude-Hold-Modus wurde in Mission Planner aktiviert.

Es wurden mehrere Testflüge durchgeführt.

Dabei wurden:
1. das interne Barometer getestet,
2. das Verhalten der Höhenregelung beobachtet,
3. der LiDAR installiert,
4. der LiDAR kalibriert,
5. der Range Finder konfiguriert,
6. Filterparameter angepasst,
7. Vibrationen reduziert,
8. weitere Testflüge durchgeführt.

## 6. Beobachtungen

- Ein ruhiger Flug verbessert die Stabilität.
- Reduzierte Vibrationen führen zu besseren Ergebnissen.
- Die LiDAR-basierte Höhenmessung lieferte bessere Ergebnisse als das interne Barometer.
- Die Drohne konnte ihre Höhe erfolgreich halten.

## 7. Vibrationsreduzierung

Zur Verbesserung der Flugstabilität wurden:
- Gyro-Filter,
- Accelerometer-Filter,
- Dynamic Harmonic Notch Filter,
- PID-Werte

angepasst.

Zusätzlich wurden die Landefüße mit Dämpfungsmaterial versehen.

## 8. Ergebnis

**Altitude Hold funktioniert erfolgreich und wurde in mehreren Testflügen überprüft.**
