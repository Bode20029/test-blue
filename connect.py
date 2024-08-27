import asyncio
from bleak import BleakClient

async def connect_to_device(address):
    async with BleakClient(address) as client:
        if client.is_connected:
            print(f"Connected to {address}")
            # Perform operations with the connected device here
        else:
            print(f"Failed to connect to {address}")

# Replace with the address you found
device_address = "64:68:76:52:ff:13"
asyncio.run(connect_to_device(device_address))