from tkinter import *
from tkinter import ttk
from MDCG_log import db_log

def generate_character_notes_tab( characterNotesTab ) :
	db_log( 'Preparing Character Notes' );

	T = Text( characterNotesTab, height = 40, width = 175, relief = 'groove', state = 'normal' );
	scroll = Scrollbar(characterNotesTab, command=T.yview)
	T.configure( yscrollcommand = scroll.set );
	
	T.grid( row = 0, column = 0, padx = 10, pady = 10 );
	scroll.grid( row = 0, column = 1, sticky = 'ns' )

	db_log( 'Created Character Notes Tab' );

	return ('Character Notes', T);
