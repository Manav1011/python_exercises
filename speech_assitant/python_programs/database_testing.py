from tinydb import TinyDB, Query
import json
import os
import pyttsx3

engine=pyttsx3.init()
db=TinyDB('db.json')
command="open"
db.insert({'command':'open','value':'say:manav shah'})
x=db.all()
engine.say("Speech recognition is stopping now")
engine.runAndWait()
for i in x:
    if str(i['command']) in command:
        if 'say:' in i['value']:
            newstr=i['value'].replace('say:','')
            engine.say("Speech recognition is stopping now")
            engine.runAndWait()
        if 'open' in i['command']:
            newstr=i['value'].replace('path:','')
            os.startfile(newstr)
        
    

    

