import sounddevice as sd
import wave
import numpy as np

print("Recording for 5 seconds... speak now!")
fs = 44100  # Higher sample rate
recording = sd.rec(int(5 * fs), samplerate=fs, channels=2, dtype='float32')
sd.wait()
print("Done!")

# Convert and save
audio = (recording * 32767).astype(np.int16)
with wave.open('test2.wav', 'w') as f:
    f.setnchannels(2)
    f.setsampwidth(2)
    f.setframerate(fs)
    f.writeframes(audio.tobytes())

print("Saved test2.wav - play it!")