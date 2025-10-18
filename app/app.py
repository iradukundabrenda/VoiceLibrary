import speech_recognition as sr
import pyttsx3
import json

engine = pyttsx3.init()
r = sr.Recognizer()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio)
            print("You said:", command)
            return command.lower()
        except:
            speak("Sorry, I didn't catch that.")
            return None

def find_book(title):
    with open('books.json') as f:
        books = json.load(f)
    for book in books:
        if title.lower() in book["title"].lower():
            return book
    return None

if __name__ == "__main__":
    speak("Welcome to Voice Library. What book would you like to borrow?")
    command = listen()
    if command:
        book = find_book(command)
        if book:
            speak(f"{book['title']} is available. Would you like to borrow it?")
        else:
            speak("Sorry, that book is not available.")

