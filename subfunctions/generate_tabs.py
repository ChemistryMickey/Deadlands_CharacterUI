from tkinter import *
from tkinter import ttk
from MDCG_log import db_log


def generate_tabs( root ):
	db_log( 'Preparing Tabs' );

	# ~ # Initialize style
	# ~ s = ttk.Style()
	# ~ # Create style used by default for all Frames
	# ~ s.configure('TFrame', background='green')

	tabParent 				= ttk.Notebook( root );
	characterTab 			= ttk.Frame( tabParent );
	equipmentTab 			= ttk.Frame( tabParent );
	characterNotesTab 	= ttk.Frame( tabParent );
	arcaneAbilitiesTab 	= ttk.Frame( tabParent );
	edgesTab 				= ttk.Frame( tabParent );
	gameNotesTab 			= ttk.Frame( tabParent );
	RNGTab 					= ttk.Frame( tabParent );

	tabParent.add( characterTab, text = 'Character' );
	tabParent.add( equipmentTab, text = 'Equipment' );
	tabParent.add( arcaneAbilitiesTab, text = 'Arcane Abilities' );
	tabParent.add( edgesTab, text = 'Edges and Hindrances' );
	tabParent.add( gameNotesTab, text = 'Game Notes' );
	tabParent.add( characterNotesTab, text = 'Character Notes' );
	tabParent.add( RNGTab, text = 'Temple of RNGesus' );

	tabParent.pack( expand = 1, fill = 'both' );
	
	db_log( 'Created Tabs' );
	
	return [tabParent, characterTab, equipmentTab, characterNotesTab, \
				arcaneAbilitiesTab, edgesTab, gameNotesTab, RNGTab];
