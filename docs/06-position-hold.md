# 06 – Position Hold

## Voraussetzungen

- Altitude Hold stabil
- LiDAR
- Optical Flow
- geringe Vibrationen

## Optical Flow

```text
FLOW_TYPE = 5
FLOW_POS_X = 0.06
FLOW_POS_Y = 0
FLOW_POS_Z = 0.01

EK3_FLOW_USE = 1
EK3_FLOW_DELAY = 10
EK3_FLOW_I_GATE = 300
EK3_FLOW_M_NSE = 0.25
EK3_MAX_FLOW = 2.5
```

## Horizontaler Controller

```text
PSC_POSXY_P = 1
PSC_VELXY_P = 2
PSC_VELXY_I = 1
PSC_VELXY_D = 0.25
PSC_VELXY_FF = 0
PSC_VELXY_IMAX = 1000
PSC_JERK_XY = 5
```

## Flow/Position Hold

```text
FHLD_BRAKE_RATE = 8
FHLD_FILT_HZ = 5
FHLD_FLOW_MAX = 0.6
FHLD_QUAL_MIN = 10
FHLD_XY_FILT_HZ = 5
FHLD_XY_I = 0.3
FHLD_XY_IMAX = 3000
FHLD_XY_P = 0.2
PHLD_BRAKE_ANGLE = 3000
PHLD_BRAKE_RATE = 8
```

Position Hold wurde erfolgreich getestet. Starke Vibrationen verschlechterten die Positionshaltung deutlich.
