from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk();
root.title('File Dialog');

# ~ root.filename = filedialog.askopenfilename( initialdir = ".", title = 'Select a Character File', filetypes = ( ("Python files", "*.py"), ("all files", "*.*") ) );

# ~ Label(root, text = root.filename).pack();

def open_file():
	root.filename = filedialog.askopenfilename( initialdir = ".", title = 'Select a Character File', filetypes = ( ("Python files", "*.py"), ("all files", "*.*") ) );
	
	Label( root, text = root.filename ).pack(); 

btn = Button( root, text = 'Open File', command = open_file ).pack();

root.mainloop();

