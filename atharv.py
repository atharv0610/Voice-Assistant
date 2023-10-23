import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

with sr.Microphone() as source:
    print("Listening...")
    audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You said: " + text)

        if "what's the weather" in text:
            # Code to fetch and display weather information
            pass
        elif "open website" in text:
            # Code to open a specific website
            pass

        # Add more commands as per your requirements

    except sr.UnknownValueError:
        print("Google Web Speech API could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Web Speech API; {0}".format(e))

engine.say("Hello, how can I assist you?")
engine.runAndWait()

