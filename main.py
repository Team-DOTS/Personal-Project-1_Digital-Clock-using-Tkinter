from tkinter import *
from tkinter.ttk import *

from time import strftime


root = Tk()
root.title("clock")

def time():
    # To dispaly the time in hours minutes seconds and %p stands for a.m, p.m
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    # To set the delay time-To change after 1 sec
    label.after(1000, time)
# defining the interface
label = Label(root, font=("DS-digital", 80), background="black", foreground="violet")
# allign them to centre
label.pack(anchor='center')
time()
mainloop()
