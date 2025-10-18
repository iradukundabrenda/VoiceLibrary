import speech_recognition as sr
import pyttsx3

# Initialize recognizer and text-to-speech engine
r = sr.Recognizer()
engine = pyttsx3.init()

# Capture audio from the microphone
with sr.Microphone() as source:
    print("Say something:")
    audio = r.listen(source)

# Recognize speech using Google Web Speech API
try:
    text = r.recognize_google(audio)
    print("You said:", text)
    engine.say(f"You said: {text}")
    engine.runAndWait()
except sr.UnknownValueError:
    print("Sorry, I could not understand the audio.")
except sr.RequestError:
    print("Could not request results from Google Speech Recognition service.")

