import os
import keyboard
import pyautogui
import webbrowser
from time import sleep


def OpenExe(query):
    query = str(query).lower()

    if "visit " in query:
        nameofweb = query.replace("visit ","")
        Link = f"https://www.{nameofweb}.com"
        webbrowser.open(Link)
        return True

    elif "launch " in query:
        nameofweb = query.replace("visit ","")
        Link = f"https://www.{nameofweb}.com"
        webbrowser.open(Link)
        return True

    elif "open" in query:
        nameofapp = query.replace("open","")
        pyautogui.press('win')
        # sleep(1)
        keyboard.write(nameofapp)
        # sleep(1)
        keyboard.press('enter')
        # sleep(0.5)
        return True

    elif "start" in query:
        nameofapp = query.replace("open","")
        pyautogui.press('win')
        # sleep(1)
        keyboard.write(nameofapp)
        # sleep(1)
        keyboard.press('enter')
        # sleep(0.5)
        return True


# OpenExe("visit ")
