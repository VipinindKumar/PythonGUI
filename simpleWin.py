import tkinter as tk

win = tk.Tk()
win.title("Simple Pyhton GUI window")

# disable resizing the gui
# win.resizable(0, 0)

# adding label
from tkinter import ttk # themed tk

# lable1 = ttk.Label(win, text="Aye Hello")
# lable1.grid(column=0, row=0)

# # button click event callback fun
# def click():
# 	button1.configure(text="## Clicked ##")
# 	lable1.configure(foreground="red")

# button click function
def click():
	button1.configure(text='Hello ' + name.get())

# Creating buttons
button1 = ttk.Button(win, text="Click here", command=click)
button1.grid(column=1, row=1)

# lable
ttk.Label(win, text='Enter your name:').grid(column=0, row=0)

# adding a text box widget
name = tk.StringVar()
nameEntered = ttk.Entry(win, width=12, textvariable=name)
nameEntered.grid(column=0, row=1)



win.mainloop()