from tkinter import *
from tkinter import ttk
from MDCG_log import db_log

import pandas as pd

def generate_equipment_tab( equipmentTab ):
	db_log( 'Preparing Equipment Tab Layout' );
	weaponFrame = LabelFrame( equipmentTab, text = 'Weapons' );
	moneyFrame  = LabelFrame( equipmentTab, text = 'Cash' );
	clothesFrame = LabelFrame( equipmentTab, text = 'Clothing' );
	steedFrame = LabelFrame( equipmentTab, text = 'Mighty Steed' );
	invFrame = LabelFrame( equipmentTab, text = 'Ruck' );
	
	weaponFrame.grid( row = 0, column = 0, columnspan = 2, padx = 10, pady = 10 );
	weaponAttrs = ['Name', 'Shots', 'Caliber', 'RoF', 'Damage', 'Range Incr.', 'Value'];
	for iWeapon in range( len( weaponAttrs ) ):
		Label( weaponFrame, text = weaponAttrs[iWeapon] ).grid( row = 0, column = iWeapon, padx = 20, pady = 5 );
	
	clothesFrame.grid( row = 1, column = 0, padx = 10, pady = 10 );
	clothesAttrs = ['Name', 'Armour', 'Value'];
	for iClothes in range( len( clothesAttrs ) ):
		Label( clothesFrame, text = clothesAttrs[iClothes] ).grid( row = 0, column = iClothes, padx = 10, pady = 5 );
	
	moneyFrame.grid( row = 1, column = 1, padx = 10, pady = 10 );
	cashEntry = Entry( moneyFrame, width = 25, borderwidth = 3, justify = "right" );
	cashEntry.grid( row = 0, column = 0 );
	Label( moneyFrame, text = '$' ).grid( row = 0, column = 1 );
	
	steedFrame.grid( row = 2, column = 0, columnspan = 2, padx = 10, pady = 10 );
	Label( steedFrame, text = 'Placeholder' ).pack();
	
	invFrame.grid( row = 3, column = 0, columnspan = 2, padx = 10, pady = 10 );
	Label( invFrame, text = 'Placeholder' ).pack();
	# Create basic grid (how do I guarantee that it won't expand beyond the range of the window limits)
	exampleData = {'Item' : 'Example', 'Quantity' : 5, 'Individual Value' : 10};
	inv = {};
	db_log( 'Created Equipment Tab Layout' );

