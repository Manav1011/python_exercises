import threading
import time
import datetime

def first_thread(num):
    # time.sleep(2)
    print(datetime.datetime.now())
    return num *2

def second_thread():
    num=first_thread(20)
    print(num)
    
t1=threading.Thread(target=first_thread, args=(18,))
t2=threading.Thread(target=second_thread, args=())
t1.start()
# t1.join()
t2.start()