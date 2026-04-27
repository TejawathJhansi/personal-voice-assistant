import datetime
import webbrowser
import os

def handle(command, speak):

    # Greet
    if "hello" in command or "hi" in command:
        speak("Hello! How can I help you?")

    # Tell time
    elif "time" in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {now}")

    # Search web
    elif "search" in command:
        query = command.replace("search", "").strip()
        webbrowser.open(f"https://google.com/search?q={query}")
        speak(f"Searching for {query}")

    # Open YouTube
    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube")

    # Open Google
    elif "open google" in command:
        webbrowser.open("https://google.com")
        speak("Opening Google")

    # Open Notepad
    elif "open notepad" in command:
        os.system("notepad")
        speak("Opening Notepad")

    # Tell date
    elif "date" in command:
        today = datetime.datetime.now().strftime("%B %d, %Y")
        speak(f"Today is {today}")

    # Stop assistant
    elif "stop" in command or "exit" in command or "bye" in command:
        speak("Goodbye! Have a great day!")
        return False

    # Unknown command
    else:
        speak("Sorry, I didn't understand. Please try again.")

    return True