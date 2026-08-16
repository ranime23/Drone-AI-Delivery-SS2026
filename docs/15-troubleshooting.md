# 15 – Troubleshooting

## MAVProxy kein Heartbeat

```bash
mavproxy.py --master=/dev/serial0 --baudrate=115200
```

Prüfen:
- TX/RX
- GND
- Baudrate
- UART
- Flight Controller Stromversorgung
- andere Prozesse auf `/dev/serial0`

## `cat /dev/serial0` leer

Nicht automatisch ein Fehler. MAVLink ist binär. MAVProxy-Heartbeat verwenden.

## Kamera

```bash
libcamera-hello
```

Danach GStreamer/libcamera-Pipeline testen.

## ArUco fehlt

```bash
TMPDIR=/var/tmp python3 -m pip install opencv-contrib-python --user --break-system-packages --no-cache-dir
```

## Speicher voll

```bash
sudo raspi-config nonint do_expand_rootfs
python3 -m pip cache purge
sudo apt clean
sudo reboot
```

## DroneKit Import Error

```python
import collections
import collections.abc
collections.MutableMapping = collections.abc.MutableMapping
import dronekit
```

## Servo zittert

- Versorgung prüfen
- Mechanik entlasten
- `servo.detach()` verwenden
- bei notwendigem Haltesignal Hardware-PWM/pigpio prüfen

## MobileNet-Dateien fehlen

Benötigt:

```text
MobileNetSSD_deploy.prototxt
MobileNetSSD_deploy.caffemodel
```

Diese Dateien müssen entsprechend der verwendeten Modellquelle bereitgestellt werden.
