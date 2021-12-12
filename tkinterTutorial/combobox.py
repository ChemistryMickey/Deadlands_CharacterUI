from tkinter import *
from tkinter import ttk
#from tkinter.ttk import combobox

root = Tk();

strVar = StringVar();
optionList = str( list( range(50) ) );
combobox = ttk.Combobox( root, textvariable = strVar, width = 40, values = optionList);
combobox.pack();

label = Label( root, text = '', width = 40 );
label.pack();

def update_label(*args):
    label.config( text = strVar.get() );
strVar.trace("w", update_label);



root.mainloop();