import speech_recognition as sr
from word2number import w2n
import os
  
# initializing string
class voice_calculator:
    def calc(self):
        while True:
            os.system('cls')
            with sr.Microphone() as source:
                            r = sr.Recognizer()
                            print("Tell your voice command")
                            print("Listening...")
                            audio = r.listen(source)
                            try:
                                print("Recognizing command")
                                query = r.recognize_google(audio, language="en-IN")

                                if 'by' in query.lower():
                                    new_list=[]
                                    for i in (query.lower().replace('by','').split()):
                                        new_list.append(w2n.word_to_num(i))
                                    os.system('cls')
                                    print(new_list[0]/new_list[1])
                                    in_=input("do you want to continue? (y/n): ")
                                    if in_=='y':
                                        continue;
                                    else: break

                                if 'into' in query.lower():

                                    new_list=[]
                                    mul=1
                                    for i in (query.lower().replace('into','').split()):
                                        new_list.append(w2n.word_to_num(i))
                                    for i in new_list:
                                        mul*=i
                                    os.system('cls')
                                    print(mul)
                                    in_=input("do you want to continue? (y/n): ")
                                    if in_=='y':
                                        continue;
                                    else: break
                                if 'plus' in query.lower():

                                    new_list=[]
                                    sum=0
                                    for i in (query.lower().replace('plus','').split()):
                                        new_list.append(w2n.word_to_num(i))
                                    for i in new_list:
                                        sum+=i
                                    os.system('cls')
                                    print(sum)
                                    in_=input("do you want to continue? (y/n): ")
                                    if in_=='y':
                                        continue;
                                    else: break
                                if 'minus' in query.lower():

                                    new_list=[]
                                    sub=1
                                    for i in (query.lower().replace('minus','').split()):
                                        new_list.append(w2n.word_to_num(i))
                                    for i in new_list:
                                        mul*=i
                                    os.system('cls')
                                    print(mul)
                                    in_=input("do you want to continue? (y/n): ")
                                    if in_=='y':
                                        continue;
                                    else: break
                                else:
                                    os.system('cls')
                                    print(eval(query.lower()))
                                    in_=input("do you want to continue? (y/n): ")
                                    if in_=='y':
                                        continue;
                                    else: break


                            except Exception as a:
                                print(a);
                                in_=input("do you want to continue? (y/n): ")
                                if in_=='y':
                                    continue;
                                else: break


a=voice_calculator()                               
a.calc()
