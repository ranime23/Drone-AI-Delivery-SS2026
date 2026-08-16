# 03 – ArduPilot Installation

## 1. Firmware

Flight Controller per USB mit Mission Planner verbinden und ArduCopter installieren.

Dokumentierter Laufzeitstand:

```text
ArduCopter V4.6.3
Board: FlywooF745
Frame: QUAD/X
```

## 2. Kalibrierung

Nach dem FC-Austausch wurden Kalibrierungen erneut durchgeführt:
- Accelerometer
- Compass
- Radio
- Motor/ESC
- Sensoren

## 3. Board Orientation

```text
AHRS_ORIENTATION = 101
CUST_ROT_ENABLE = 1
CUST_ROT1_ROLL = 180
CUST_ROT1_PITCH = 0
CUST_ROT1_YAW = 225
```

## 4. DShot600

```text
MOT_PWM_TYPE = 6
MOT_SPIN_ARM = 0.03
MOT_SPIN_MIN = 0.06
```

## 5. Filter

```text
INS_GYRO_FILTER = 80
INS_ACCEL_FILTER = 20
INS_HNTCH_ENABLE = 1
INS_HNTCH_MODE = 3
INS_HNTCH_FREQ = 80
INS_HNTCH_BW = 40
INS_HNTCH_ATT = 40
```

## 6. Erstflug

Erst Stabilize/Manual-Verhalten prüfen. Danach kontrollierter Hover. Erst wenn das stabil ist, Altitude Hold und Position Hold testen.
