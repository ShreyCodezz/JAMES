import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import pyautogui
import pyjokes
import pywhatkit
from PyDictionary import PyDictionary as Dict
from playsound import playsound
from gui import play_gif
import random


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Sarge Sir. Please tell me how may I help you")

def takeCommand():  
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:  
        print("Say that again please...")  
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:

        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'youtube' in query:
            webbrowser.open("youtube.com")

        elif 'google' in query:
            webbrowser.open("www.google.com")

        elif 'stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   
            
        elif 'music' and 'song' in query:
            speak("Sir, Which song should i play for you?")
            song = takeCommand()
            pywhatkit.playonyt(song)
            speak("Sir,your song has been started")
            

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = r'C:\Users\91987\AppData\Local\Programs\Microsoft VS Code\Code.exe'
            os.startfile(codePath)
            
        elif 'anime' in query:
            webbrowser.open("aniwatch.tv")

        elif 'instagram' in query:
            webbrowser.open("instagram.com") 
        

            
        elif 'bored' and 'joke' in query:
            speak("Sir, what can i do for you?")
            
            if 'joke' in query:
                joke = pyjokes.get_joke()
                speak(joke)
            
            if 'music' or 'song' in query:
                speak("Sir, Which song should i play for you?")
                song = takeCommand()
                pywhatkit.playonyt(song)
                speak("Sir,your song has been started")