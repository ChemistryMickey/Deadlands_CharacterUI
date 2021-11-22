from tkinter import *
from tkinter import ttk
from MDCG_log import db_log

from create_new_character import create_new_character
from load_character import load_character
from save_character import save_character

def generate_menubar( root ):
	db_log( 'Preparing Menubar' );

	menubar = Menu( root );
	fileMenu = Menu( menubar, tearoff = 0 );
	fileMenu.add_command( label = 'New Character', command = create_new_character );
	fileMenu.add_command( label = 'Load Character', command = load_character );
	fileMenu.add_command( label = 'Save Character', command = save_character );
	fileMenu.add_separator();
	fileMenu.add_command( label = 'Exit', command = root.quit );
	menubar.add_cascade( label = 'File', menu = fileMenu );
	
	db_log( 'Created Menubar' );	

	return menubar;
