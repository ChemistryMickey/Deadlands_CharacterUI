from tkinter import *
from tkinter import ttk
from MDCG_log import db_log
from datetime import datetime

def generate_game_notes_tab( gameNotesTab ) :
	db_log( 'Preparing Game Notes Tab' );

	T = Text( gameNotesTab, height = 40, width = 175, relief = 'groove', state = 'normal', wrap = WORD, highlightcolor = '#000000' );
	scroll = Scrollbar(gameNotesTab, command=T.yview)
	T.configure( yscrollcommand = scroll.set );
	
	T.grid( row = 1, column = 0, padx = 10, pady = 10 );
	scroll.grid( row = 1, column = 2, sticky = 'ns' )

	entryButton = Button( gameNotesTab, text = "New Entry", height = 2, width = 10, command = lambda: write_new_entry( T ) );
	entryButton.grid( row = 0, column = 0, padx = 10, pady = 0 );
	
	db_log( 'Created Game Notes Tab' );

	return ('Game Notes', T); #Stub
	
def write_new_entry( textObjectIn ):
	db_log( 'Writing new game notes entry' );
	curTime = str( datetime.now().strftime( '%Y-%m-%d %H:%M' ) );
	curLog = textObjectIn.get("1.0", 'end');
	textObjectIn.delete( '1.0', 'end' );
	
	eventLine = curTime + ':\n';
	
	textObjectIn.insert( "1.0", '{}{}'.format( eventLine, curLog ) );
	return True;
