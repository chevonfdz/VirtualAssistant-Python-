import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speaking(text):
    # print("check speaking")
    engine.say(text)
    engine.runAndWait()


def takeCommand():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'hello alexa' in command:
                speaking('Hello chevon... what can i do for you?')
                # print("Check after speaking function")
            elif 'alexa' in command:
                command = command.replace('alexa', '')

    except:
        pass
    return command


def running():
    command = takeCommand()
    # print("Check running")
    # print(command)
    if 'play' in command:
        song = command.replace('play', '')
        speaking('playing' + song)
        print('playing')
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M %p')
        print(time)
        speaking('Current time is ' + time)

    elif 'date' in command:
        from datetime import date
        today = date.today()
        print("Today's date is ", today)

    elif 'what' or 'who' or 'when' or 'why' or 'which' or 'where' or 'whose' in command:
        question = command
        info = wikipedia.summary(question, 2)
        print(info)
        speaking(info)

    elif 'how to' in command:
        question = command
        info = wikipedia.summary


while True:
    running()
