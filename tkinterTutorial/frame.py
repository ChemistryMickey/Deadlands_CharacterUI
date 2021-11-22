from tkinter import *
from PIL import ImageTk, Image

root = Tk();
root.title('Frame');

frame = LabelFrame(root, text = "This is my Frame...", padx = 5, pady = 5); #interior padding
frame.pack(padx = 10, pady = 10); #padding between frame and root frame

b = Button( frame, text = "Click me!", padx = 2, pady = 2 );
b.grid( row = 0, column = 0 );

root.mainloop();
