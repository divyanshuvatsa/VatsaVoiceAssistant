import os
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    '''This Function will program your Vatsa to speak something.'''
    engine.say(audio)
    engine.runAndWait

def greet():
    '''his Function will make your Vatsa greet you according to system time.'''
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning, Sir!")

    elif hour>=12 and hour<=17:
        speak("Good Afternoon, Sir!")

    else:
        speak("Good Evening, Sir!")

    speak("Your trusty assistant Vatsa, at your service. How may I help you?")

def micInput():
    '''This Function will allow your Vatsa to take microphone input from the user and returns a string output.'''
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
        print("Say that again, please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('dv4710@srmist.edu.in', 'my-password')
    server.sendmail('dv4710@srmist.edu.in', to, content)
    server.close()


  
if __name__ == "__main__":
    greet()
    while True:
       query = micInput().lower()

       if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia, """)
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia, ")
            print(results)
            speak(results)

       elif 'open youtube' in query:
            speak("Opening YouTube...")
            webbrowser.open("youtube.com")
       elif 'open google' in query:
            speak("Opening Google...")
            webbrowser.open("google.com")
       elif 'open facebook' in query:
            speak("Opening Facebook...")
            webbrowser.open("facebook.com")
       elif 'open instagram' in query:
            speak("Opening Instagram...")
            webbrowser.open("instagram.com")
       elif 'open stackoverflow' in query:
            speak("Opening StackOverflow...")
            webbrowser.open("stackoverflow.com")

       elif 'play music' in query:
            music_dir = "D:\\Songs"
            songs = os.listdir(music_dir)
            print(songs)
            n = random.randint(0, len(songs))
            os.startfile(os.path.join(music_dir, songs[n]))

       elif 'the time' in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the current time is {time}")

       elif 'email to divyanshu' in query:
            try:
              speak("What should I say?")
              content = micInput()
              to = "diyanshuvatsa7@gmail.com"
              sendEmail = (to, content)
              speak("Your email has successfully been sent, sir.")
            
            except Exception as e:
                speak("I am unable to send the email at the moment.")

       elif 'quit' in query:
            exit()







