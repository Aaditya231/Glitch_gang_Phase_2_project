import pyttsx3                                     
import datetime
import speech_recognition as sr                                                  
import wikipedia                            
import webbrowser
import os
import sys
import pywhatkit                                                      
from pywikihow import search_wikihow               
import pyautogui                                                                                                 
import wolframalpha                                            
import winshell as winshell                        


engine = pyttsx3.init()

def fun_talk(audio):
    engine.say(audio)
    engine.runAndWait()

def wish_user():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        fun_talk("Good Morning !")
    elif hour >= 12 and hour < 18:
        fun_talk("Good Afternoon !")
    else:
        fun_talk("Good Evening !")
        
    fun_talk("I am P.A. (Python Assistant). Tell me how may I help you.")


def get_command():
    rec = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        rec.pause_threshold = 1

        audio = rec.listen(source)

        try:
            print("Recognizing...")
            query = rec.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            return "None"
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            return "None"

        except Exception as e:
            print(e)
            print("Say that again please...")
            return "None"
        return query


if __name__ == '__main__':
    wish_user()
    while True: 
        query = get_command().lower()
        home_user_dir = os.path.expanduser("~")

        if 'wikipedia' in query:
            fun_talk('Searching Wikipedia')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            fun_talk("According to Wikipedia")
            print(results)
            fun_talk(results)

        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")

        elif 'open google' in query:
            webbrowser.open("www.google.com")

        elif 'open blackboard' in query:
            webbrowser.open("cuchd.blackboard.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            fun_talk(f"The time is {strTime}")

        elif 'the date' in query:
            strDate = datetime.datetime.today().strftime('%Y-%m-%d')
            print(strDate)
            fun_talk(f"The date is {strDate}")

        elif 'open visual studio code' in query:
            os.startfile(home_user_dir + "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\"
                         "Programs\\Visual Studio Code\\Visual Studio Code")

        elif 'open notepad' in query:
            os.startfile("C:\\Windows\\notepad.exe")

        elif 'open mozilla firefox' in query:
            os.startfile("C:\\Program Files\\Mozilla Firefox\\firefox.exe")

        elif 'open chrome' in query:
            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

        elif 'open v l c' in query:
            os.startfile("C:\\Program Files\\VideoLAN\\VLC\\vlc.exe")

        elif 'who are you' in query:
            fun_talk("I am P.A. (Python Assistant), developed by Rishabh Ranjan, Himanshi, "
                        "Rachit Dwivedi and Umesh Singh as a project in their college.")

        elif 'what you want to do' in query:
            fun_talk("I want to help people to do certain tasks on their single voice commands.")

        elif 'python assistant' in query:
            fun_talk("Are you joking. You're coming in loud and clear.")

        elif 'what language you use' in query:
            fun_talk("I am written in Python and I generally speak english.")

        elif 'play' in query:
            cmd_info = query.replace('play', '')
            fun_talk(f'Playing {cmd_info} ')
            print(cmd_info)
            pywhatkit.playonyt(cmd_info)

        elif 'search' in query:
            query = query.replace('search', '')
            pywhatkit.search(query)

        elif 'exit pa' in query:
            fun_talk("Exiting Sir...")
            sys.exit()

        elif 'close command prompt' in query:
            os.system("TASKKILL /F /IM cmd.exe")

        elif 'close visual studio code' in query:
            os.system("TASKKILL /F /IM Code.exe")

        elif 'close notepad' in query:
            os.system("TASKKILL /F /IM notepad.exe")

        elif 'close chrome' in query:
            os.system("TASKKILL /F /IM chrome.exe")


        elif 'close vlc' in query:
            os.system("TASKKILL /F /IM vlc.exe")


            webbrowser.open(query)

        elif 'resume' in query or 'pause' in query:
            pyautogui.press("playpause")

        elif 'previous' in query:
            pyautogui.press("prevtrack")

        elif 'next' in query:
            pyautogui.press("nexttrack")

      
        elif 'month' in query or 'month is going' in query:
            def tell_month():
                month = datetime.datetime.now().strftime("%B")
                fun_talk(month)

            tell_month()

        elif 'day' in query or 'day today' in query:
            def tell_day():
                day = datetime.datetime.now().strftime("%A")
                fun_talk(day)

            tell_day()

        elif "calculate" in query:
            try:
                app_id = "JUGV8R-RXJ4RP7HAG"
                client = wolframalpha.Client(app_id)
                indx = query.lower().split().index('calculate')
                query = query.split()[indx + 1:]
                res = client.query(' '.join(query))
                answer = next(res.results).text
                print("The answer is " + answer)
                fun_talk("The answer is " + answer)

            except Exception as e:
                print("Couldn't get what you have said, Can you say it again??")


        elif 'empty recycle bin' in query or 'clear recycle bin' in query:
            try:
                winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
                print("Recycle Bin is cleaned successfully.")
                fun_talk("Recycle Bin is cleaned successfully.")

            except Exception as e:
                print("Recycle bin is already Empty.")
                fun_talk("Recycle bin is already Empty.")

        elif 'write a note' in query or 'make a note' in query:
            fun_talk("What should I write, sir??")
            note = get_command()
            file = open('Notes.txt', 'a')
            fun_talk("Should I include the date and time??")
            n_conf = get_command()
            if 'yes' in n_conf:
                str_time = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(str_time)
                file.write(" --> ")
                file.write(note)
                fun_talk("Point noted successfully.")
            else:
                file.write("\n")
                file.write(note)
                fun_talk("Point noted successfully.")

        elif 'show me the notes' in query or 'read notes' in query:
            fun_talk("Reading Notes")
            file = open("Notes.txt", "r")
            data_note = file.readlines()
            # for points in data_note:
            print(data_note)
            fun_talk(data_note)


        elif 'screenshot' in query:
            sc = pyautogui.screenshot()
            sc.save('pa_ss.png')
            print("Screenshot taken successfully.")
            fun_talk("Screenshot taken successfully.")

        elif 'volume up' in query:
            pyautogui.press("volumeup")

        elif 'volume down' in query:
            pyautogui.press("volumedown")

        elif 'mute volume' in query:
            pyautogui.press("volumemute")

        elif 'shutdown' in query:
            print("Do you want to shutdown you system?")
            fun_talk("Do you want to shutdown you system?")
            cmd = get_command()
            if 'no' in cmd:
                continue
            else:
                
                os.system("shutdown /s /t 1")

        elif 'restart' in query:
            print("Do you want to restart your system?")
            fun_talk("Do you want to restart your system?")
            cmd = get_command()
            if 'no' in cmd:
                continue
            else:
                
                os.system("shutdown /r /t 1")

        elif 'logout' in query:
            print("Do you want to logout from your system?")
            fun_talk("Do you want to logout from your system?")
            cmd = get_command()
            if 'no' in cmd:
                continue
            else:
                os.system("shutdown -l")
