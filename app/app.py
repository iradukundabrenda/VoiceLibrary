import json
import time
import speech_recognition as sr
import pyttsx3

# Initialize speech recognition and text-to-speech
r = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

def listen():
    # Use built-in microphone (change device_index if needed)
    try:
        with sr.Microphone() as source:
            print("Listening...")
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source, timeout=10, phrase_time_limit=10)
            command = r.recognize_google(audio)
            print("You said:", command)
            return command.lower()
    except sr.WaitTimeoutError:
        speak("I didn't hear anything. Please try again.")
        return None
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return None
    except sr.RequestError:
        speak("Sorry, speech service is unavailable.")
        return None

def find_book(command):
    # Load books from JSON
    with open("books.json", "r") as f:
        books = json.load(f)
    command_words = command.lower().split()
    for book in books:
        title_words = book["title"].lower().split()
        # Check if all words in title are in the command
        if all(word in command_words for word in title_words):
            return book
    return None

if __name__ == "__main__":
    speak("Welcome to Voice Library.")
    while True:
        speak("Which book would you like to borrow? Say 'exit', 'quit', or 'bye' to quit.")
        time.sleep(1)
        command = listen()
        if not command:
            continue
        if any(word in command for word in ["exit", "quit", "bye"]):
            speak("Goodbye!")
            break
        book = find_book(command)
        if book:
            speak(f"{book['title']} is available. Book borrowed successfully!")
        else:
            speak("Sorry, that book is not available.")
        time.sleep(1)

