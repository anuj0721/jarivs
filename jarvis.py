import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
from twilio.rest import Client
from pytube import YouTube

engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')

engine.setProperty('voice',voices [0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait() 

def sendEmail(to , contents):    
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('anujgupta0721@gmail.com','9560430478')
    server.sendmail('anujgupta0721@gmail.com',to,content)
    server.close()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning anuj!")

    elif hour>=12 and hour<18:
        speak("good afternoon anuj!")

    else:
        speak("good evening anuj!")

    speak("i m jarvis. please tell me how may I help you")

def takeCommand():
    '''it takes microphone input from user and returns string output'''
    
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold=1
        r.adjust_for_ambient_noise(source,duration=5)
        audio = r.listen(source)    
        
    try:
        print("recognizing..")
        query=r.recognize_google(audio, language='en-in')
        print(f"user said:{query}\n")
    
    
    except Exception as e:
        #print(e)
        print("say that again please...")
        return "none"
    return query

if __name__ == "__main__" :
    
    chrome_path='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s' 
    myvideo=YouTube("https://www.youtube.com/watch?v=5MgBikgcWnY")
    print(sr.__version__)
    wishMe()
   
    if True:
        query=takeCommand().lower()
        #query='open google'
        #logic for executing task based on query
        if 'wikipedia' in query:
            speak('searching wikipedia..')
            query=query.replace('wikipedia','')
            results=wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            url="youtube.com"
            webbrowser.get(chrome_path).open(url)

        elif 'open google' in query:
            url="google.com"
            webbrowser.get(chrome_path).open(url)

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            
        elif 'send email' in query:
            speak("what should i say")
            content='send this email to anuj gupta to check code'
            to='anujgupta0721@gmail.com'
            sendEmail(to,content)
            speak("email has been sent ")

        elif 'message' in query:
            client=Client()
            from_whatsapp_number='whatsapp:+918109813801'
            to_whatsapp_number='whatsapp:+919009849949'
            client.messages.create(body="checking program!",from_=from_whatsapp_number,to=to_whatsapp_number)
            speak("whatsapp message has been sent")

        elif 'open netflix' in query:
            webbrowser.open("netflix.com")

        elif 'title' in query:
           print(myvideo.title)

        elif 'views' in query:
            print(myvideo.views)
