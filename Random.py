import random
import string
from tkinter import *
import tkinter as tk
import tkinter.font as font
import sys
import os
from tkinter import Tk, Label, Button
import webbrowser
from tkinter import ttk

root = Tk()
root.title("Random password generator")

root.geometry("400x290")
root["bg"] = "light blue"
root.iconbitmap('C:\\Users\\User\\Documents\\python\\kas\\mk.ico')

source = string.ascii_letters + string.digits
result_str = ''.join((random.choice(source) for i in range(8)))
myLabel = Label(root,text="Your random password is: " + str(result_str),bg="#F0F0F0",fg="black",font="Arial 10 bold")
myLabel.pack()

def restart_program():
	python = sys.executable
	os.execl(python, python, * sys.argv)

Button(root, text="  Restart  ", command=restart_program, fg="blue").pack()

def callback(url):
    webbrowser.open_new(url)

#making hyperlink

link1 = Button(root, text="Made by Medisrise", fg="blue", cursor="hand2")
link1.pack()
link1.bind("<Button-1>", lambda e: callback("https://github.com/MedisRise"))

root.mainloop()


                                                   
