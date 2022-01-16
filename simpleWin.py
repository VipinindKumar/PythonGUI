import tkinter as tk

win = tk.Tk()
win.title("Simple Pyhton GUI window")

# disable resizing the gui
# win.resizable(0, 0)

# adding label
from tkinter import ttk # themed tk

lable1 = ttk.Label(win, text="Aye Hello")
lable1.grid(column=0, row=0)

# button click event callback fun
def click():
	action.configure(text="## Clicked ##")
	action.configure(foreground="red")

# Creating buttons
action = ttk.button(win, text="Click here", command=click)
action.grid(column=1, row=0)



win.mainloop()