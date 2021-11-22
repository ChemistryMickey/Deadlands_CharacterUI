#!/bin/python

from tkinter import * #import everything

root = Tk(); #must go before everything else in tkinter

def my_click():
	myLabel = Label(root, text = "Look! I clicked!");
	myLabel.pack();

myButton = Button(root, text = "Click me!", padx = 50, pady = 50, command = my_click, fg = "red", bg = "blue");
myButton.pack();

#Create loop
root.mainloop();
