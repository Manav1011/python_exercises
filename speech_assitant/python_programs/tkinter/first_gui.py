import tkinter as tk

root=tk.Tk()
root.geometry('300x300')

def helloCallBack():
    global w
    C = tk.Canvas(root, bg="blue", height=250, width=300)
    C.pack()
    w['text']='Go Back'
    w['command']=GoBack

def GoBack():
    global C
    C.pack_forget()
    
w=tk.Button(root, text ="Hello", command = helloCallBack)
w.pack()

root.mainloop()