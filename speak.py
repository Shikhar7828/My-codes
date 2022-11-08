import pyttsx3

def speak(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice' , voices[0].id)
    engine.setProperty('rate',190)

    engine.say(audio)
    engine.runAndWait()
    print("")
    print(f"A.I : {audio}")
    print("")


speak("hello world")