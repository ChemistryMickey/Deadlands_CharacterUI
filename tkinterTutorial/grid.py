#!/bin/python

from tkinter import * #import everything

root = Tk(); #must go before everything else in tkinter

myLabel1 = Label( root, text = "Hello World!" ).grid( row = 0, column = 0 ); #you can slap it on the end but it's not too clean
myLabel2 = Label( root, text = "My name is John Elder!" ).grid( row = 0, column = 1 );

#Create loop
root.mainloop();
