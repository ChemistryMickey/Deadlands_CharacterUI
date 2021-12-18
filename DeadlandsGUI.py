"""
	Tkinter GUI for Deadlands Players
	
	
	Author: Mickey T Da Silva
	Version: 0.1
	ToDo:
		- Create Arcane Abilities Tab
        
    Reach Goals:
        - Create character creation widget
        - Create encounter tracker
		- Export as .txt function        
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

ttkCanvas = Canvas( root, width = 1500, height = 800 );
ttkCanvas.grid( row = 0, column = 0 );

# Create Tab Layout
from generate_tabs import generate_tabs
[tabParent, characterTab, equipmentTab, characterNotesTab, \
				arcaneAbilitiesTab, edgesTab, gameNotesTab, RNGTab, figuresTab] = generate_tabs( ttkCanvas );

# Create Character Tab
from generate_character_tab import generate_character_tab
[charNameTuple, charClassTuple, attrDict, \
     subAtrDict, woundDict, chipDict] = generate_character_tab( characterTab );

	
# Create Equipment Tab
from generate_equipment_tab import generate_equipment_tab
equipList = generate_equipment_tab( equipmentTab );

# Create Arcane Abilities Tab
testLabel = Label( arcaneAbilitiesTab, text = "Blank until my Marshal gives me permisssion to read Arcane Abilities section of Player's Guide" );
testLabel.grid( row = 0, column = 0 );
	
# Create Edges and Hindrances Tab
from generate_EandD_tab import generate_EandD_tab
[edgeList, hindList] = generate_EandD_tab( edgesTab );

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

# Place useful figures
from generate_useful_figures_tab import generate_useful_figures
[images, imageLabels] = generate_useful_figures( figuresTab );

# Create Menubar
from generate_menubar import generate_menubar
menubar = generate_menubar( root, charNameTuple, charClassTuple, attrDict, \
                       subAtrDict, woundDict, chipDict, \
                       characterNotes, gameNotes, edgeList, hindList, equipList );


#=========END GUI============
                           
root.bind( '<Control-s>', lambda event: save_character( charNameTuple, charClassTuple, attrDict, \
                                                       subAtrDict, woundDict, chipDict, characterNotes, \
                                                       gameNotes, edgeList, hindList, equipList ) );
root.bind( '<Control-l>', lambda event: load_character( charNameTuple, charClassTuple, attrDict, \
                                                       subAtrDict, woundDict, chipDict, characterNotes, \
                                                       gameNotes, edgeList, hindList, equipList) );
root.bind( '<Control-q>', lambda event: root.destroy() );

root.config( menu = menubar );
root.mainloop();
