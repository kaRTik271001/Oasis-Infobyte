import speech_recognition as sr
from gtts import gTTS
from bs4 import BeautifulSoup
import requests
import os
from datetime import datetime

def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save('response.mp3')
    os.system('start response.mp3')

def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=5)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio).lower()
        print("You said:", query)
        return query
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand the audio.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None

def process_command(command):
    if "hello" in command:
        speak("Hello! How can I help you today?")
    elif "time" in command:
        current_time = datetime.now().strftime("%H:%M")
        speak(f"The current time is {current_time}.")
    elif "date" in command:
        current_date = datetime.now().strftime("%Y-%m-%d")
        speak(f"Today's date is {current_date}.")
    elif "search" in command:
        query = command.replace("search", "").strip()
        search_web(query)
    else:
        speak("I'm sorry, I didn't understand that command.")

def search_web(query):
    try:
        url = f"https://www.google.com/search?q={query}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        results = soup.find_all('div', class_='BNeawe iBp4i AP7Wnd')
        if results:
            result_text = results[0].text
            speak(f"According to the web, {result_text}")
        else:
            speak("I couldn't find any relevant information on the web.")
    except Exception as e:
        speak(f"An error occurred while searching the web: {e}")

if __name__ == "__main__":
    speak("Hello! How can I help you today?")
    while True:
        command = recognize_speech()
        if command:
            process_command(command)
