from tkinter import *
from tkinter import ttk
from MDCG_log import db_log
from copy import deepcopy, copy

import pandas as pd
from config import attrAbr, horseTypes, horseSkills, standardHorse, \
                weaponAttrs, clothesAttrs
from functools import partial

maxRows = 10;
maxCols = 14;

"""
Lessons learned:
    Consider the size of your data before selecting a widget ==> Combobox is a better choice for lots of choices than an entry with dynamic dropdown
"""


def generate_equipment_tab( equipmentTab ):
    
    db_log( 'Preparing Equipment Tab Layout' );
    

    weaponFrame = LabelFrame( equipmentTab, text = 'Weapons', height = 50);
#    [interiorWeaponFrame, weaponCanvas, weaponScrlbar] = generate_scrollbar(weaponFrame, 50);
    
    moneyFrame  = LabelFrame( equipmentTab, text = 'Cash' );
    clothesFrame = LabelFrame( equipmentTab, text = 'Clothing' );
    steedFrame = LabelFrame( equipmentTab, text = 'Mighty Steed' );
    invFrame = LabelFrame( equipmentTab, text = 'Ruck' );
    
    weaponFrame.grid( row = 0, column = 0, columnspan = 2, padx = 10, pady = 10 );
    weaponList = generate_weapon_frame( weaponFrame );
    
    clothesFrame.grid( row = 1, column = 0, padx = 10, pady = 10 );
    clothesList = generate_clothes_frame( clothesFrame );
    
    moneyFrame.grid( row = 1, column = 1, padx = 10, pady = 10 );
    cashVar = StringVar();
    cashEntry = Entry( moneyFrame, textvariable = cashVar, width = 25, borderwidth = 3, justify = "right" );
    cashEntry.grid( row = 0, column = 0 );
    Label( moneyFrame, text = '$' ).grid( row = 0, column = 1 );
    
    # Create Standard Horse with dropdown for modifiers
    steedFrame.grid( row = 2, column = 0, columnspan = 2, padx = 10, pady = 10 );
    steedList = generate_steed_list( steedFrame );
    steedList[2].trace("w", partial(update_steed_stats, steedList));
    
    invFrame.grid( row = 3, column = 0, columnspan = 2, padx = 10, pady = 10 );
    Label( invFrame, text = 'Placeholder' ).pack();
    
    
    # Create basic grid (how do I guarantee that it won't expand beyond the range of the window limits)
    db_log( 'Created Equipment Tab Layout' );
    
    return [cashVar, steedList];

def generate_scrollbar( tab, maxheight = 800 ):
    scrlbar = Scrollbar( tab, orient = VERTICAL );
    scrlbar.grid( row = 0, column = 1, sticky = 'nsew' );
    
    canvas = Canvas( tab, yscrollcommand = scrlbar.set, height = maxheight );
    canvas.grid( row = 0, column = 0, sticky = 'nsew' );
    scrlbar.config( command = canvas.yview );
    
    canvas.xview_moveto(0)
    canvas.yview_moveto(0)
    
    interiorFrame = ttk.Frame( canvas, height = maxheight );
    interior_id = canvas.create_window(0, 0, window=interiorFrame,
                                           anchor=NW)
    interiorFrame.grid(row = 0, column = 0)
    
    def _configure_interior(event):
            # update the scrollbars to match the size of the inner frame
            size = (interiorFrame.winfo_reqwidth(), interiorFrame.winfo_reqheight())
            canvas.config(scrollregion="0 0 %s %s" % size)
            if interiorFrame.winfo_reqwidth() != canvas.winfo_width():
                # update the canvas's width to fit the inner frame
                canvas.config(width=interiorFrame.winfo_reqwidth())
    interiorFrame.bind('<Configure>', _configure_interior)

    def _configure_canvas(event):
        if interiorFrame.winfo_reqwidth() != canvas.winfo_width():
            # update the inner frame's width to fill the canvas
            canvas.itemconfigure(interior_id, width=canvas.winfo_width())
    canvas.bind('<Configure>', _configure_canvas)
    
    return [interiorFrame, canvas, scrlbar]

def generate_clothes_frame( clothesFrame ):
    clothesList = [];
    for iClothes in range( len( clothesAttrs ) ):
        Label( clothesFrame, text = clothesAttrs[iClothes] ).grid( row = 0, column = iClothes, padx = 10, pady = 5 );
    addClothes = Button( clothesFrame, text = "+", command = lambda: add_item_entry( clothesFrame, clothesList, 'clothes' ) );
    
    addClothes.grid( row = 0, column = 4, padx = 0, pady = 5 );
    
def generate_weapon_frame( weaponFrame ):
    
    weaponList = [];
    for iWeapon in range( len( weaponAttrs ) ):
        Label( weaponFrame, text = weaponAttrs[iWeapon] ).grid( row = 0, column = iWeapon, padx = 20, pady = 5 );
    addWeapon = Button( weaponFrame, text = '+', command = lambda: add_item_entry( weaponFrame, weaponList, 'weapon' ) );
    
    addWeapon.grid( row = 0, column = 10, padx = 0, pady = 5 );
    
   
def add_item_entry( frame, itemList, itemClass ):
    numItems = len( itemList );
    db_log( 'Adding weapon entry {}'.format( numItems ) );
    itemEntry = [];
    # Add a row of entries with a combobox first
    if( itemClass == 'weapon' ):
        options = get_item_options(itemClass);
        labels = weaponAttrs;
    elif( itemClass == 'clothes' ):
        options = get_item_options(itemClass);
        labels = clothesAttrs;
    itemBox = ttk.Combobox( frame, width = 40, values = options );
    itemBox.grid( row = numItems + 1, column = 0, padx = 0, pady = 2 );
    
    itemEntry.append( itemBox );
    
    entryStrs = [];
    for iEntry in range( len( labels[1:] ) ):
        entryStrs.append( StringVar() );
        itemEntry.append( entryStrs[iEntry] );
        itemEntry.append( Entry( frame, textvariable = entryStrs[iEntry], width = 10 ) );
        itemEntry[-1].grid( row = numItems + 1, column = iEntry + 1, padx = 0, pady = 2 );
    itemEntry.append( Button( frame, text = '-', command = lambda c = numItems: remove_item_entry( itemList, c ) ) );
    itemEntry[-1].grid( row = numItems + 1, column = iEntry + 2, padx = 0, pady = 2 );
    itemList.append( itemEntry );
    return;

def remove_item_entry( itemList, entryToRemove ):
    db_log( 'Removing weapon entry {}'.format( entryToRemove ) )
    for item in itemList[entryToRemove]:
        try:
            item.destroy();
        except AttributeError:
            continue; #db_log( 'Cannot destroy {}'.format( item ) );
        
    itemList.remove( itemList[entryToRemove] );
    
    # Reassign buttons
    numItems = len( itemList );
    for iItem in range( numItems ):
        itemList[iItem][-1].config( command = lambda c = iItem: remove_item_entry( itemList, c ) );
    
def get_item_options(itemClass):
    itemDir = './data/items/'
    if( itemClass == 'weapon' ):
        shootingTable = pd.read_csv('{}/shooting_irons.csv'.format( itemDir ) );
        fightingTable = pd.read_csv('{}/fighting_weapons.csv'.format( itemDir ) );
        rangedTable   = pd.read_csv('{}/other_ranged_weapons.csv'.format( itemDir ) );
    
        fullTable = pd.concat( [shootingTable, fightingTable, rangedTable] );
        
    elif( itemClass == 'clothes' ):
        hatsTable = pd.read_csv('{}/hats.csv'.format( itemDir ) );
        clothesTable = pd.read_csv( '{}/clothes.csv'.format( itemDir ) );

        fullTable = pd.concat( [hatsTable, clothesTable] );
    
    optionList = list( fullTable['Item'] );
    optionList.sort();
    
    return optionList;


def update_steed_stats( steedList, *args ):
    horseStats = list( standardHorse.keys() );
    specialHorse = steedList[2].get();
    
    # Set special stats
    statVals = deepcopy( standardHorse );
    if( specialHorse == 'Brave' ):
        statVals['Sp'] = '2d8';
        statVals['Guts (Spirit)'] = '4d8';
        noteStr = 'A foolish, brave horse';
    elif( specialHorse == 'Fast' ):
        statVals['Pace'] = '24';
        noteStr = 'Pony Express be darned';
    elif( specialHorse == 'Smart' ):
        noteStr = "+2 to user's Horse Ridin' Skill"
    elif( specialHorse == 'Strong' ):
        statVals['STR'] = '3d12';
        noteStr = "More muscle'n'a Ghost-Stone-Grown Steak";
    elif( specialHorse == 'Surly' ):
        noteStr = 'Bites and kicks with little provocation';
    elif( specialHorse == 'Tough' ):
        noteStr = "From Russia, with love";
        statVals['V'] = '2d12';
    else:
        noteStr = "An ordinary horse. Better'n no horse";
        
    steedList[4].set( noteStr );
        
    for iStat in range( len( horseStats ) ):
        # Find the stat label that corresponds to this stat
        requestedStat = horseStats[iStat];
        standardStat = statVals[requestedStat];
        db_log( 'Attempting to set standard horse stat {} to {}'.format( requestedStat, standardStat ) );
        try:
            steedList[6][requestedStat][1].set( standardStat );
        except (ValueError, KeyError) as e:
            try:
                steedList[7][requestedStat][1].set( standardStat );
            except (ValueError, KeyError) as e2:
                steedList[7]['Terror'][1].set( standardStat );
        
        
    return True;

def generate_steed_list( steedFrame ):
    Label( steedFrame, text = 'Name: ' ).grid( row = 0, column = 0, padx = 5, pady = 5 );
    Label( steedFrame, text = 'Bent: ' ).grid( row = 0, column = 3, padx = 5, pady = 5 );
    Label( steedFrame, text = 'Note: ' ).grid( row = 0, column = 6, padx = 5, pady = 5 );
    nameVar = StringVar();
    specialVar = StringVar();
    noteVar = StringVar();
    steedList = [nameVar, \
                 Entry( steedFrame, textvariable = nameVar, width = 30, borderwidth = 5 ), \
                 specialVar, \
                 OptionMenu( steedFrame, specialVar, *horseTypes ), \
                 noteVar,\
                 Entry( steedFrame, text = noteVar, width = 40, borderwidth = 5 )];
    
    steedList[1].grid( row = 0, column = 1, columnspan = 2, padx = 10, pady = 10 );
    steedList[3].grid( row = 0, column = 4, columnspan = 2, padx = 5, pady = 5 );
    steedList[5].grid( row = 0, column = 7, columnspan = 3, padx = 5, pady = 5 );

    
    attrDict = {};
    curRow = 1;
    curCol = -2;
    attrStrs = [];
    for iCol in range( len( attrAbr ) ):
        curCol += 2;
        if( curCol == maxCols ):
            curCol = 0;
            curRow += 1;
            
        attrStrs.append( StringVar() );
        attrDict[attrAbr[iCol]] = ( Label( steedFrame, text = attrAbr[iCol], font = ('Helvatica', 8) ) ), \
                                    attrStrs[iCol], \
                                    Entry( steedFrame, textvariable = attrStrs[iCol], width = 10, borderwidth = 3, font = ('Helvatica', 8) ) ;
        attrDict[attrAbr[iCol]][0].grid( row = curRow, column = curCol, padx = 10, pady = 10 );
        attrDict[attrAbr[iCol]][2].grid( row = curRow, column = curCol + 1, padx = 10, pady = 10 );

    steedList.append( attrDict );
    db_log( 'After appending attrDict to your trusty steed, steedList is now {} elements long'.format( len( steedList ) ) );
    
    #46 subatributes
    curCol = -2;
    #curRow = 0;
    subAttrStrs = [];
    subAtrDict = {};
    for iSubAtr in range( len( horseSkills ) ):
        curCol += 2;
        
        subAttrStrs.append( StringVar() );
        subAtrDict[horseSkills[iSubAtr]] = (  Label( steedFrame, text = horseSkills[iSubAtr], font = ('Helvatica', 8) ), \
                                              subAttrStrs[iSubAtr], \
                                              Entry( steedFrame, textvariable = subAttrStrs[iSubAtr], width = 5, borderwidth = 3, font = ('Helvatica', 8) ));
        subAtrDict[horseSkills[iSubAtr]][0].grid( row = 3, column = curCol, padx = 10, pady = 10 );
        subAtrDict[horseSkills[iSubAtr]][2].grid( row = 3, column = curCol + 1, padx = 10, pady = 10 );
        
    subAttrStrs.append( StringVar() );
    subAtrDict['Terror'] = (Label( steedFrame, text = 'Terror', font = ('Helvetica', 8 ) ), subAttrStrs[-1], \
                              Entry( steedFrame, textvariable = subAttrStrs[-1], width = 5, borderwidth = 3, font = ('Helvetica', 8 ) ));
    subAtrDict['Terror'][0].grid( row = 3, column = curCol + 2, padx = 10, pady = 10 );
    subAtrDict['Terror'][2].grid( row = 3, column = curCol + 3, padx = 10, pady = 10 );         
    
    steedList.append( subAtrDict );
        
    return steedList;
