# TianTcl - Whisper game - main
import generate, tkinter
from tkinter import messagebox
tkinter.Tk().withdraw()
for i in range(5):
    sentence = str(generate.gen())
    print("Your sentence :",sentence)
    messagebox.showinfo("Your sentence",sentence)