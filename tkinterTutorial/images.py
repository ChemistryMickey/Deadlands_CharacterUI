from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('');
#root.iconbitmap(''); #location of square file (16x16, 32x32, 64x64; shouldn't be that much larger)

button_quit = Button( root, text = "Exit Program", command = root.quit );
button_quit.pack();

myImg = ImageTk.PhotoImage( Image.open('/home/mickey/1_Documents/1_Projects/DeadlandsGUI/tkinterTutorial/The Hair.jpg') );
myLabel = Label(image = myImg);
myLabel.pack();

root.mainloop();
