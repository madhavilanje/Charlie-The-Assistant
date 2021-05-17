import pyttsx3      #text to speech conversion library
import speech_recognition as sr
import datetime                                   ##############################
import wikipedia                                  ######### Some modules #######
import webbrowser                                 ##############################
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning..!")
    elif hour == 12:
        speak("Good Noon..!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon..!")
    else:
        speak("Good Evening..!")
    speak("I am CHARLIE ma'am. Please tell me how may I help you.")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        speak("Sorry..! Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('madhavilanje9623@gmail.com','gmail@76204201')
    server.sendmail('madhavilanje9623@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        #logic for tasks

        if 'wikipedia'in query:                 #to search through wikipedia
            speak("Searching wikipedia...")
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query,sentences = 2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'who are you' in query:
            speak("I am CHARLIE and I am here to help you.")

        elif 'work time' in query:              #to open any file
            path = "D:\\Work"
            os.startfile(path)
            speak("OK...")
        elif 'open youtube' in query:               #to open youtube
            webbrowser.open("youtube.com")
            speak("OK.. Opening youtube")
        elif 'open whatsapp' in query:                      #to open whatsApp
            webbrowser.open("web.whatsapp.com")  
            speak("OK.. Opening whatsApp") 
        elif 'open google' in query:                        #to open google search
            webbrowser.open("google.com")  
            speak("OK.. Opening google") 
        elif 'play music' in query:                     #to play music
            webbrowser.open("gaana.com")  
            speak("OK.. Playing music for you ma'am") 
        elif 'the time' in query:                                   #to know time
            strTime = datetime.datetime.now().strftime("%H.%M.%S")
            speak(f"Ma'am, the time is {strTime}")
        elif 'open code' in query:                              #to open vs code                
            codePath = "C:\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            speak("OK... Opening VS code")
        elif 'send an email' in query:                          #to send an email
            try:
                speak("What should I say..?")
                content = takeCommand()
                to = "lanje_madhavi.cs@ghrce.raisoni.net"
                sendEmail(to,content)
                speak('email has been sent')
            except Exception as e:                              #for errors
                    print(e)
                    speak("Sorry ma'am... I am not able to send this email at this moment ")
        elif 'shut up' in query:                                 #exit
            speak("Ok ma'am... Hope, I was able to help you. Have a nice day.")
            exit()
   