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
