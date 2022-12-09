import pyttsx3

def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice' , voices[0].id)
    engine.setProperty('rate',170)
    # print("")
    # print(f"A.I : {text}.")
    # print("")

    engine.say(text)
    engine.runAndWait()







# from Body.speak import speak
fileopen = open("Data\\Api.txt","r")
API = fileopen.read()
fileopen.close()

import openai
from dotenv import load_dotenv


openai.api_key = API
load_dotenv()
completion = openai.Completion()

def ReplyBrain(question,chat_log = None):
    FileLog = open("DataBase\\chat_log.txt","r")
    chat_log_template = FileLog.read()
    FileLog.close()

    if chat_log is None:
        chat_log = chat_log_template

    prompt = f'{chat_log}You : {question}\nSevin : '
    response = completion.create(
        model = "text-davinci-002",
        prompt = prompt,
        temperature = 1,
        max_tokens = 60,
        top_p = 0.3,
        frequency_penalty = 0.5,
        presence_penalty = 0)

    answer = response.choices[0].text.strip()

    chat_log_template_update = chat_log_template + f"\nYou : {question}\nSevin : {answer}\n"
    FileLog = open("DataBase\\chat_log.txt","w")
    FileLog.write(chat_log_template_update)
    FileLog.close()
    return answer


# while True:
#     kk = input("Enter : ")
#     print(ReplyBrain(kk))
#     speak(ReplyBrain(kk))
    
#     if 'exit' in kk:
#         exit()

