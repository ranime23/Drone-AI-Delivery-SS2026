# 05 – Altitude Hold

## Ziel

Stabile Höhenhaltung im Innenbereich.

## Entwicklungsweg

1. Internes Barometer getestet.
2. Ergebnisse für den vorgesehenen Aufbau nicht ausreichend.
3. LiDAR integriert.
4. LiDAR kalibriert.
5. Filter/Controller angepasst.
6. Mehrere Testflüge.

## Relevante Parameter

```text
RNGFND_FILT = 0.5
RNGFND1_TYPE = 10
RNGFND1_GNDCLEAR = 10
RNGFND1_MAX_CM = 700
RNGFND1_MIN_CM = 20
RNGFND1_ORIENT = 25
RNGFND1_POS_X = 0.05
RNGFND1_POS_Y = 0
RNGFND1_POS_Z = 0.01

EK3_RNG_USE_HGT = -1
EK3_RNG_I_GATE = 500
EK3_RNG_M_NSE = 0.5

PSC_POSZ_P = 1
PSC_ACCZ_P = 0.5
PSC_ACCZ_I = 1
PSC_ACCZ_D = 0
PSC_ACCZ_IMAX = 800

PILOT_ACCEL_Z = 250
PILOT_SPEED_UP = 250
```

## Beobachtungen

Vibrationen beeinflussen die Höhenregelung negativ. Gedämpfte Landefüße und Filteroptimierung wurden zur Verbesserung eingesetzt.

Altitude Hold wurde im Projekt erfolgreich getestet.
