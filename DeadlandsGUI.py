"""
	Tkinter GUI for Deadlands Players
	
	
	Author: Mickey T Da Silva
	Version: 0.0
	ToDo:
		- Create Player Tab
		- Create Equipment Tab
		- Create Arcane Abilities Tab
		- Create Edges and Hindrances Tab
		- Load / Save Character Function
		- Export as .txt function
	ChangeLog:
		2021-11-22 (Mickey):
			- 
"""

from tkinter import *
from tkinter import ttk

# Set path
import sys, os, pathlib
scriptPath = pathlib.Path( __file__ ).parent.resolve();
subfunctionPath = '{}/subfunctions'.format( scriptPath );
sys.path.append( subfunctionPath );

# Import subfunctions
from MDCG_log import db_log

db_log( 'Imported all modules' );


#========Start GUI=======

root = Tk();
root.title('Deadlands Character GUI');
root.geometry('960x800');

# Create Menubar
from generate_menubar import generate_menubar
menubar = generate_menubar( root );


# Create Tab Layout
from generate_tabs import generate_tabs
[tabParent, characterTab, equipmentTab, characterNotesTab, \
				arcaneAbilitiesTab, edgesTab, gameNotesTab, RNGTab] = generate_tabs( root );

# Create Character Tab
from generate_character_tab import generate_character_tab
generate_character_tab( characterTab );

	
# Create Equipment Tab
db_log( 'Preparing Equipment Tab Layout' );
testLabel = Label( equipmentTab, text = 'Test Label' );
testLabel.grid( row = 0, column = 0 );
db_log( 'Created Equipment Tab Layout' );
	
# Create Arcane Abilities Tab
# ~ if( DEBUG_LEVEL == DEBUG_LEVELS['Debug'] ):
	# ~ MDCG_tee('Preparing Arcane Abilities Tab Layout');
testLabel = Label( arcaneAbilitiesTab, text = 'Test Label' );
testLabel.grid( row = 0, column = 0 );
# ~ if( DEBUG_LEVEL == DEBUG_LEVELS['Debug'] ):
	# ~ MDCG_tee('Created Arcane Abilities Tab Layout');
	
# Create Edges and Hindrances Tab
# ~ if( DEBUG_LEVEL == DEBUG_LEVELS['Debug'] ):
	# ~ MDCG_tee('Preparing Edges and Hindrances Tab Layout');
testLabel = Label( edgesTab, text = 'Test Label' );
testLabel.grid( row = 0, column = 0 );
# ~ if( DEBUG_LEVEL == DEBUG_LEVELS['Debug'] ):
	# ~ MDCG_tee('Created Edges and Hindrances Tab Layout');

# Create Game Happenings Tab
from generate_game_notes_tab import generate_game_notes_tab
generate_game_notes_tab( gameNotesTab );


# Create Character Notes Tab
from generate_character_notes_tab import generate_character_notes_tab
generate_character_notes_tab( characterNotesTab );

	
# Create RNGesus Tab
from generate_RNG_tab import generate_RNG_tab
generate_RNG_tab( RNGTab );

#=========END GUI============
root.config( menu = menubar );
root.mainloop();
