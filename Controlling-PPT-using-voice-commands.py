import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install SpeechRecognition
import os
import keyboard
import datetime


engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=6 and hour<12:
        speak("Good Morning Mr AbdulBasit")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Mr AbdulBasit")

    elif hour>=18 and hour<24:
        speak("Good Evening Mr AbdulBasit")

    else:
        speak("Good Night Mr AbdulBasit")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"Mr Robo Said:{query}\n")

    except Exception as e:
        print(e)
        print("Say that again Please...")
        speak("Say that again Please...")
        return "None"
    return query

def takeCommand1():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"Mr Robo Said:{query}\n")

    except Exception as e:
        print(e)
        print("Say that again Please...")
        return "None"
    return query

def controlPpt():
    speak("Controlling PPT Presentation")
    while True:
        query1 = takeCommand1().lower()

        if 'start' in query1:
            keyboard.send('F5')
             
        elif 'next' in query1:
            keyboard.send('space')
        
        elif 'previous' in query1:
            keyboard.send('backspace')

        elif 'stop' in query1:
            keyboard.send('escape')

        elif 'quit' in query1:
            speak("Quitting the program")
            quit()

        elif 'close' in query1:
            speak("Stopping the control of PPT presentation")
            speak("Closing PPT presentation ")
            os.system("TASKKILL /F /IM POWERPNT.exe")
            return "None"
            

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'ppt' in query:
            controlPpt()

        elif 'quit' in query:
            speak("Quitting the program")
            quit()

        