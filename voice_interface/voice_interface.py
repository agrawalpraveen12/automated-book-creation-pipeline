import pyttsx3
import speech_recognition as sr
import os

# Path to final chapter file
chapter_path = "../output/chapter1_review.txt"

# Load the content to be spoken
if os.path.exists(chapter_path):
    with open(chapter_path, 'r', encoding='utf-8') as f:
        text = f.read()
else:
    print("❌ Chapter file not found!")
    exit()

# Text-to-speech setup
engine = pyttsx3.init()
engine.setProperty('rate', 150)

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Voice command listener
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Say something...")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        return command.lower()
    except sr.UnknownValueError:
        return "Could not understand"
    except sr.RequestError:
        return "API unavailable"

# Run
print("✅ Voice interface started! Say 'read chapter'")
command = listen()
if "read" in command or "chapter" in command:
    print("🔊 Reading...")
    speak(text)
else:
    print("🤖 Unrecognized command.")
