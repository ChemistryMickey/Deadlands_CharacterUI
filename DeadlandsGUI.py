"""
	Tkinter GUI for Deadlands Players
	
	
	Author: Mickey T Da Silva
	Version: 0.0
	ToDo:
		- Create Equipment Tab
		- Create Arcane Abilities Tab
		- Create Edges and Hindrances Tab
		- Load / Save Character Function
		- Export as .txt function
	ChangeLog:
		2021-11-23 (Mickey):
			- Added chips and wounds to character tab (ch. tab complete?)
"""

from tkinter import *
from tkinter import ttk

# Set path
import sys, pathlib
scriptPath = pathlib.Path( __file__ ).parent.resolve();
subfunctionPath = '{}/subfunctions'.format( scriptPath );
sys.path.append( subfunctionPath );

# Import subfunctions
from MDCG_log import db_log
from save_character import save_character
from load_character import load_character

db_log( 'Imported all modules' );

#========Start GUI=======

root = Tk();
root.title('Deadlands Character GUI');
root.geometry('1500x800');

# Create Tab Layout
from generate_tabs import generate_tabs
[tabParent, characterTab, equipmentTab, characterNotesTab, \
				arcaneAbilitiesTab, edgesTab, gameNotesTab, RNGTab] = generate_tabs( root );

# Create Character Tab
from generate_character_tab import generate_character_tab
[charNameTuple, charClassTuple, attrDict, \
     subAtrDict, woundDict, chipDict] = generate_character_tab( characterTab );

	
# Create Equipment Tab
from generate_equipment_tab import generate_equipment_tab
generate_equipment_tab( equipmentTab );

# Create Arcane Abilities Tab
# ~ if( DEBUG_LEVEL == DEBUG_LEVELS['Debug'] ):
	# ~ MDCG_tee('Preparing Arcane Abilities Tab Layout');
testLabel = Label( arcaneAbilitiesTab, text = 'Test Label' );
testLabel.grid( row = 0, column = 0 );
# ~ if( DEBUG_LEVEL == DEBUG_LEVELS['Debug'] ):
	# ~ MDCG_tee('Created Arcane Abilities Tab Layout');
	
# Create Edges and Hindrances Tab
from generate_EandD_tab import generate_EandD_tab
EandD = generate_EandD_tab( edgesTab );

# Create Game Happenings Tab
from generate_game_notes_tab import generate_game_notes_tab
gameNotes = generate_game_notes_tab( gameNotesTab );


# Create Character Notes Tab
from generate_character_notes_tab import generate_character_notes_tab
characterNotes = generate_character_notes_tab( characterNotesTab );

	
# Create RNGesus Tab
from generate_RNG_tab import generate_RNG_tab
generate_RNG_tab( RNGTab );

# Assemble Character
from create_new_character import create_new_character
curChar = create_new_character();

# Create Menubar
from generate_menubar import generate_menubar
menubar = generate_menubar( root, charNameTuple, charClassTuple, attrDict, subAtrDict, woundDict, chipDict, characterNotes, gameNotes );


#=========END GUI============
root.bind( '<Control-s>', lambda event: save_character( charNameTuple, charClassTuple, attrDict, \
                                                       subAtrDict, woundDict, chipDict, characterNotes, gameNotes ) );
root.bind( '<Control-l>', lambda event: load_character( charNameTuple, charClassTuple, attrDict, \
                                                       subAtrDict, woundDict, chipDict, characterNotes, gameNotes) );
root.bind( '<Control-q>', lambda event: root.destroy() );

root.config( menu = menubar );
root.mainloop();
