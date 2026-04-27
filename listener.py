import speech_recognition as sr
import sounddevice

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... Speak now!")
        r.adjust_for_ambient_noise(source, duration=1)
        try:
            audio = r.listen(source, timeout=5)
            command = r.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.WaitTimeoutError:
            print("No speech detected.")
            return ""
        except sr.UnknownValueError:
            print("Could not understand. Try again.")
            return ""
        except sr.RequestError as e:
            print(f"Speech service error: {e}")
            return ""