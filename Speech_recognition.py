import speech_recognition as sr
from gtts import gTTS
import os
from playsound import playsound

# Initialize recognizer
recognizer = sr.Recognizer()

# Capture audio from the microphone
with sr.Microphone() as source:
    print("Adjusting for ambient noise... Please wait!")
    recognizer.adjust_for_ambient_noise(source, duration=1)
    print("Listening...")

    # Record the audio
    audio = recognizer.listen(source)

try:
    # Recognize speech using Google Web Speech API
    print("Recognizing speech...")
    text = recognizer.recognize_google(audio)
    print(f"You said: {text}")
    # Create a gTTS object (Google Text-to-Speech)
    tts = gTTS(text=text, lang='en', slow=False)

    # Save the converted speech as an mp3 file
    tts.save("output.mp3")

    # Play the mp3 file
    playsound("output.mp3")

    # Optionally, remove the audio file after playing
    os.remove("output.mp3")

except sr.UnknownValueError:
    print("Sorry, could not understand the audio.")
except sr.RequestError:
    print("Request failed. Please check your internet connection.")



