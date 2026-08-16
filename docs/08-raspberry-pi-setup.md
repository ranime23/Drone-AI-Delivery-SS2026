# 08 – Raspberry Pi Setup

## Speicher

```bash
sudo raspi-config nonint do_expand_rootfs
python3 -m pip cache purge
sudo apt clean
sudo reboot
```

Dies löste das dokumentierte Problem:

```text
OSError: [Errno 28] No space left on device
```

## Systempakete

```bash
sudo apt update
sudo apt install -y git python3-pip python3-numpy libcamera-apps python3-libcamera
```

## Python

```bash
TMPDIR=/var/tmp python3 -m pip install   opencv-contrib-python   pymavlink   dronekit   mavsdk   MAVProxy   --user --break-system-packages --no-cache-dir
```

## DroneKit Patch

```python
import collections
import collections.abc
collections.MutableMapping = collections.abc.MutableMapping
import dronekit
```

## MAVSDK

```python
from mavsdk import System
import asyncio

async def fetch_backend():
    drone = System()
    await drone.connect(system_address="udp://:14550")

asyncio.run(fetch_backend())
```

## Kamera

Für die Pi-Kamera wurde eine `libcamerasrc`-GStreamer-Pipeline mit 640x480 und 30 FPS dokumentiert.

## OpenCV Test

```bash
python3 -c "import cv2; print(cv2.__version__)"
```
