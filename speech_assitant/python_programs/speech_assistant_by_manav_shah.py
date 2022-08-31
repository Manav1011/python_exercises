import re
import signal
import pyttsx3
import os
import wikipedia
import datetime
import speech_recognition as sr
import time
from tinydb import TinyDB, Query

db = TinyDB("speech_assistant_by_manav_shah.json")

engine = pyttsx3.init()
engine.setProperty("rate", 130)
engine.setProperty("volume", 1.0)
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
os.system("color 06")


class speech_assistant:
    def delete_command(self):
        while True:
            x = db.all()
            os.system("color 06")
            os.system("cls")
            print(r"-----Your Commands-----")
            Command = Query()
            udf_commands = {}
            j = 1
            for i in db.all():
                udf_commands.update({j: i["command"]})
                j += 1

            for i, j in udf_commands.items():
                print(f"{i} : {j}")

            print()
            choice = input(
                "Please enter your choice according to the command you want to delete: "
            )
            if re.search("[1-9]", choice):
                if 1 <= int(choice) <= len(db.all()):
                    db.remove(Command.command == udf_commands[int(choice)])
                    print("command removed successfully")
                    break
                else:
                    break
            else:
                break

    def search_in_browser(self):
        os.system("color 06")
        os.system("cls")
        global r
        while True:
            with sr.Microphone() as source:
                print("Tell your voice command")
                print("Listening...")
                audio = r.listen(source)
                try:
                    print("Recognizing command")
                    query = r.recognize_google(audio, language="en-IN")
                    command = query
                    link = command.replace('+', '%2B')
                    link = link.replace(' ', '+')
                    if 'Google' in link:
                        os.system(f'start www.google.com/search?q={link}')
                        break
                    elif 'in YouTube' in link:
                        os.system(f'start www.youtube.com/results?search_query={link}')
                        break
                        
                except Exception as a:
                    break

    def type_and_open(self):
        os.system("color 06")
        os.system("cls")
        default = {}
        default.update({1: "open vs code",
                       2: "code for python",
                       3:"django project",
                       })
        for i, j in default.items():
            print(i, ' : ', j)

        udf_commands = {}
        j = 4
        for i in db.all():
            udf_commands.update({j: i["command"]})
            j += 1

        for i, j in udf_commands.items():
            print(f"{i} : {j}")
        while True:
            global command_main
            x = db.all()
            u_i = input("Type the command here: ")
            if not re.search('[0-9]', u_i):
                for i in x:
                    if u_i == i['command']:
                        if "say:" in str(i["value"]):
                            newstr = i["value"].replace("say:", "")
                            engine.say(newstr)
                            engine.runAndWait()
                            break
                        else:
                            newstr = i["value"].replace("path:", "")
                            print('Executing command: {}'.format(i['command']))
                            os.startfile(newstr)
                            break
                    else:
                        command_main = u_i
                        self.run_command(command_main)
                        break
                break
            else:
                if int(u_i) in default.keys():
                    command_main = default[int(u_i)]
                    self.run_command(command_main)
                    break
                elif int(u_i) in udf_commands.keys():
                    if "say:" in udf_commands[int(u_i)]:
                        newstr = udf_commands[int(u_i)].replace("say:", "")
                        self.run_command(newstr)
                        break
                    else:
                        newstr = udf_commands[int(u_i)].replace("path:", "")
                        self.run_command(newstr)
                        break
            break

    def insert_command(self):
        os.system("color 06")
        os.system("cls")
        print()
        print(r"for assistant to say something write 'say:{your_input}' ")
        print(r"to open a programme write 'path:{your_file/program_path}' ")
        print()
        global r
        x = db.all()
        while True:
            with sr.Microphone() as source:
                print("Please wait. Calibrating microphone...")
                # listen for 5 seconds and calculate the ambient noise energy level
                r.adjust_for_ambient_noise(source, 2)
                print("Tell your voice command")
                print("Listening...")
                audio = r.listen(source)
                try:
                    print("Recognizing command")
                    query = r.recognize_google(audio, language="en-IN")
                    command = query.lower()
                    for i in x:
                        if command in i["command"]:
                            print("voice command already registered!!")
                            time.sleep(2)
                            break
                except Exception as a:
                    break
                print(f"Your command is: {command}")
                command_con=str(input("Is this you wanted to say? [y/n]"))
                if command_con=="y":
                    value = str(input("Enter the use of the command: "))
                    confirm = input("Do you want to save this command?[y/n]")
                    if confirm == "y":
                        if "path" in value:
                            db.insert(
                                {"command": command, "value": r"{}".format(value)})
                            # self.root.deiconify()
                            break
                        else:
                            db.insert({"command": command, "value": value})
                            # self.root.deiconify()
                            break
                    elif confirm == "n":
                        break
                    else:
                        break
                else:
                    break

        # win32gui.ShowWindow(hide, win32con.SW_HIDE

    def default_commands(self):
        while True:
            os.system("color 06")
            os.system("cls")
            print()
            print(r"-----Inbuilt Commands-----")
            print("who are you")
            print("tell me a joke")
            print("greet me")
            print(r"{Your command} in wikipedia")
            print(r"search {Your input}   //To search in browser")
            print(r"time //Tells current time")
            print(r"open vs code //opens visual studio code")
            print(r"new command // let user insert new voice command")
            print(r"default commands //shows list of default commands")
            print(r"my commands //shows list of my  commands")
            print()
            if input("Press enter to continue: ") == "":
                break
            else:
                continue

    def show_my_commands(self):
        while True:
            x = db.all()
            os.system("color 06")
            os.system("cls")
            print(r"------here are your voice commands------")
            for i in x:
                command = i["command"]
                value = i["value"]
                print()
                print(f"Command: {command}", f"Value: {value}")
            print("----------------------------------------------------------------")
            print()
            if input("Press enter to continue: ") == "":
                break
            else:
                continue

    def recognize(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)
            try:
                print("Recognizing...")
                query = r.recognize_google(audio, language="en-IN")
            except Exception as a:
                print(a)
                return "None"
            return query.lower()

    def execute(self):
        command = self.recognize()
        self.run_command(command)

    def run_command(self, command_main):
        self.command_main = command_main
        global Running
        x = db.all()
        for i in x:
            if str(i["command"]) in command_main:
                if "say:" in str(i["value"]):
                    newstr = i["value"].replace("say:", "")
                    engine.say(newstr)
                    engine.runAndWait()
                else:
                    newstr = i["value"].replace("path:", "")
                    print('Executing command: {}'.format(i['command']))
                    os.startfile(newstr)
                    
        if 'low performance' in command_main:
            os.system(
                "powercfg.exe /setactive a1841308-3541-4fab-bc81-f71556f20b4a")

        if 'balance performance' in command_main:
            os.system(
                "powercfg.exe /setactive 381b4222-f694-41f0-9685-ff5bb260df2e")

        if 'high performance' in command_main:
            os.system(
                "powercfg.exe /setactive 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c")

        if "new command" in command_main:
            self.insert_command()

        if "delete command" in command_main:
            self.delete_command()

        if "show my commands" in command_main:
            self.show_my_commands()

        if "default commands" in command_main:
            self.default_commands()

        if "who are you" in command_main:
            engine.say("I am a voice assistant created by manav shah")
            engine.runAndWait()
            
        if 'django course' in command_main:
            os.chdir(r'D:\Django\[FreeCourseSite.com] Udemy - Python eCommerce Build a Django eCommerce Web Application')
            os.system('start.')
        
        if "search" in command_main:
            command_main = command_main.replace("search:", "")
            link = command_main.replace('+', '%2B')
            link = link.replace(' ', '+')
            os.system(f'start www.google.com/search?q={link}')


        if "stop listening" in command_main:
            engine.say("Speech recognition is stopping now")
            engine.runAndWait()
            print("speech recognition is stopped.")
            os.system("cls")
            pid = os.getpid()
            os.kill(pid, signal.SIGILL)

        if "in wikipedia" in command_main:
            global label
            command_main = command_main.replace("wikipedia", "")
            results = wikipedia.summary(command_main, sentences=2)
            label.config(text=results)

        if "time" in command_main:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            engine.say(time)
            engine.runAndWait()

        if "open vs code" in command_main:
            os.system("code")

        if 'code for python' in command_main:
            os.chdir(r"D:\python_exercises\speech_assitant")
            os.system('code ..')
            
        if 'django project' in command_main:
            os.chdir(r"'D:\django_uedmy\simplecrud\simplecrud'")
            os.system('code ..')
            
        if "open notes" in command_main:
            os.system(
                "start D:\python_exercises\speech_assitant\python_programs\dist\exam_notes.exe"
            )
        Running = True


a = speech_assistant()
r = sr.Recognizer()
Running = True
with sr.Microphone() as source:
    while Running:
        while Running:
            os.system("cls")
            os.system("color 06")
            print(r"1: Do you want to insert new voice command?..")
            print()
            print(r"2:Do you want to see default voice commands?..")
            print()
            print(r"3:Do you want to see your voice commands?..")
            print()
            print(r"4:Do you want to delete your voice commands?..")
            print()
            print(r"5:Do you want to stop the voice assistant?..")
            print()
            print(r"6:Do you want seach something in the browser?..")
            print()
            print("7:Do you want to type and execute the comamnd..")
            print()
            print("Press enter if you want to continue to the voice assistant..")
            print()
            user_choice = input(
                "Enter your choice from above options(1/2/3/4/5/6/7/enter):"
            )
            if user_choice == "1":
                a.insert_command()
            elif user_choice == "2":
                a.default_commands()
            elif user_choice == "3":
                a.show_my_commands()
            elif user_choice == "3":
                a.show_my_commands()
            elif user_choice == "4":
                a.delete_command()
            elif user_choice == "6":
                a.search_in_browser()
            elif user_choice == "7":
                a.type_and_open()

            elif user_choice == "5":
                engine.say("Speech recognition is stopping now")
                engine.runAndWait()
                print("speech recognition is stopped.")
                os.system("cls")
                pid = os.getpid()
                os.kill(pid, signal.SIGILL)
            else:
                Running = False
                os.system("cls")
                r.adjust_for_ambient_noise(source, 2)
                a.execute()
