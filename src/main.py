import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from listener import listen
from speaker import speak
from commands import handle

def main():
    speak("Hello! Voice assistant is ready. How can I help you?")
    
    running = True
    while running:
        command = listen()
        if command:
            running = handle(command, speak)

if __name__ == "__main__":
    main()