from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk();
root.title('Message Box');

# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

def popup():
	response = messagebox.askquestion("This is my popup", "Hello World");
	if( response == 'yes' ):
		print('You responded yes!');
	elif( response == 'no' ):
		print('You responded no!');
	else:
		print('??');
	#print(response);
Button( root, text = 'popup', command = popup ).pack();

root.mainloop();
