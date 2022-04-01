#Libraries


import speech_recognition as sr

import pyttsx3
import datetime

import wikipedia

import webbrowser
import os
import time

import subprocess

import wolframalpha

import json

import requests

import sys
import random

import pyglet

import argparse

import py2exe
import translator
import pandas as pd

import googletrans

import goslate
print ("******************************* HORTSENS AI ASSISTANT ******************************")
time.sleep(1) 
print('')
time.sleep(1)
print('**       **      *******    **********    **********   ********    ******    ***         **   ********       ')
time.sleep(1)
print('**       **     **     **   **        *   **********   **          *         **  *       **   *      ')
time.sleep(1)
print('***********     **     **   **        *       **       ********    *****     **   *      **   ******** ')
time.sleep(1)
print('***********     **     **   *********         **       ********    *****     **     *    **   ******** ')
time.sleep(1)
print('**       **     **     **   **       *        **             **    *         **       *  **         **')
time.sleep(1)
print('**       **      *******    **        *       **       ********    ******    **         ***   ********       ')
time.sleep(1)
print('')
#pyttsx3 setup


engine=pyttsx3.init('sapi5')

new_vol = .5 

engine.setProperty("volume", .50)


def speak(text):

    engine.say(text)

    engine.runAndWait()

def wishMe():

    hour=datetime.datetime.now().hour

    if hour>=0 and hour<12:

        print("Good morning.")
        speak("Good morning.")
    elif hour>=12 and hour<18:

        print("Good afternoon.")
        speak("Good afternoon.")
    else:

        print("Good evening.")
        speak("Good evening.")
        
    time.sleep(1)

def takeCommand():

    r=sr.Recognizer()

    with sr.Microphone() as source:

        print("I'm listening...")

        audio=r.listen(source)
        

        # speech recognition setup   

        try:

            statement=r.recognize_google(audio,language='en-en')
            statement=r.recognize_google(audio,language='fr-fr')
            print(f"I heard :{statement}\n")


        except Exception as e:

            speak("Forgive me, but I didn't hear what you said.")

            return "None"
        return statement


print("Wait a while...")

time.sleep(2)
jls_extract_var = wishMe
jls_extract_var()

if __name__=='__main__':
    

    while True:

        speak("What can I do for you today ?")
        print("What can I do for you today ?")
        time.sleep(2)

        statement = takeCommand().lower()

        if statement==0:
            continue
        
        

        #ENGLISH STATEMENTS

        if "hello" in statement:

            speak("Hi, I will be delighted to help you")

            print("Hi, I will be delighted to help you")

        if "good evening" in statement:

            speak('Good evening')

            print('Good evening')

        if "good afternoon" in statement:

            speak("good afternoon")

            print("Good afternoon")
            
        if "is your dream" in statement:
            speak("my only dream is to serve you, but. I guess my other dream is to make you happy")

        if "good morning" in statement:

            speak("good morning")

            print("Good morning")

        if "how are you" in statement:

            speak("I'm doing well, thanks")

        if "what's your name" in statement:

            speak("My name is HortSens Assistant, and I love helping you in your life with technology")

            print("My name is HortSens Assistant, and I love helping you in your life with technology")

        if "what can you do" in statement:

            speak("I can search the internet, talk with you if you want, tell you the time. Let you know the weather and daily news, I can randomly choose heads or tails, rap, and much more.")

            print("I can search the internet, talk with you if you want, tell you the time. Let you know the weather and daily news, I can randomly choose heads or tails, rap, and much more.")
        
        if "siri" in statement:
            speak("Siri is my hero, I hope one day I will be like one of the best vocal assistant in the world")
            print("Siri is my hero, I hope one day I will be like one of the best vocal assistant in the world")
        
        if "repeat" in statement:
            speak(statement)
            
        if "say" in statement:
            speak(statement)
                        
        if "you are cool" in statement or "you are top" in statement or "you're the best" in statement or "you are the best" in statement:
    
            speak("Oh thank you so much, you make me blush, but I have no cheeks")

            print("🥰")
            
        if "bye" in statement or "ok bye" in statement or "good bye" in statement:

            speak('See you soon, I hope')

            print('Good bye')

            break

        if "play music" in statement or "music" in statement:
            speak('okay.    Be ready for the most epic music you will hear ')
            pygame.mixer.init()
            pygame.mixer.music.load('music.mp3')
            pygame.mixer.music.play()
            time.sleep(27)
            speak('so, what do you thing ?')
            
        if 'wiki' in statement:

            statement =statement.replace("wikipédia", "")

            results = wikipedia.summary(statement, sentences=3)

            speak("I am according with wikipedia")
            print(results)

            speak(results)

        if "news" in statement or "info" in statement or "information" in statement or "what's the news of the day" in statement or "what are today's news" in statement or "what's today's news" in statement or "what is today's news" in statement:

            news = webbrowser.open_new_tab("https://news.google.com/topstories?hl=fr&gl=MA&ceid=MA:fr")

            speak('here are news from google news')

            time.sleep(5)

        elif "open calculator" in statement:

            subprocess.run('calc.exe')

            speak('calculator is opened now')

            time.sleep(5)

        elif 'Google' in statement or 'open google' in statement:

            webbrowser.open("www.google.com")

            speak("google is opened, have fun")

            time.sleep(5)

        elif 'open youtube' in statement:

            webbrowser.open("www.youtube.com")

            speak("YouTube is opened good viewing")

        elif 'open mail' in statement or 'mail' in statement or "mail" in statement or 'open gmail' in statement:

            webbrowser.open_new_tab("gmail.com")

            speak("Google Mail is opened now")

            time.sleep(5)

        elif 'what time is it' in statement or 'time' in statement:

            strTime=datetime.datetime.now().strftime("%H:%M:%S")

            speak(f" {strTime}")

        elif "search" in statement:

            statement = statement.replace("search", "")

            webbrowser.open_new_tab(statement.replace("search", ""))

            speak("here is the information I found in the web")

            time.sleep(5)

        if "who are you" in statement or "what are you" in statement:

            speak("I'm afraid of speeches but it's my duty to introduce myself, .. So .... I am an assistant created by IMG Hortsens Technologie ... it was Adam Boukhare who designed me. and I hope to serve you as I should. I can read, speak, and listen .... it is thanks to these three senses that I can perceive a small part of the outside world ..... I can look up information for you on the internet. tell you what time it is, and also today's information. do not hesitate to speak to me so that I do anything to you. So ... what do you want me to do for you first. Ooooh! and I am sorry for my somewhat neutral robot view, this may change in a future update where I will be more friendly. So ... Tadaa")

        if "rap me" in statement or "rap" in statement:

            speak("Yolo                        Life is good   yolo                            you            the researcher   of information       I'll help you     to find them    because me           you      assis    tant       i'm helping you         with technology yeah")

        if "birthay" in statement or "today is my birthday" in statement or "it's my birthday" in statement or "it is my birthday" in statement:

            speak("Ooh happy birthday and I think I prepped a gift, hold this gift emoji")

            print("🎁")
 
        if "stop" in statement:

                break

        if "wait" in statement:

            speak('ok')

            time.sleep(5)

        if "I have a question" in statement or "question" in statement:

            speak("what question do you want to ask me?")

            question=takeCommand()

            app_id="KH8L8U-RY6VU98U5J"

            client = wolframalpha.Client('R2K75H-7ELALHR35X')

            res = client.query(question)

            answer = next(res.results).text

            speak(answer)

            print(answer)

        elif "what's your name" in statement:

            speak("My name is HortSense Assistant, I am your personal assistant, consider me as a friend")

            print("My name is HortSense Assistant, I am your personal assistant, consider me as a friend")

        elif "who created you" in statement or "who invented you" in statement:

            speak("I was created by Adam Boukhare from IMG. HortSens Technologies. , without him, I couldn't be here to help you")

            print("I was created by IMG. Pictures Technologies.")      

        elif "weather" in statement or "what is today's weather " in statement or "what are the meteorological data" in statement or "what weather is it today" in statement or "what is the weater of today" in statement or "what's the weater of today" in statement:

            statement = statement.replace("weather", "")

            webbrowser.open_new_tab("https://weather.com/en-US/temps/aujour/l/MOXX0007:1:MO?Goto=Redirected")

            speak("Here is the weather forecast today from weather dot com")

            time.sleep(5)
        
        elif "Flip or Flop" in statement:
            
            piece=random.raandint(1,2)
            
            if piece == 1:
                speak("maybee.  Flip")
                print("maybe... Flip")
            if piece == 2:
                
                speak("maybee.  Flop")
                print("maybe... Flop")                
        elif "heads or tails" in statement:

            piece=random.randint(1,2)

            if piece == 1:

                speak("maybe   heads")

            if piece == 2:

                speak("maybe   tails")
                
        elif "tell me something" in statement or "something" in statement or "tell me" in statement or "tell" in statement or "story" in statement:
            speak("Hum.   Oh yes, do you know the story of the pirate who went in a deserted islend ?.     Well, he still there")
        
        elif "game" in statement:
            speak("Ok, but in the actual version, there is no games to play, but make sure that it will be in a future update")

        elif "1 + 1" in statement:

            speak("2")
            print("The result is 2")

        elif "in which language you are created" in statement or "in what language are you created" in statement or "in wich programming language are you created" in statement or "in what programming language are you created" in statement or "in wich language" in statement or "which language you are created" in statement or "in wich language are you programmed" in statement :

            speak("i am programmed in python. Do you want me to inform you more about this computer language?")                  

        elif "turn off" in statement or "disconnect my device" in statement or "ferme mon pc" in statement or "turn off my pc" in statement:

            speak("Ok your computer will shut down in 10 seconds, make sure you have closed all windows")

            subprocess.call(["shutdown;", "/l"])

        time.sleep(3)

