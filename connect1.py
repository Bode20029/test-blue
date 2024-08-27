import asyncio
from bleak import BleakScanner, BleakClient

async def find_and_connect_to_device():
    print("Scanning for devices...")
    devices = await BleakScanner.discover()
    for d in devices:
        print(f"Found device: {d.name or 'Unknown'}, Address: {d.address}")
        if d.address == "17:24:c5:14:b8:c4":
            print(f"Found JBL Go 2, attempting to connect...")
            async with BleakClient(d.address) as client:
                if client.is_connected:
                    print(f"Connected to JBL Go 2")
                    # Perform operations with the connected device here
                else:
                    print(f"Failed to connect to JBL Go 2")
            return
    print("JBL Go 2 not found during scan")

asyncio.run(find_and_connect_to_device())