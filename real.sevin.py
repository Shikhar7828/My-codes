import code
import pyaudio
import struct
import math
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
from requests import get
import pywhatkit as kit
from googletrans import Translator

# INITIAL_TAP_THRESHOLD = 0.1


# FORMAT = pyaudio.paInt16 
# SHORT_NORMALIZE = (1.0/32768.0)
# CHANNELS = 2
# RATE = 44100  
# INPUT_BLOCK_TIME = 0.05
# INPUT_FRAMES_PER_BLOCK = int(RATE*INPUT_BLOCK_TIME)
# OVERSENSITIVE = 15.0/INPUT_BLOCK_TIME                    
# UNDERSENSITIVE = 120.0/INPUT_BLOCK_TIME 
# MAX_TAP_BLOCKS = 0.15/INPUT_BLOCK_TIME

# def get_rms( block ):
#     count = len(block)/2
#     format = "%dh"%(count)
#     shorts = struct.unpack( format, block )
#     sum_squares = 0.0
#     for sample in shorts:
#         n = sample * SHORT_NORMALIZE
#         sum_squares += n*n

#     return math.sqrt( sum_squares / count )

# class TapTester(object):

#     def __init__(self):
#         self.pa = pyaudio.PyAudio()
#         self.stream = self.open_mic_stream()
#         self.tap_threshold = INITIAL_TAP_THRESHOLD
#         self.noisycount = MAX_TAP_BLOCKS+1 
#         self.quietcount = 0 
#         self.errorcount = 0

#     def stop(self):
#         self.stream.close()

#     def find_input_device(self):
#         device_index = None            
#         for i in range( self.pa.get_device_count() ):     
#             devinfo = self.pa.get_device_info_by_index(i)   
#             # print( "Device %d: %s"%(i,devinfo["name"]) )

#             for keyword in ["mic","input"]:
#                 if keyword in devinfo["name"].lower():
#                     # print( "Found an input: device %d - %s"%(i,devinfo["name"]) )
#                     device_index = i
#                     return device_index

#         if device_index == None:
#             print( "No preferred input found; using default input device." )

#         return device_index

#     def open_mic_stream( self ):
#         device_index = self.find_input_device()

#         stream = self.pa.open(   format = FORMAT,
#                                  channels = CHANNELS,
#                                  rate = RATE,
#                                  input = True,
#                                  input_device_index = device_index,
#                                  frames_per_buffer = INPUT_FRAMES_PER_BLOCK)

#         return stream
    
#     def listen(self):
        
#         try:
#             block = self.stream.read(INPUT_FRAMES_PER_BLOCK)

#         except IOError as e:
#             self.errorcount += 1
#             print( "(%d) Error recording: %s"%(self.errorcount,e) )
#             self.noisycount = 1
#             return

#         amplitude = get_rms( block )
        
#         if amplitude > self.tap_threshold:
#             self.quietcount = 0
#             self.noisycount += 1
#             if self.noisycount > OVERSENSITIVE:

#                 self.tap_threshold *= 1.1
#         else:            

#             if 1 <= self.noisycount <= MAX_TAP_BLOCKS:
#                 return "True-Mic"
#             self.noisycount = 0
#             self.quietcount += 1
#             if self.quietcount > UNDERSENSITIVE:
#                 self.tap_threshold *= 2

# def Tester():

#     tt = TapTester()

#     while True:
#         kk = tt.listen()
#         if "True-Mic" == kk:
#             print("clap detected")
#             print("")
#             print("Starting The Program...")
            
#             break
            
# while True:
    # Tester()


def speak(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice' , voices[0].id)
    engine.setProperty('rate',170)

    engine.say(audio)
    engine.runAndWait()
    print("")
    print(f"A.I : {audio}")


def wishme():
    hour = int(datetime.datetime.now().hour)

    if hour >=0 and hour<12:

        speak("good morning sir!")

    elif hour >=12 and hour <18:

        speak("good afternoon sir!")

    else:
        speak("good evening sir!")

    speak("I am your personal assistant. please tell me how may i help you")

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

# query = Listen().lower()

def TranslationHinToEng(Text):
    line = str(Text)
    translate = Translator()
    result = translate.translate(line)
    data = result.text
    print(f"you said : {data}.")
    return data

def micExe():
    query = Listen()
    data = TranslationHinToEng(query)
    return data

# micExe()
Name = "sevin"
userName = "Shikhar"
nickName = "astroblack"

if __name__ == "__main__":
    wishme()
    while True:
        query = micExe().lower()
        if 'wikipedia' in query:
        
            speak('Searching Wikipedia....')
            speak("wait a second")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=3)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("opening youtube")
            # webbrowser.open("youtube.com")
            codePath = "C:\\Users\\shikh\\OneDrive\\Desktop\\YouTube.lnk"
            os.startfile(codePath)



        elif 'open google' in query:
            speak("opening google")
            webbrowser.open("google.com")
           
        elif "play music" in query:
             speak("sir which song you want to listen")
             s = micExe()
             speak(f"ok playing {s}.")
             kit.playonyt(s)

        elif "play song" in query:
             speak("sir which song you want to listen")
             s = Listen()
             speak(f"ok playing {s}.")
             kit.playonyt(s)

        elif 'time'  in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open visual studio code' in query:
            speak("opening visual studio code")
            codePath = "C:\\Users\\shikh\\OneDrive\\Desktop\\Visual Studio Code.lnk"
            os.startfile(codePath)

        elif 'quit' in query:
            speak("system closed")
            exit()

        elif 'pycharm' in query:
            speak("opening")
            codePath = "Y:\\PyCharm Community Edition 2022.2.3\\bin\\pycharm64.exe"
            os.startfile(codePath)

        elif 'brave' in query:
            speak("opening brave browser")
            codePath = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
            os.startfile(codePath)

        elif 'open command prompt' in query:
            speak("opening")
            codePath = "C:\\Users\\shikh\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Windows PowerShell\\Windows PowerShell (x86).lnk"
            os.startfile(codePath)

        elif 'your name' in query:
            speak("My name is"+Name)
            print("My name is: "+Name)

        elif 'my name' in query:
            speak("your name is :" +userName)
            print("your name is: " +userName)

        elif "play game" in query:
           
        # elif 'github' in query:
        #     speak("opening")
            codePath = "C:\\Users\\shikh\\OneDrive\\Desktop\\GitHub.lnk"
            os.startfile(codePath)

        
        elif 'stop' in query:
            speak("thanks for using me sir, have a good day")
            exit()

        elif 'ip address' in query:
            ip = get('https://api.ipify.org').text
            speak(f"your ip address is {ip}")
            print(ip)

        elif 'song on youtube' in  query:
            speak("wait a second")
            speak
            kit.playonyt("Despasito","middle of the night")

        elif 'github' in query:
            speak("opening")
            codePath = "C:\\Users\\shikh\\OneDrive\\Desktop\\GitHub.lnk"
            os.startfile(codePath)


        elif 'close youtube' in query:
            speak("ok sir closing youtube")
            os.system("taskkill /f /im youtube.com")

        elif 'ok thanks' in query:
            speak("ok sir")
            speak("closing the program")
            exit()

        elif 'astroblack sleep' in query:
            speak("ok sir, as your wish")
            exit()

        elif 'no thanks' in query:
            speak("thanks for using me sir, have a good day ")
            exit()
        
        elif 'hello'  in query:
            speak("hello sir, how are you sir")

        elif 'fine' in query :
            speak("that's nice to hear")

        elif 'hi'  in query:
            speak("hello sir, how are you sir")

        elif "search" in query:
            speak("sir what would you like to search")
            g = micExe()
            kit.search(g)

        elif 'your nick name' in query:
            speak(f"my nick name is {nickName}.")


        # speak("sir do you have any other work")

