# Jarvis Ai Assistant--

import speech_recognition as sr  # Library for speech recognition
import webbrowser               # Library to open web pages
import pyttsx3                  # Text-to-speech conversion library
from datetime import datetime   # For getting current date and time
import musiclibrary             # Custom module containing music links
import requests                 # For making HTTP requests (e.g., news API)
import random                   # For random selection (e.g., jokes)

# Predefined list of jokes
jokes = [
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Why don't scientists trust atoms? Because they make up everything!",
    "I told my computer I needed a break, and it said 'No problem — I'll go to sleep.'",
    "Why did the math book look sad? Because it had too many problems!"
]

newsapi= "0b4ada0401a0427189fa7fd8ce24c602"  # API key for newsapi.org

# Function to convert text to speech
def speak(text):
    engine = pyttsx3.init()  # Initialize TTS engine
    engine.say(text)         # Queue the text to speak
    engine.runAndWait()      # Play the speech

# Function to process user commands
def processcommand(c):
    c = c.lower()  # Convert command to lowercase for easier comparison

    # Open YouTube
    if 'youtube' in c:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    # Open Google
    elif ' google' in c:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    # Open LinkedIn
    elif 'linkedin' in c:
        speak("Opening LinkedIn")
        webbrowser.open("https://www.linkedin.com")

    # Open GitHub
    elif 'github' in c:
        speak("Opening GitHub")
        webbrowser.open("https://www.github.com")

    # Play YouTube music
    elif 'youtube music' in c:
        speak("Playing music")
        webbrowser.open("https://music.youtube.com")

    # Tell the current time
    elif 'the time' in c:
        now = datetime.now()                     # Get current datetime
        current_time = now.strftime("%H:%M:%S")  # Format time as HH:MM:SS
        speak(f"The current time is {current_time}")

    # Open WhatsApp Web
    elif 'whatsapp' in c:
        speak("Opening WhatsApp")
        webbrowser.open("https://web.whatsapp.com/")

    # Play a specific song from the music library
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]  # Extract song name
        link = musiclibrary.music[song] # Get song link
        webbrowser.open(link)

    # Exit the program
    elif 'exit' in c or 'quit' in c:
        speak("Exiting. Goodbye!")
        exit()

    # General greetings and interactions
    elif 'hello' in c:
        speak("Hello! How can I assist you?")
    elif 'help' in c:
        speak("You can ask me to open websites, tell the time, play music, and more.")
    elif 'thank you' in c:
        speak("You're welcome!")
    elif 'what is your name' in c:
        speak("I am Jarvis, your personal assistant.")
    elif 'who created you' in c:
        speak("I was created by Rishi Yadav.")
    elif 'where do you live' in c:
        speak("I live in the cloud.")
    elif 'how are you' in c:
        speak("I'm just a program, but thanks for asking!")

    # Fetch and read latest news
    elif 'news' in c:
        speak("Here are the latest news headlines.")
        try:
            url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}"
            response = requests.get(url)
            data = response.json()
            articles = data['articles'][:5]  # Take top 5 headlines
            for article in articles:
                speak(article['title'])
        except Exception as e:
            speak("Sorry, I couldn't fetch the news at this time.")
            print(f"News API error: {e}")

    # Tell a random joke
    elif 'tell me a joke' in c:
        joke = random.choice(jokes)
        speak(joke)       

    # Unrecognized command
    else:
        print("Command not recognized. Please try again.")

# Main program starts here
if __name__ == "__main__":
    speak("Initializing Jarvis...")  # Startup greeting

    r = sr.Recognizer()  # Initialize the speech recognizer

    while True:
        try:
            # Listen for the wake word
            with sr.Microphone() as source:
                print("Listening for wake word...")
                r.adjust_for_ambient_noise(source, duration=0.5)
                audio = r.listen(source, timeout=5, phrase_time_limit=5)
                word = r.recognize_google(audio)
                print(f"You said: {word}")

            # Check if wake word ("jarvis") is in the sentence
            if "jarvis" in word.lower():
                speak("Yeah, I'm here.")

                # Listen for command after wake word
                with sr.Microphone() as source:
                    print("Listening for command...")
                    r.adjust_for_ambient_noise(source, duration=0.5)
                    audio = r.listen(source, timeout=5, phrase_time_limit=5)
                    command = r.recognize_google(audio)
                    print(f"Command: {command}")

                processcommand(command)  # Process the command

        except Exception as e:
            print(f"Error: {e}")  # Handle recognition or runtime errors
