#!/bin/python

from tkinter import * #import everything

root = Tk(); #must go before everything else in tkinter

e = Entry(root, width = 50, borderwidth = 2);
e.pack();
#e.get(); #gets whatever you typed into e
e.insert(0, "Enter your name"); #default value in box

def my_click():
	myLabel = Label(root, text = "Hello " + e.get());
	myLabel.pack();

myButton = Button(root, text = "Enter your name", padx = 50, pady = 50, command = my_click, fg = "red", bg = "blue");
myButton.pack();

#Create loop
root.mainloop();
