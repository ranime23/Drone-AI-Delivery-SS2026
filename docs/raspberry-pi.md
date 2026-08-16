# Raspberry Pi Integration

## Overview

A Raspberry Pi Zero 2 W was integrated into the project as an additional onboard computing platform.

The work performed so far mainly focused on preparing the Raspberry Pi environment, installing the required software dependencies and configuring a persistent network setup.

A major objective of the network configuration was to allow the Raspberry Pi to maintain a Wi-Fi connection while simultaneously providing its own local Access Point.

The software environment was also prepared with libraries such as OpenCV, MAVProxy, MAVSDK, pymavlink and DroneKit.

At the current stage of the project, the Raspberry Pi environment and network configuration have been prepared, while communication with the complete drone system is still one of the current challenges.

---

# 1. Hardware

The Raspberry Pi work was performed using:

| Component | Used in the project |
|-----------|---------------------|
| Raspberry Pi | Raspberry Pi Zero 2 W |
| Camera | Raspberry Pi AI Camera |
| Storage | microSD card |
| Network | Integrated Wi-Fi |

The Raspberry Pi runs separately from the ArduPilot flight controller and is being prepared for communication with the remaining drone system.

---

# 2. Software Environment

The following software components were installed or prepared on the Raspberry Pi:

- Raspberry Pi OS
- Python 3
- Git
- NumPy
- OpenCV
- pymavlink
- DroneKit
- MAVSDK
- MAVProxy
- libcamera

The software stack was prepared locally on the Raspberry Pi.

---

# 3. Storage Problem

During dependency installation, a storage problem occurred.

The system produced the following error:

```text
OSError: [Errno 28] No space left on device
```

This occurred during the extraction or installation of larger binary dependencies, for example `grpcio`.

The problem required changes to the Raspberry Pi storage configuration before the installation could continue.

---

# 4. Root Filesystem Expansion

The root filesystem was expanded using:

```bash
sudo raspi-config nonint do_expand_rootfs
```

Afterwards, cached installation files were removed:

```bash
python3 -m pip cache purge
sudo apt clean
```

The Raspberry Pi was then restarted:

```bash
sudo reboot
```

This step was carried out to make the available microSD-card storage accessible to the operating system and to remove unnecessary cached files.

---

# 5. Dependency Installation

After addressing the storage problem, the required system packages were installed.

The following command was used:

```bash
sudo apt update
sudo apt install -y git python3-pip python3-numpy libcamera-apps python3-libcamera
```

This installed the basic development and camera-related dependencies.

---

# 6. Python Packages

The Python control and vision packages were installed using:

```bash
TMPDIR=/var/tmp python3 -m pip install opencv-contrib-python pymavlink dronekit mavsdk MAVProxy --user --break-system-packages --no-cache-dir
```

The temporary build directory was redirected to:

```text
/var/tmp
```

This was done to avoid problems caused by limited temporary RAM-based storage during the installation of larger packages.

The `--no-cache-dir` option was also used to avoid creating unnecessary package-cache data.

---

# 7. Installed Control and Vision Stack

The resulting software stack contains several components with different roles.

| Software | Role in the prepared environment |
|----------|----------------------------------|
| OpenCV | Computer vision library |
| pymavlink | MAVLink communication library |
| MAVProxy | MAVLink command-line and communication tool |
| MAVSDK | MAVLink-based SDK |
| DroneKit | Python drone communication library |
| libcamera | Camera interface |
| NumPy | Numerical Python dependency |

At this stage, the work focused on installing and preparing these components.

Their presence in the environment does not mean that all planned drone functions using these libraries have already been completed.

---

# 8. DroneKit Compatibility Problem

A compatibility problem occurred when using the legacy DroneKit library with newer Python versions.

DroneKit expects:

```python
collections.MutableMapping
```

However, newer Python versions use:

```python
collections.abc.MutableMapping
```

A runtime patch was therefore prepared before importing DroneKit.

The following code was used:

```python
import collections
import collections.abc

collections.MutableMapping = collections.abc.MutableMapping

import dronekit
```

This remaps the old `MutableMapping` reference to the current Python implementation.

---

# 9. MAVSDK Initialization

MAVSDK was also initialized as part of the prepared Raspberry Pi environment.

The following initialization code was used:

```python
from mavsdk import System
import asyncio

async def fetch_backend():
    drone = System()
    await drone.connect(system_address="udp://:14550")

asyncio.run(fetch_backend())
```

The configured connection address is:

```text
udp://:14550
```

The purpose of this initialization step was to prepare the MAVSDK backend and bind the connection to UDP port `14550`.

The complete Raspberry Pi-to-drone communication is still part of the ongoing integration work.

---

# 10. Initialization Script

The compatibility and MAVSDK initialization steps were combined in an `init_libs.py` script.

The documented script is:

```python
import collections
import collections.abc

collections.MutableMapping = collections.abc.MutableMapping

import dronekit

from mavsdk import System
import asyncio

async def fetch_backend():
    drone = System()
    await drone.connect(system_address="udp://:14550")

asyncio.run(fetch_backend())
```

This script performs two preparation tasks:

1. applies the DroneKit compatibility patch,
2. initializes the MAVSDK connection environment.

---

# 11. Network Configuration

Another major part of the Raspberry Pi work was the wireless network configuration.

The objective was to create a persistent setup in which the Raspberry Pi can operate with:

- a normal Wi-Fi Station connection,
- an additional local Access Point.

A virtual wireless interface called:

```text
uap0
```

was created for this purpose. :contentReference[oaicite:2]{index=2}

---

# 12. Wi-Fi Channel Identification

Before creating the Access Point, the channel used by the physical `wlan0` interface was checked.

The following command was used:

```bash
iw dev wlan0 info | grep channel
```

The documented output was:

```text
channel 11 (2462 MHz), width: 20 MHz, center1: 2462 MHz
```

Therefore, the active physical Wi-Fi connection was operating on channel 11 during this configuration. :contentReference[oaicite:3]{index=3}

---

# 13. Virtual Wireless Interface

The additional Access Point requires a virtual wireless interface.

A `systemd` service was therefore created:

```bash
sudo nano /etc/systemd/system/uap0.service
```

The following service configuration was used:

```ini
[Unit]
Description=Instantiate uap0 virtual wireless interface
Requires=sys-subsystem-net-devices-wlan0.device
After=sys-subsystem-net-devices-wlan0.device
Before=NetworkManager.service

[Service]
Type=oneshot
RemainAfterExit=yes
ExecStart=/usr/sbin/iw dev wlan0 interface add uap0 type __ap

[Install]
WantedBy=multi-user.target
```

The important command is:

```bash
iw dev wlan0 interface add uap0 type __ap
```

This creates the virtual `uap0` interface from the physical `wlan0` wireless device. :contentReference[oaicite:4]{index=4}

---

# 14. Persistent Interface Creation

The `systemd` service was used because the virtual interface must be recreated after boot.

The service is configured to run before NetworkManager:

```text
Before=NetworkManager.service
```

This allows `uap0` to exist before NetworkManager attempts to activate the corresponding wireless connection profile.

---

# 15. NetworkManager Access Point Profile

A NetworkManager profile called:

```text
Himbeere_AP
```

was created.

The documented command is:

```bash
sudo nmcli connection add type wifi ifname wlan0 con-name "Himbeere_AP" autoconnect yes ssid "Himbeere"
```

The Access Point SSID was configured as:

```text
Himbeere
```

---

# 16. Access Point Mode

The NetworkManager profile was changed to Access Point mode:

```bash
sudo nmcli connection modify "Himbeere_AP" 802-11-wireless.mode ap 802-11-wireless.band bg ipv4.method shared
```

The important configuration elements are:

```text
802-11-wireless.mode = ap
802-11-wireless.band = bg
ipv4.method = shared
```

This configures the connection as a Wi-Fi Access Point using shared IPv4 networking. :contentReference[oaicite:5]{index=5}

---

# 17. Wi-Fi Security

WPA-PSK security was configured for the Access Point.

The documented command is:

```bash
sudo nmcli connection modify "Himbeere_AP" wifi-sec.key-mgmt wpa-psk wifi-sec.psk "Himbeere"
```

This configured WPA-PSK authentication for the local Access Point.

---

# 18. Binding the Access Point to `uap0`

The NetworkManager profile was then assigned to the virtual interface:

```bash
sudo nmcli connection modify "Himbeere_AP" connection.interface-name uap0 802-11-wireless.channel <CHANNEL>
```

During the documented configuration, the physical interface was operating on channel 11.

The Access Point therefore had to use a compatible channel configuration because both interfaces use the same physical Wi-Fi hardware.

---

# 19. PMF Configuration

Protected Management Frames were adjusted to avoid connection problems.

The following command was used:

```bash
sudo nmcli connection modify "Himbeere_AP" 802-11-wireless-security.pmf 1
```

This change was introduced during troubleshooting of wireless connection timeouts. :contentReference[oaicite:6]{index=6}

---

# 20. Virtual Interface MAC Address

A cloned MAC address was configured for the virtual interface:

```bash
sudo nmcli connection modify "Himbeere_AP" 802-11-wireless.cloned-mac-address 12:34:56:78:9A:BC
```

This was part of the configuration used to avoid conflicts between the physical and virtual wireless interfaces.

---

# 21. Enabling the Configuration at Boot

After creating the service and NetworkManager profile, the `systemd` configuration was reloaded:

```bash
sudo systemctl daemon-reload
```

The `uap0` service was enabled:

```bash
sudo systemctl enable uap0.service
```

Finally, the Raspberry Pi was restarted:

```bash
sudo reboot
```

This allows the virtual wireless interface to be recreated automatically during the boot process. :contentReference[oaicite:7]{index=7}

---

# 22. Network Architecture Implemented

The resulting configuration can be summarized as:

```text
                 Raspberry Pi Zero 2 W
                         │
                       wlan0
                         │
                Wi-Fi Station Connection
                         │
                Existing Wi-Fi Network


                 Raspberry Pi Zero 2 W
                         │
                       uap0
                         │
                  Wi-Fi Access Point
                         │
                    "Himbeere"
                         │
                  Local Client Device
```

The physical Wi-Fi hardware is therefore used together with a virtual interface to prepare simultaneous Station and Access Point operation.

---

# 23. Tools Used for the Network Configuration

The wireless configuration uses:

```text
iw
systemd
NetworkManager
nmcli
```

Their roles in the implemented setup are:

| Tool | Use |
|------|-----|
| `iw` | Creation and inspection of wireless interfaces |
| `systemd` | Persistent creation of `uap0` during boot |
| `NetworkManager` | Network connection management |
| `nmcli` | Command-line configuration of NetworkManager |

---

# 24. Work Performed So Far

The following Raspberry Pi work has been documented as performed:

- Raspberry Pi environment prepared.
- Required system packages installed.
- OpenCV installed.
- pymavlink installed.
- DroneKit installed.
- MAVSDK installed.
- MAVProxy installed.
- Camera-related system packages installed.
- Storage-space problem investigated.
- Root filesystem expanded.
- pip cache cleaned.
- APT cache cleaned.
- Temporary package installation directory moved to `/var/tmp`.
- DroneKit Python compatibility patch implemented.
- MAVSDK backend initialization prepared.
- UDP port `14550` used in the MAVSDK initialization.
- Physical Wi-Fi channel checked.
- Virtual `uap0` interface configured.
- Persistent `systemd` service created.
- NetworkManager Access Point profile created.
- Access Point mode configured.
- WPA-PSK configured.
- `uap0` assigned to the Access Point profile.
- PMF configuration adjusted.
- Separate MAC address configured.
- Automatic startup configuration enabled.

---

# 25. Current Problem

Although significant progress has been made on the Raspberry Pi environment and network configuration, communication with the Raspberry Pi remains one of the current project challenges.

The project development log explicitly records:

```text
Pi-Verbindung / Kommunikation mit dem Raspberry Pi
```

as an area with larger remaining problems.

Therefore, the Raspberry Pi integration must not yet be considered fully completed.

The operating environment and network configuration have been prepared, but integration with the complete drone system is still ongoing.

---

# 26. Current Status

The current Raspberry Pi status can be summarized as follows:

| Task | Status |
|------|--------|
| Raspberry Pi environment | Implemented |
| Storage preparation | Implemented |
| Required Python packages | Installed |
| DroneKit compatibility patch | Implemented |
| MAVSDK initialization | Prepared |
| `uap0` virtual interface | Configured |
| Access Point profile | Configured |
| Persistent network startup | Configured |
| Complete Pi-to-drone communication | Still in progress |

The next work on this part of the project depends on resolving the remaining communication problems and testing the Raspberry Pi together with the complete drone system.