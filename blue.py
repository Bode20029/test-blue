import asyncio
from bleak import BleakScanner, BleakClient

async def find_and_connect_to_speaker():
    print("Scanning for devices...")
    devices = await BleakScanner.discover()
    
    speaker_device = None
    for d in devices:
        print(f"Found device: {d.name}")
        if "Speaker" in d.name:  # Adjust this condition based on your speaker's name
            speaker_device = d
            break
    
    if speaker_device:
        print(f"Attempting to connect to {speaker_device.name}")
        async with BleakClient(speaker_device.address) as client:
            if client.is_connected:
                print(f"Connected to {speaker_device.name}")
                # Perform operations with the connected speaker here
            else:
                print(f"Failed to connect to {speaker_device.name}")
    else:
        print("No suitable speaker found")

asyncio.run(find_and_connect_to_speaker())