import pyttsx3

engine = pyttsx3.init()

# Set voice properties
engine.setProperty('rate', 150)    # Speed (150 = normal)
engine.setProperty('volume', 1.0)  # Volume (0.0 to 1.0)

# Optional: Set voice to female (index 1) or male (index 0)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Change 0 to 1 for female voice

def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()