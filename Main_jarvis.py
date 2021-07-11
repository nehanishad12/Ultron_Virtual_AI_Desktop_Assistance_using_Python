import pyttsx3 # pip install pyttsx3 #It is used to convert text to speech (module)
import speech_recognition as sr # pip install speechRecognition
import datetime
import wikipedia # pip install wikipedia
import webbrowser
import os
import smtplib # which defines an SMTP client session object that can be used to send mail to any Internet machine with an SMTPdaemon

print("Initializing Jarvis")

MASTER = "Neha"

engine = pyttsx3.init('sapi5') #sapi5 is a module
voices = engine.getProperty('voices') #getProperty
engine.setProperty('voice', voices[0].id) #setProperty (1=Female & 0=Male)

#speak function will pronouce the string which is passed to it
def speak(text):
    engine.say(text)
    engine.runAndWait()

# This function will wish you as per the current time
def wishMe():
    hour = int(datetime.datetime.now().hour) #int = integer

    if hour>=0 and hour<12:
        speak("Good Morning" + MASTER)
    
    if hour>=12 and hour<18:
        speak("Good Afternoon" + MASTER)

    else :
        speak("Good Evening" + MASTER)

    #speak("I am jarvis. How may I help you?")

# This function will take command from the microphone
def takeCommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print ("Listening...")
        audio=r.listen(source)
    
    try:
        print("Recognizing...")
        query =r.recognize_google(audio,language="en-in")
        print(f"User said:{query}\n")

    except Exception as e:
        print("Say that again please")
        query = "None"

    return query

# Main program starts here...

def main():
    speak("Initializing Jarvis...")
    wishMe()
    # takecommand()
    query = takeCommand()
# Logic for excecuting task

    if "wikipedia" in query.lower():
            speak('Searching wikipedia...')
            query= query.replace("wikipedia", "")
            results= wikipedia.summary(query,sentences=2)
            print(results)
            speak(results)

    elif 'open youtube' in query.lower():
            webbrowser.open("https://www.youtube.com/")

    elif 'open google' in query.lower():
            webbrowser.open("google.com")

    elif 'open stackoverflow' in query.lower():
            webbrowser.open("stackoverflow.com")

    elif 'open flipkart' in query.lower():
            speak('Opening Flipkart')
            webbrowser.open("https://www.flipkart.com/")

    elif 'open amazon' in query.lower():
            speak('Opening Amazon')
            webbrowser.open("https://www.amazon.in/ref=nav_logo")

    elif 'open google' in query.lower():
            speak('Opening Google')
            webbrowser.open("https://www.google.com/")   


    elif 'the time' in query.lower():
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

    elif 'thank you' in query.lower():
            speak(f"Your welcome {MASTER}")

    elif 'open code' in query.lower():
            codepath = "C:\\Users\\Neha Nishad\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
    
    elif 'thank you' in query.lower():
        speak(f"Your welcome {MASTER}")

main()
