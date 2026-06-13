import datetime
import os
import smtplib
import webbrowser
from pathlib import Path

import pyttsx3
import speech_recognition as sr
import wikipedia


def create_speech_engine():
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty("voices")
    if voices:
        engine.setProperty("voice", voices[0].id)
    return engine


engine = create_speech_engine()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish_me():
    hour = datetime.datetime.now().hour

    if hour < 12:
        speak("Good Morning!")
    elif hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Jarvis. Please tell me how may I help you.")


def take_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")
        return query.lower()
    except sr.UnknownValueError:
        print("Could not understand audio.")
        speak("Say that again please.")
    except sr.RequestError as error:
        print(f"Speech recognition service error: {error}")
        speak("Speech recognition service is not available right now.")

    return ""


def send_email(to_address, content):
    email = os.getenv("EMAIL")
    password = os.getenv("EMAIL_PASSWORD")

    if not email or not password:
        speak("Email credentials are not configured.")
        return

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.ehlo()
            server.starttls()
            server.login(email, password)
            server.sendmail(email, to_address, content)
        speak("Email has been sent!")
    except Exception as error:
        print(f"Email error: {error}")
        speak("Sorry, I am not able to send this email.")


def search_wikipedia(query):
    search_term = query.replace("wikipedia", "").strip()
    if not search_term:
        speak("Please tell me what to search on Wikipedia.")
        return

    speak("Searching Wikipedia...")

    try:
        results = wikipedia.summary(search_term, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)
    except Exception as error:
        print(f"Wikipedia error: {error}")
        speak("Sorry, I could not fetch the information.")


def play_music():
    music_dir = os.getenv("MUSIC_DIR")

    if not music_dir:
        speak("Music directory is not configured. Set the MUSIC_DIR environment variable.")
        return

    music_path = Path(music_dir)
    if not music_path.exists():
        speak("Music directory not found.")
        return

    songs = [song for song in music_path.iterdir() if song.is_file()]
    if not songs:
        speak("No songs found in the directory.")
        return

    os.startfile(songs[0])


def handle_query(query):
    if not query:
        return True

    if "exit" in query or "quit" in query:
        speak("Goodbye!")
        return False

    if "wikipedia" in query:
        search_wikipedia(query)
    elif "open youtube" in query:
        webbrowser.open("https://www.youtube.com")
    elif "open google" in query:
        webbrowser.open("https://www.google.com")
    elif "play music" in query:
        play_music()
    elif "the time" in query:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {current_time}")
    else:
        print("No query matched")
        speak("I do not know that command yet.")

    return True


def main():
    wish_me()
    while True:
        query = take_command()
        if not handle_query(query):
            break


if __name__ == "__main__":
    main()
