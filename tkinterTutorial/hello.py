#!/bin/python

from tkinter import * #import everything

root = Tk(); #must go before everything else in tkinter

myLabel = Label( root, text = "Hello World!" );
myLabel.pack(); #put it on the screen, not much control

#Create loop
root.mainloop();
