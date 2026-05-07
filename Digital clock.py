from tkinter import *
from tkinter import ttk
from tkinter import font
import time
import datetime

 
def quit():
    root.destroy()

def clock_time():
       
    time=datetime.datetime.now()
    time=(time.strftime("%Y-%m-%d %H:%M:%S"))
    txt.set(time)
    root.after(1000,clock_time)
        

root=Tk()
root.attributes("-fullscreen",True)
root.configure(background='white')
root.bind("<Escape>",quit)
root.after(1000,clock_time)

fnt=font.Font(family='Chiller', size=100, weight='bold')
txt=StringVar()
lbl=ttk.Label(root, textvariable=txt, font=fnt, foreground="black", background="white")
lbl.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()
