import speech_recognition as sr
import pyttsx3
import json

# Load book data
with open("books.json") as f:
    books = json.load(f)

# Initialize recognizer and text-to-speech
r = sr.Recognizer()
engine = pyttsx3.init()

engine.say("Say the name of the book you want to search for.")
engine.runAndWait()

with sr.Microphone() as source:
    print("Listening...")
    audio = r.listen(source)

try:
    text = r.recognize_google(audio)
    print(f"You said: {text}")

    found = False
    for book in books:
        if text.lower() in book["title"].lower():
            engine.say(f"{book['title']} by {book['author']} is available.")
            found = True
            break

    if not found:
        engine.say(f"Sorry, {text} is not in the library.")
    engine.runAndWait()

except sr.UnknownValueError:
    print("Could not understand audio.")
except sr.RequestError:
    print("Error with speech recognition service.")

