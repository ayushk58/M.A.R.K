#the module is responsile to convert the text to the speech to the user
import speech_recognition as sr
import pyttsx3

engine=pyttsx3.init()

def say(text):
    print(text)
    engine.say(text)
    engine.runAndWait()


def listen():
    listener=sr.Recognizer()
    with sr.Microphone() as source:
        voice=listener.listen(source)
        try:
            command=listener.recognize_google(voice)
        except sr.UnknownValueError:
            say("Pardon me,please say that again")
            command = listen()
        except sr.RequestError as e:
            say("Request Failed due to network issues")
            command = listen()
        if command!="":
            return command
