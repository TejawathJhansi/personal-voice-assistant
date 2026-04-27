import sounddevice as sd

devices = sd.query_devices()
print("INPUT DEVICES ONLY:")
for i, d in enumerate(devices):
    if d['max_input_channels'] > 0:
        print(f"Device {i}: {d['name']}")
        print(f"  Channels: {d['max_input_channels']}")
        print(f"  Sample rate: {d['default_samplerate']}")
        print()