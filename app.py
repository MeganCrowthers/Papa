## Remember to activate the virtual environment before running or installing new modules
## source Jarvis/bin/activate

import speech_recognition as sr
import pyttsx3
import random
from datetime import datetime
from decouple import config

USERNAME = config('BOTUSER')
BOTNAME = config('BOTNAME')
NICKNAMES = config('BOTNICKNAMES')
BOTNICKNAMES = ["Meggie", "Megs", "Megan", "Sugar tits"]

# Setting up text to speech
engine = pyttsx3.init()
engine.setProperty("rate", 178)
#engine.setProperty('voice', "english+f4")

# Initialize recognizer class (for recognizing the speech)
#r = sr.Recognizer()
#source = sr.Microphone()
#hot_word='Norbert'


def speak(text):
    engine.say(text)
    engine.runAndWait()


def greet_user():
    """Greets the user according to the time"""
    
    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        speak(f"Good Morning {USERNAME}")
    elif (hour >= 12) and (hour < 16):
        speak(f"Good afternoon {USERNAME}")
    elif (hour >= 16) and (hour < 19):
        speak(f"Good Evening {random.choice(BOTNICKNAMES)})")
    else:
        speak(f"You should be in bed.")

# datetime object containing current date and time
now = datetime.now()

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
time_string =now.strftime("%H:%M:%S")

RUNTIME = ["whats the time","dimmie da time","time"]

"""Greets the user through the terminal and awaits users input"""
greet_chat = input(f"How can I help you today {random.choice(BOTNICKNAMES)}:")
print("...")

if greet_chat.lower() in RUNTIME:
    print(f"The time is {time_string}")

#greet_user()


