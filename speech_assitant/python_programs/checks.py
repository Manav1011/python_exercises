from tinydb import TinyDB, Query

db = TinyDB("speech_assistant_by_manav_shah.json")

new_dict={}
for i in db.all():
    new_dict.update({i['command']:i['value']})
string='github'
for i,j in new_dict.items():
    if string in i:
        print(j)