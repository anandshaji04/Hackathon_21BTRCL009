import pyttsx3 as p  # Import the pyttsx3 library and alias it as p
import speech_recognition as sr  # Import the speech_recognition library and alias it as sr
from selenium_web import YahooSearch
from music import YoutubeSearch

engine = p.init()  # Initialize the pyttsx3 engine
rate = engine.getProperty('rate')  # Get the current speaking rate
engine.setProperty('rate',140)  
voices = engine.getProperty('voices')  
engine.setProperty('voice', voices[1].id)
def speak(text):
    engine.say(text)  # Queue the text "Hello World" to be spoken
    engine.runAndWait()  # Process the voice commands and wait for them to complete

r=sr.Recognizer()
speak("Hello I am your voice assistant, how are you?")

with sr.Microphone() as source:
    print("Listening...")
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source)
    audio=r.listen(source,10)
    print("Processing...")
    try:
        text=r.recognize_google(audio)
        print("You said: {}".format(text))
    except:
        print("Sorry, I did not get that.")

if "what" and "about" and "you" in text:
    speak("I am doing great, thank you for asking.")

speak("What can I do for you?")

with sr.Microphone() as source:
    print("Listening...")
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source)
    audio=r.listen(source,10)
    text2=r.recognize_google(audio)

if "information" in text2:
    speak("What information do you need?")
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold=10000
        r.adjust_for_ambient_noise(source)
        audio=r.listen(source,10)
        text3=r.recognize_google(audio)
    speak("Searching for information on yahoo on {}".format(text3))
    YahooSearch(text3)

elif "music" or "song" or "play" or "video" in text3:
    speak("What song would you like to listen to?")
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold=10000
        r.adjust_for_ambient_noise(source)
        audio=r.listen(source,10)
        text4=r.recognize_google(audio)
    speak("Playing {} on youtube".format(text4))
    YoutubeSearch(text4)
