# 09 – MAVLink / MAVProxy

## Erfolgreicher Verbindungstest

Dokumentierter Output:

```text
Detected vehicle 1:1 on link 0
AP: ArduCopter V4.6.3
AP: FlywooF745
AP: Frame: QUAD/X
Received 1180 parameters (ftp)
Saved 1180 parameters to mav.parm
Flight battery 90 percent
```

## MAVProxy

```bash
mavproxy.py --master=/dev/serial0 --baudrate=115200
```

## UDP Bridge

```bash
mavproxy.py   --master=/dev/serial0   --baudrate=115200   --out=udp:<PC-IP>:14550
```

## UART

```bash
stty -F /dev/serial0 115200
cat /dev/serial0
```

`cat` ist kein ausreichender MAVLink-Test, da MAVLink binär ist. Der Heartbeat-Test mit MAVProxy ist entscheidend.

## TX/RX

```text
Pi TX → FC RX
Pi RX → FC TX
Pi GND → FC GND
```

## Mini-UART

Die Projektentwicklung dokumentiert als mögliche Stabilisierung:

```text
dtoverlay=miniuart-bt
core_freq=250
```

## Systemd

Eine Beispielservice-Datei befindet sich in:

```text
config/mavproxy.service.example
```
