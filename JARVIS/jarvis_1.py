
# pip install pyaudio

import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install SpeechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis Maam. Please tell me how may I help you")


def takeCommand():
    # It takes microphone input and returns string output

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


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('yourmail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


if __name__ == "__main__":

    wishMe()

    while True:

        query = takeCommand().lower()

        # Logic for executing tasks based on query

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')

            search_query = query.replace("wikipedia", "").strip()

            if not search_query:
                speak("Please tell me what you want to search.")
                continue

            try:
                results = wikipedia.summary(search_query, sentences=2)

                print(results)
                speak("According to Wikipedia")
                speak(results)

            except wikipedia.exceptions.DisambiguationError:
                speak("There are multiple results. Please be more specific.")

            except wikipedia.exceptions.PageError:
                speak("Sorry, I could not find that topic.")

            except Exception as e:
                print("Wikipedia error:", e)
                speak("Sorry, I could not connect to Wikipedia.")

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("https://stackoverflow.com")

        elif 'play music' in query:
            music_dir = r'D:\Python\Music101'
            songs = os.listdir(music_dir)

            print(songs)

            if songs:
                os.startfile(os.path.join(music_dir, songs[0]))
            else:
                speak("No songs found in the music folder.")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M %p")
            print(f"Ma'am, the time is {strTime}")
            speak(f"Ma'am, the time is {strTime}")

            
        elif 'open code' in query:
            codePath = r"C:\Users\Haris\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            os.startfile(codePath)

        elif 'email to harry' in query:
            try:
                speak("What should I say?")
                content = takeCommand()

                to = "harryyourEmail@gmail.com"

                sendEmail(to, content)

                speak("Email has been sent!")

            except Exception as e:
                print(e)
                speak("Sorry my friend Harry bhai. I am not able to send this email.")

        else:
            print("No query matched")
