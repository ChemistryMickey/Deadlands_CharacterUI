from tkinter import *
from PIL import ImageTk, Image

root = Tk();
root.title('Dropdown Box');
root.geometry('400x400');

optionList = ["Monday", "Tuesday", "Wednesday"]


clicked = StringVar();
clicked.set(optionList[0]);


drop = OptionMenu( root, clicked, *optionList )
drop.pack();

def show():
	Label(root, text = clicked.get()).pack();

btn = Button( root, text = "Show Selection", command = show ).pack();

root.mainloop();
