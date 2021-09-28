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
from distutils.core import setup
import random
import googletrans
import pyglet
import argparse
import py2exe
try     :

    import win32gui, win32con;

    frgrnd_wndw = win32gui.GetForegroundWindow();
    wndw_title  = win32gui.GetWindowText(frgrnd_wndw);
    if wndw_title.endswith("python.exe"):
        win32gui.ShowWindow(frgrnd_wndw, win32con.SW_HIDE);
except  :
    pass
from gooey import Gooey, GooeyParser
@Gooey(language='french')
def main():
    softPath="/usr/bin/soft"
    parser = argparse.ArgumentParser(description="Clara Assistant est là pour vous !  Appuyez sur démmarer pour que je m'active 😉.")
    parser = argparse.ArgumentParser(description="Pour chercher du contenu sur Internet, dites seulement 'cherche-moi',  pour me poser des... questions de maths dites 'dis-moi',  puis vous pouvez me parler sur tout à votre guise😉")
    parser.parse_args()
 
main()



engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voice')
engine.setProperty('voice','voices[1].id')

def speak(text):
    engine.say(text)
    engine.runAndWait()
def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Bonjour")
        print("Bonjour.")
    elif hour>=12 and hour<18:
        speak("Salut")
        print("Salut.")
    else:
        speak("Bonsoir")
        print("Bonsoir.")
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("J'écoute...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='fr-fr')
            print(f"J'ai entendu:{statement}\n")

        except Exception as e:
            speak("Pardonnez moi, mais je n'ai pas entendu ce que vous aviez dit.")
            return "None"
        return statement

print("Préparation...")
speak("Je suis Ravi de vous voir")
wishMe()
if __name__=='__main__':
    

    while True:
        speak("Comment puis-je vous aider ?")
        statement = takeCommand().lower()
        if statement==0:
            continue
        if "salut" in statement or "bonjour" in statement:
            speak("Bonjour, je serai enchanté de vous aider")
            print("Bonjour, je serai enchanté de vous aider.")
        if "ello" in statement or "hello" in statement:
            speak("Hello, je suis ravie de vous aider")
            print("Hello, je suis ravi de vous aider")
        if "comment tu t'appelles" in statement:
            speak("Je m'appelle Clara Assistant, Clara comme je suis claire dans mes réponses  et assistant car j'aime vous aider.")
            print("Je m'appelle Clara Assistant, Clara comme je suis claire dans mes réponses  et assistant car j'aime vous aider.")
        if "dis-moi une blague" in statement:
            speak("Hi        Hi     Vous savez pourquoi les japonais n'ont pas de poney.....       Parce qu'ils sont déjaponé")
        if "tu es cool" in statement or "tu es top" in statement or "tu es la meilleur" in statement:
            speak("Oh merci beaucoup, vou me faites rougir, mais je n'ai pas de joues")
            print("🥰")
        if "au revoir" in statement or "ok bye" in statement or "stop" in statement:
            speak('A bientôt jéspère')
            print('A bientôt')
            break
        if 'wikipédia' in statement:
            speak('Je cherche votre requête sur Wikipedia...')
            statement =statement.replace("wikipédia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("Je m'ccording à Wikipedia")
            print(results)
            speak(results)
        if "nouvelle" in statement or "info" in statement or "information" in statement or "quel son les informations du jour" in statement:
            news = webbrowser.open_new_tab("https://news.google.com/topstories?hl=fr&gl=MA&ceid=MA:fr")
            speak('voilà les informations du jour provenant de Google News')
            time.sleep(6)
        elif "contrôle de vie" in statement or "contrôle V" in statement or "contrôle vie" in statement:
            webbrowser.open_new_tab("https://www.rcar.ma/fr/controlevie")
            speak("entrez votre numéro de pension pour savoir si vous êtes concernés")
        elif 'Google' in statement or 'ouvre google' in statement:
            webbrowser.open("www.google.com")
            speak("google est maintenant ouvert, amusez vous bien")
            time.sleep(5)
        elif 'ouvre gmail' in statement or 'gmail' in statement or "mail" in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail est maintenant ouvert")
            time.sleep(5)
        elif 'quelle heure est-il' in statement or 'heure' in statement or "l'heure" in statement or 'il est quelle heure' in statement or 'quelle heure il est' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"il est {strTime}")
        elif "cherche" in statement:
            statement = statement.replace("cherche", "")
            webbrowser.open_new_tab(statement.replace("cherche", ""))
            speak("voici les informations que j'ai trouvé dans le web")
            time.sleep(5)
        elif "traduit" in statement or "traduis" in statement or "traduis-moi" in statement:
            statement = statement.replace("traduit", "")
            webbrowser.open_new_tab(statement)
            speak(statement)
            time.sleep(3)
        if "qui es-tu" in statement or "que peux-tu faire " in statement:
            speak("J'ai bien peur des discours mais c'est mon devoir de me présenter,.. Donc... Oui. je suis un assistant créé par Hortsense Technologie... c'est Adam Boukhare qui m'a conçu. et j'éspère vous servir comme je le doit. je peux lire, parler, et écouter.... c'est grâce à ces trois sens que je peux percevoir une petite partie du monde extérieur..... je peux vous chercher des informations sur internet. vous dire l'heure qu'il est, et aussi les informations d'aujourd'hui. n'hésitez pas à me parler pour que je vous fasse quoi que se soit. Alors... que voulez vous que je fasse pour vous en premier.      Ooooh ! et je suis désolé pour ma vois de robot un peux neutre, ceci pourra changer dans une prochaine mise à jour ou je serai plus aimable. Donc...    Tadaa")
        if "rap moi" in statement or "rap" in statement or "fais-moi du rap" in statement:
            speak("Yolo                        La vie est belle   yolo                            toi qui cherche   des information       je t'aiderai    à les trouver    car moi       ton assistant jojo       je t'aide à faire         tes recherches yoyo")
        if "chante-moi une chanson" in statement or "joue-moi un morceau" in statement:
            speak('Je ne sais pas chanter, mais je sais vibrer le piano')
            music = pyglet.resource.media('Enregistrement.m4a')
            music.play()
            time.sleep(20)    
            speak("Pas la peine d'applaudire merci")     
            if "stop" in statement:
                break
            main()
        if "dis-moi" in statement or "donne-moi la réponse de cette question" in statement:
            speak("quelle question veux-tu me poser ?")
            question=takeCommand()
            app_id="KH8L8U-RY6VU98U5J"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)
        elif "comment tu t'appelles" in statement:
            speak("Je m'appelle Clara Assistant, de mon nom complet Clara Hortsense Assistant, je suis là pour vous facilité la vie avec la technologie")
            print("Je m'appelle Clara Assistant, de mon nom complet Clara Hortsense Assistant, je suis là pour vous facilité la vie avec la technologie.")
        elif "qui t'a créé" in statement or "qui t'ont créé" in statement or "qui t'a inventé" in statement or "quitte à inventer" in statement:
            speak("J'ai été créé par le merveilleux Adam Boukhare, sans lui, je ne pourrai être ici pour vous aider")
            print("J'ai été créé par Adam Boukhare")
        elif "ouvre-moi world" in statement:
            speak ("Ok, Microsoft Office word sera ouvert")
            projectpath = 'C:\Program Files (x86)\Microsoft Office\root\Office16\start WINWORD.EXE' 
 
            subprocess.check_output( ('start',projectpath) , shell=True )        
        elif "météo" in statement or "quelle est la météo" in statement or "quelles sont les données météorologiques" in statement:
            api_key="KH8L8U-RY6VU98U5J"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("De quelle ville voulez vous savoir la météo ?")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature en kelvin est " +
                      str(current_temperature) +
                      "\n le pourcentage d'humidité est " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print("  La temperature en kelvin = " +
                      str(current_temperature) +
                      "\n le pourcentage d'humidité (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))
        elif "pile ou face" in statement:
            piece=random.randint(1,2)
            if piece == 1:
                speak("pile")
            if piece == 2:
                speak("face")

        elif "éteins" in statement or "déconnecte mon appareil" in statement or "ferme mon pc" in statement or "éteins mon pc" in statement:
            speak("Ok , votre ordi s'éteindra dans 10 secondes, soyez sûr d'avoir fermé toutes les applications ")
            subprocess.call(["shutdown", "/l"])
time.sleep(3)

