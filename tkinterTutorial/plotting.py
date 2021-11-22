from tkinter import *
from PIL import ImageTk, Image
import numpy as np
from matplotlib import pyplot as plt

root = Tk();
root.title('Database');
root.geometry('400x400');

def graph():
	housePrices = np.random.normal(200e3, 25e3, 5000);
	plt.hist( housePrices, 50 );
	
	plt.show();
	
btn = Button( root, text = 'Plot bogus data', command = graph );
btn.pack();

root.mainloop()
