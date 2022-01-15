from tkinter import *
import webbrowser
import subprocess
import speech_recognition as sr
from datetime import datetime
import pyttsx3
root = Tk()
root.geometry('500x500')
root.configure(background='lightblue')

label = Label(root,text='Welcome to your personal desktop assistant',bg='lightblue',fg='black',font=('Bahnschrift Light',20,'bold'))
label.place(relx=0.5,rely=0.3,anchor=CENTER)

text_to_speech = pyttsx3.init()

def speak(audio):
    text_to_speech.say(audio)
    text_to_speech.runAndWait()

def r_audio():
    speak('How can I help you?')
    speech_recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        audio = speech_recognizer.listen(source)
        voice_data = ''
        try:
            voice_data = speech_recognizer.reognize_google(audio,language='en-us')
        except sr.UnknownValueError:
            print('Please Repeat, I did not understand that')
            speak('Please Repeat, I did not understand that')
            r_audio()
    respond(voice_data)
    
def respond(voice_data):
    voice_data = voice_data.lower()
    print(voice_data)
    if 'name' in voice_data:
        speak('My name is Aditi')
        print('My name is Aditi')
    if 'time' in voice_data:
        speak('Current time is: ')
        now = datetime.now()
        current_time = now.strftime('%H:%M:%S:')
        speak(current_time)
        print(current_time)
    if 'search' in voice_data:
        speak('Opening google')
        print('Opening google')
        webbrowser.get().open('https://google.com/')
    if 'video' in voice_data:
        speak('Opening youtube')
        print('Opening youtube')
        webbrowser.get().open('https://youtube.com/')
    if 'text editor' in voice_data:
        speak('Opening text editor')
        print('Opening text editor')
        subprocess.call(['/usr/bin/open','/Applications/TextEdit.app'])
        
btn = Button(root,text='Start',command=r_audio,bg='lightblue',fg='black',font=('Bahnschrift Light',18,'bold'))
btn.place(relx=0.5,rely=0.6,anchor=CENTER)

root.mainloop()
