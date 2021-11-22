from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk();
root.title('New Window');

# ~ top = Toplevel(); #instantly create a new window
# ~ lbl = Label(top, text = 'This is a test').pack();

def open_window():
	top = Toplevel(); #don't want another instance of Tk (not sure why but that seems to be the standard)
	top.title('This is a second window test');
	Label(top, text = 'This is a test second window').pack();
	
	btn2 = Button( top, text = 'Close Window', command = top.destroy );
	btn2.pack();
	

btn = Button( root, text = 'Open second window', command = open_window ).pack();

root.mainloop();
