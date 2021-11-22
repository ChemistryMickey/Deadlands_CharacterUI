from tkinter import *
from tkinter import ttk
from MDCG_log import db_log


def generate_character_tab( characterTab ):
	db_log( 'Preparing Character Tab' );
	charNameLabel = Label( characterTab, text = 'Character Name:' );
	charNameLabel.grid( row = 0, column = 0, padx = 10, pady = 10 );
	charName = Entry( characterTab, width = 35, borderwidth = 5 );
	charName.grid( row = 0, column = 1, columnspan = 3, padx = 10, pady = 10 );

	charClassLabel = Label( characterTab, text = 'Class: ' );
	charClassLabel.grid( row = 0, column = 4, padx = 10, pady = 10 );
	className = Entry( characterTab, width = 30, borderwidth = 5 );
	className.grid( row = 0, column = 5, columnspan = 2, padx = 10, pady = 10 );

	# Attributes

	db_log( 'Created Character Tab' );
