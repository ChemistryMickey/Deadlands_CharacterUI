# Mickey understanding listboxes

from tkinter import *

def main():
    # Create Window
    root = Tk();
    
    # Create Listbox
    listbox = Listbox( root, width = 40, yscrollcommand = True );
    for i in range( 50 ):
        listbox.insert( i, 'Index: {}'.format( i ) );
    listbox.place( relx = 0.2, rely = 0.2 );
    
    
    # Create Label
    label = Label( root, text = listbox.get(0), width = 40 );
    label.place( relx = 0.2, rely = 0.6 );
    
    
    def update_label():
        label.config( text = listbox.curselection() );
    
    
    # Update Button
    def selected_item():
        label.config( text = listbox.curselection() );
            
    Button( root, text = 'Print Selected', command = selected_item ).place( relx = 0.6, rely = 0.2 );
    
    root.mainloop(); 
    
    
    
if __name__ == '__main__' : main();