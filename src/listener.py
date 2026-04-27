import speech_recognition as sr
import sounddevice as sd
import numpy as np
import io
import wave

DEVICE_INDEX = 2
SAMPLE_RATE = 44100
CHANNELS = 1
DURATION = 6

def listen():
    r = sr.Recognizer()
    print("Listening... Speak now!")

    audio_float = sd.rec(
        int(DURATION * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=CHANNELS,
        dtype='float32',
        device=DEVICE_INDEX
    )
    sd.wait()

    # Convert to int16
    audio_int16 = (audio_float.flatten() * 32767).astype(np.int16)

    # Resample from 44100 to 16000 for Google Speech API
    new_length = int(len(audio_int16) * 16000 / SAMPLE_RATE)
    resampled = np.interp(
        np.linspace(0, len(audio_int16), new_length),
        np.arange(len(audio_int16)),
        audio_int16
    ).astype(np.int16)

    wav_buffer = io.BytesIO()
    with wave.open(wav_buffer, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(16000)
        wf.writeframes(resampled.tobytes())
    wav_buffer.seek(0)

    try:
        with sr.AudioFile(wav_buffer) as source:
            audio = r.record(source)
            command = r.recognize_google(audio, language="en-IN")
            print(f"You said: {command}")
            return command.lower()
    except sr.UnknownValueError:
        print("Could not understand. Try again.")
        return ""
    except sr.RequestError as e:
        print(f"Internet error: {e}")
        return ""
    except Exception as e:
        print(f"Error: {e}")
        return ""