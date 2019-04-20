# TianTcl - Whisper game - main

import generate, tkinter
from tkinter import messagebox

tkscr = tkinter.Tk()
tkscr.withdraw()

for i in range(5):
    sentence = str(generate.gen())
    messagebox.showinfo("Your sentence",sentence)