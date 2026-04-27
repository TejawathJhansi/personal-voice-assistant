import sounddevice as sd
import numpy as np

devices = sd.query_devices()
input_devices = [(i, d) for i, d in enumerate(devices) if d['max_input_channels'] > 0]

for idx, dev in input_devices:
    try:
        print(f"Testing device {idx}: {dev['name']} - speak now...")
        rec = sd.rec(int(2 * 16000), samplerate=16000, channels=1, dtype='int16', device=idx)
        sd.wait()
        vol = np.abs(rec).mean()
        print(f"  Volume: {vol:.4f}")
    except Exception as e:
        print(f"  Error: {e}")