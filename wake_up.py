import speech_recognition as sr
import os

def Listen():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,8)

    try:
        print('recognizing....')
        query = r.recognize_google(audio, language="en")
        # print(f"user said, {query}\n")

    except Exception as e:
        print("I can't understand say that again please...")
        return "None"  

    # query = Listen().lower()
    print(query)


    return query

while True:
    wake_up = Listen()
    if "wake up" in wake_up:
        os.startfile("Y:\\SEVIN.07\\main.py")

    elif "sevin" in wake_up:
        os.startfile("Y:\\SEVIN.07\\main.py")

    elif "07" in wake_up:
        os.startfile("Y:\\SEVIN.07\\main.py")

    elif "hey sevin" in wake_up:
        os.startfile("Y:\\SEVIN.07\\main.py")

    elif "7" in wake_up:
        os.startfile('Y:\\SEVIN.07\\main.py')

    else:
        pass