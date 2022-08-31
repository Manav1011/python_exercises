import re
import signal
import pyttsx3
import os
import wikipedia
import datetime
import webbrowser
import pyjokes
import speech_recognition as sr
import tkinter as tk
import threading, keyboard
import win32gui
import win32con
import time
from tinydb import TinyDB,Query

db = TinyDB("speech_assistant_by_manav_shah.json")

hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hide, win32con.SW_HIDE)


engine = pyttsx3.init()
engine.setProperty("rate", 130)
engine.setProperty("volume", 1.0)
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
os.system('mode con: cols=100 lines=20')
os.system('color 06')

class speech_assistant(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.start()
    
    def delete_command(self):
        while True:
            x=db.all()
            global Running
            os.system("color 06")
            os.system("cls")
            self.root.withdraw()
            win32gui.ShowWindow(hide, win32con.SW_SHOWNORMAL)
            print(r"-----Your Commands-----")
            Command=Query()
            udf_commands={}
            j=1
            for i in db.all():
                udf_commands.update({j:i['command']})
                j+=1

            for i,j in udf_commands.items():
                print(f'{i} : {j}')
        
            print()
            choice=input("Please enter your choice according to the command you want to delete: ")
            if re.search('[1-9]',choice):
                if 1<=int(choice)<=len(db.all()):
                    db.remove(Command.command==udf_commands[int(choice)])
                    print('command removed successfully')
                    break
                else:
                    break
            else:
                break
        
    def insert_command(self):
        os.system("color 06")
        os.system("cls")
        global Running
        win32gui.ShowWindow(hide, win32con.SW_SHOWNORMAL)
        self.root.withdraw()
        print()
        print(r"for assistant to say something write 'say:{your_input}' ")
        print(r"to open a programme write 'path:{your_file/program_path}' ")
        print()
        global r
        x=db.all()
        while True:
            with sr.Microphone() as source:
                print("Please wait. Calibrating microphone...")
            # listen for 5 seconds and calculate the ambient noise energy level
                r.adjust_for_ambient_noise(source, 2)
                print('Tell your voice command')
                print("Listening...")
                audio = r.listen(source)
                try:
                    print("Recognizing command")
                    query = r.recognize_google(audio, language="en-IN")
                    command = query.lower()
                    for i in x:
                        if command in i['command']:
                            print('voice command already registered!!')
                            time.sleep(2)
                            break
                except Exception as a:
                    break
                value = str(input("Enter the use of the command: "))
                confirm=input("Do you want to save this command?[y/n]")
            if confirm=="y":
                if "path" in value:
                    db.insert({"command": command, "value": r"{}".format(value)})
                    #self.root.deiconify()
                    break
                else:
                    db.insert({"command": command, "value": value})
                    #self.root.deiconify()
                    break
            elif confirm=='n':
                break
            else:
                break
        
        #win32gui.ShowWindow(hide, win32con.SW_HIDE
        
    def default_commands(self):
        while True:
            global Running
            os.system("color 06")
            os.system("cls")
            self.root.withdraw()
            win32gui.ShowWindow(hide, win32con.SW_SHOWNORMAL)
            print()
            print(r"-----Inbuilt Commands-----")
            print("who are you")
            print("tell me a joke")
            print("greet me")
            print(r"{Your command} in wikipedia")
            print(r"search {Your input}   //To search in browser")
            print(r"time //Tells current time")
            print(r"open vs code //opens visual studio code")
            print(r'new command // let user insert new voice command')
            print(r'default commands //shows list of default commands')
            print(r'my commands //shows list of my  commands')
            print()
            if input('Press enter to continue: ')=='':
                break
            else:
                continue
            
    def show_my_commands(self):
        while True:
            x=db.all()
            global Running
            os.system("color 06")
            os.system("cls")
            self.root.withdraw()
            win32gui.ShowWindow(hide, win32con.SW_SHOWNORMAL)
            print(r'------here are your voice commands------')
            for i in x:
                command=i['command']
                value=i['value']
                print()
                print(f'Command: {command}',f'Value: {value}')
            print('----------------------------------------------------------------')
            print()
            if input('Press enter to continue: ')=='':
                break
            else:
                continue
        
        
    def callback(self):
        self.root.quit()

    def run(self):
        global label
        self.root = tk.Tk()
        self.root.geometry("400x400")
        photo = tk.PhotoImage(file=r"Webp.net-resizeimage.png")
        f = tk.Label(image=photo)
        f.pack()
        self.root.protocol("WM_DELETE_WINDOW", self.callback)
        label = tk.Label(text="")
        label.pack()
        self.root.mainloop()

    def recognize(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            label.config(text="Listening...")
            audio = r.listen(source)
            try:
                label.config(text="Recognizing...")
                query = r.recognize_google(audio, language="en-IN")
            except Exception as a:
                label.config(text=a)
                return "None"
            return query.lower()

    def execute(self):
        global Running
        engine.say("Tell me what can i do")
        engine.runAndWait()
        command = self.recognize()
        x = db.all()
        for i in x:
            if str(i["command"]) in command:
                if "say:" in str(i["value"]):
                    newstr = i["value"].replace("say:", "")
                    engine.say(newstr)
                    engine.runAndWait()
                else:
                    newstr = i["value"].replace("path:", "")
                    os.startfile(newstr)
        if 'new command' in command:
            self.insert_command()
       
        if 'delete command' in command:
            self.delete_command()    
        
        if 'show my commands' in command:
            self.show_my_commands()

        if 'default commands' in command:
            self.default_commands()
            
        if "who are you" in command:
            engine.say("I am a voice assistant created by manav shah")
            engine.runAndWait()

        if "joke" in command:
            joke = pyjokes.get_joke(language="en", category="neutral")
            engine.setProperty("rate", 100)
            engine.say(joke)
            engine.runAndWait()

        if "greet me" in command:
            engine.say("Heyy there nice to meet you")
            engine.runAndWait()

        if "stop listening" in command:
            engine.say("Speech recognition is stopping now")
            engine.runAndWait()
            pid = os.getpid()
            os.kill(pid, signal.SIGILL)

        if "in wikipedia" in command:
            global label
            command = command.replace("wikipedia", "")
            results = wikipedia.summary(command, sentences=2)
            label.config(text=results)

        if "search" in command:
            command = command.replace("search", "")
            # fire=webbrowser.get('google-chrome')
            # fire.open("What is one plus three")
            webbrowser.open(command)

        if "time" in command:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            engine.say(time)
            engine.runAndWait()

        if "open vs code" in command:
            os.system("code")

        if "open notes" in command:
            os.system(
                "start D:\python_exercises\speech_assitant\python_programs\dist\exam_notes.exe"
            )
        Running=False


a = speech_assistant()
r = sr.Recognizer()
Running=True
with sr.Microphone() as source:
    while Running:
        label.config(text="Microphone calibrating please wait...")
        # listen for 5 seconds and calculate the ambient noise energy level
        r.adjust_for_ambient_noise(source, 2)
        a.execute()
        a.root.withdraw()
        win32gui.ShowWindow(hide, win32con.SW_SHOWNORMAL)
        while Running ==False:
            os.system("cls")
            os.system("color 06")
            print(r'1: Do you want to insert new voice command?..')
            print()
            print(r'2:Do you want to see default voice commands?..')
            print()
            print(r'3:Do you want to see your voice commands?..')
            print()
            print(r'4:Do you want to delete your voice commands?..')
            print()
            print('Press enter if you want to continue to the voice assistant..')
            print()
            user_choice=input('Enter your choice from above options(1/2/3/4/enter):')
            if user_choice=='1':
                a.insert_command()
            elif user_choice=='2':
                a.default_commands()
            elif user_choice=='3':
                a.show_my_commands()
            elif user_choice=='3':
                a.show_my_commands()
            elif user_choice=='4':
                a.delete_command()
            else:
                Running=True
                win32gui.ShowWindow(hide, win32con.SW_HIDE)
                a.root.deiconify()
        # if keyboard.read_key()=='enter':
