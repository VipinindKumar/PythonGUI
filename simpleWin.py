import tkinter as tk

win = tk.Tk()
win.title("Simple Pyhton GUI window")

# disable resizing the gui
# win.resizable(0, 0)

# adding label
from tkinter import ttk

ttk.Label(win, text="Aye Hello").grid(column=0, row=0)

win.mainloop()