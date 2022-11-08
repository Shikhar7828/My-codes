import speech_recognition as sr
from googletrans import Translator

def Listen():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,8)

    try:
        print('recognizing....')
        query = r.recognize_google(audio, language="hi")
        # print(f"user said, {query}\n")

    except Exception as e:
        print("I can't understand say that again please...")
        return "None"      
  
    return query

query = Listen().lower()
# print(Listen())

def TranslationHinToEng(Text):
    line = str(Text)
    translate = Translator()
    result = translate.translate(line)
    data = result.text
    print(f"you said : {data}.")
    return data

def micExe():
    # query = Listen()
    data = TranslationHinToEng(query)
    return data

# micExe()


