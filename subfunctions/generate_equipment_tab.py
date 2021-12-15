from tkinter import *
from tkinter import ttk
from MDCG_log import db_log
from copy import deepcopy, copy
from os import listdir

import pandas as pd
from config import attrAbr, horseTypes, horseSkills, standardHorse, \
                weaponAttrs, clothesAttrs, ruckAttrs
from functools import partial

maxRows = 10;
maxCols = 14;

"""
Lessons learned:
    Consider the size of your data before selecting a widget ==> Combobox is a better choice for lots of choices than an entry with dynamic dropdown
"""


def generate_equipment_tab( equipmentTab ):
    
    db_log( 'Preparing Equipment Tab Layout' );
    
    [interiorFrame, canvas, scrlbar] = generate_scrollbar( equipmentTab );
    
    weaponFrame = LabelFrame( interiorFrame, text = 'Weapons', height = 50);    
    moneyFrame  = LabelFrame( interiorFrame, text = 'Cash' );
    clothesFrame = LabelFrame( interiorFrame, text = 'Clothing' );
    steedFrame = LabelFrame( interiorFrame, text = 'Mighty Steed' );
    invFrame = LabelFrame( interiorFrame, text = 'Ruck', width = 800 );
    
    weaponFrame.grid( row = 0, column = 0, columnspan = 2, padx = 10, pady = 10, sticky = 'nsew' );
    weaponList = []
    generate_weapon_frame( weaponFrame, weaponList );
    
    clothesFrame.grid( row = 1, column = 0, padx = 10, pady = 10, sticky = 'nsew' );
    clothesList = [];
    generate_clothes_frame( clothesFrame, clothesList );
    
    moneyFrame.grid( row = 1, column = 1, padx = 10, pady = 10, sticky = 'nsew' );
    cashVar = StringVar();
    cashEntry = Entry( moneyFrame, textvariable = cashVar, width = 25, borderwidth = 3, justify = "right" );
    cashEntry.grid( row = 0, column = 0 );
    Label( moneyFrame, text = '$' ).grid( row = 0, column = 1 );
    
    # Create Standard Horse with dropdown for modifiers
    steedFrame.grid( row = 2, column = 0, columnspan = 2, padx = 10, pady = 10, sticky = 'nsew' );
    steedList = generate_steed_list( steedFrame );
    steedList[2].trace("w", partial(update_steed_stats, steedList));
    
    invFrame.grid( row = 3, column = 0, columnspan = 2, padx = 10, pady = 10, sticky = 'nsew' );
    invList = [];
    generate_inventory_frame( invFrame, invList );
    
    
    # Create basic grid (how do I guarantee that it won't expand beyond the range of the window limits)
    db_log( 'Created Equipment Tab Layout' );
    
    frames = [weaponFrame, clothesFrame, invFrame];
    return [cashVar, steedList, weaponList, clothesList, invList, frames];

def generate_inventory_frame( invFrame, invList ):
    for iInv in range( len( ruckAttrs ) ):
        Label( invFrame, text = ruckAttrs[iInv], width = 50 ).grid( row = 0, column = iInv, padx = 10, pady = 5 );
    addItem = Button( invFrame, text = "+", command = lambda: add_item_entry( invFrame, invList, 'ruck' ) );
    
    addItem.grid( row = 0, column = 3, padx = 0, pady = 0 );
    
    return invList;


def generate_clothes_frame( clothesFrame, clothesList ):
    for iClothes in range( len( clothesAttrs ) ):
        Label( clothesFrame, text = clothesAttrs[iClothes] ).grid( row = 0, column = iClothes, padx = 10, pady = 5 );
    addClothes = Button( clothesFrame, text = "+", command = lambda: add_item_entry( clothesFrame, clothesList, 'clothes' ) );
    
    addClothes.grid( row = 0, column = 3, padx = 0, pady = 0 );
    
    return clothesList;
    
def generate_weapon_frame( weaponFrame, weaponList ):
    for iWeapon in range( len( weaponAttrs ) ):
        Label( weaponFrame, text = weaponAttrs[iWeapon] ).grid( row = 0, column = iWeapon, padx = 20, pady = 5 );
    addWeapon = Button( weaponFrame, text = '+', command = lambda: add_item_entry( weaponFrame, weaponList, 'weapon' ) );
    
    addWeapon.grid( row = 0, column = 10, padx = 0, pady = 0 );
    
    return weaponList;
    
   
def add_item_entry( frame, itemList, itemClass ):
    # Item Entry Structure [ComboBox, entryStrs[iEntry], entry, ..., Button, ComboBoxStr]
    numItems = get_num_item_rows( frame );
    db_log( 'Adding {} entry {}'.format( itemClass, numItems ) );
    
    options = get_item_options(itemClass);
    if( itemClass == 'weapon' ):        
        labels = weaponAttrs;
    elif( itemClass == 'clothes' ):
        labels = clothesAttrs;
    elif( itemClass == 'ruck' ):
        labels = ruckAttrs;
    
    itemEntry = [];
    combStr = StringVar();
    itemBox = ttk.Combobox( frame, width = 30, textvariable = combStr, values = options );
    itemBox.grid( row = numItems + 1, column = 0, padx = 0, pady = 0 );
    
    itemEntry.append( itemBox );
    
    entryStrs = [];
    for iEntry in range( len( labels[1:] ) ):
        entryStrs.append( StringVar() );
        itemEntry.append( entryStrs[iEntry] );
        itemEntry.append( Entry( frame, textvariable = entryStrs[iEntry], width = 10 ) );
        itemEntry[-1].grid( row = numItems + 1, column = iEntry + 1, padx = 0, pady = 0 );
    itemEntry.append( Button( frame, text = '-', command = lambda c = numItems: remove_item_entry( itemList, itemClass, c ) ) );
    itemEntry[-1].grid( row = numItems + 1, column = iEntry + 2, padx = 0, pady = 0 );
    itemEntry.append( combStr );
    itemList.append( itemEntry );
    
    def update_entries(itemClass, *args):
        db_log( 'Updating item entries' );
        try:
            propDict = get_item_props(itemClass, combStr.get());
                
            for iEntry in range( len( labels[1:] ) ):
                entryStrs[iEntry].set( propDict[labels[iEntry + 1]] );
        except:
            return; #may be a custom entry and that's OK
    
    combStr.trace("w", partial( update_entries, itemClass ) );
    
    #Reassign buttons in case of load
    numItems = len( itemList );
    for iItem in range( numItems ):
        itemList[iItem][-2].config( command = lambda c = iItem: remove_item_entry( itemList, itemClass, c ) );
        
    return itemList;

def get_num_item_rows( frame ):
    numItems = 0;
    for item in frame.children:
        if( 'combo' in str( item )  ):
            numItems += 1;
    #count the number of comboboxes to get the number of items
    return numItems;
  
def get_item_props( itemClass, itemName ):
    itemDir = './data/items'
    if( itemClass == 'weapon' ):
        shootingTable = pd.read_csv('{}/shooting_irons.csv'.format( itemDir ) );
        fightingTable = pd.read_csv('{}/fighting_weapons.csv'.format( itemDir ) );
        rangedTable   = pd.read_csv('{}/other_ranged_weapons.csv'.format( itemDir ) );
    
        fullTable = pd.concat( [shootingTable, fightingTable, rangedTable] );
        
    elif( itemClass == 'clothes' ):
        hatsTable = pd.read_csv('{}/hats.csv'.format( itemDir ) );
        clothesTable = pd.read_csv( '{}/clothes.csv'.format( itemDir ) );

        fullTable = pd.concat( [hatsTable, clothesTable] );
    elif( itemClass == 'ruck' ):
        #LOAD EVERY CSV. LOAD THEM ALL!!!!
        csvList = [];
        for csv in listdir( './data/items' ):
            csvList.append( pd.read_csv('./data/items/{}'.format( csv ) ) );
            
        fullTable = pd.concat( csvList );
        
    requestedIndex = list(fullTable['Item'].values).index(itemName);
    keys = list( fullTable.keys() );
    properties = {};
    for key in keys:
        properties[key] = fullTable[key].values[requestedIndex];
    
    return properties;
    
def remove_item_entry( itemList, itemClass, entryToRemove ):
    db_log( 'Removing {} entry {}'.format( itemClass, entryToRemove ) )
    for item in itemList[entryToRemove]:
        try:
            item.destroy();
        except AttributeError:
            continue; #db_log( 'Cannot destroy {}'.format( item ) );
        
    itemList.remove( itemList[entryToRemove] );
    
    # Reassign buttons
    numItems = len( itemList );
    for iItem in range( numItems ):
        itemList[iItem][-2].config( command = lambda c = iItem: remove_item_entry( itemList, itemClass, c ) );
    
def get_item_options(itemClass):
    itemDir = './data/items'
    if( itemClass == 'weapon' ):
        shootingTable = pd.read_csv('{}/shooting_irons.csv'.format( itemDir ) );
        fightingTable = pd.read_csv('{}/fighting_weapons.csv'.format( itemDir ) );
        rangedTable   = pd.read_csv('{}/other_ranged_weapons.csv'.format( itemDir ) );
    
        fullTable = pd.concat( [shootingTable, fightingTable, rangedTable] );
        
    elif( itemClass == 'clothes' ):
        hatsTable = pd.read_csv('{}/hats.csv'.format( itemDir ) );
        clothesTable = pd.read_csv( '{}/clothes.csv'.format( itemDir ) );

        fullTable = pd.concat( [hatsTable, clothesTable] );
    
    elif( itemClass == 'ruck' ):
        #LOAD EVERY CSV. LOAD THEM ALL!!!!
        csvList = [];
        for csv in listdir( './data/items' ):
            csvList.append( pd.read_csv('./data/items/{}'.format( csv ) ) );
            
        fullTable = pd.concat( csvList );
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

def generate_scrollbar( tab, maxheight = 800 ):
    scrlbar = Scrollbar( tab, orient = VERTICAL );
    scrlbar.pack( fill = Y, side = RIGHT );
    
    canvas = Canvas( tab, yscrollcommand = scrlbar.set );
    canvas.pack( expand = 1, fill = BOTH );
    scrlbar.config( command = canvas.yview );
    
    canvas.xview_moveto(0)
    canvas.yview_moveto(0)
    
    interiorFrame = ttk.Frame( tab, height = maxheight );
    interior_id = canvas.create_window(0, 0, window=interiorFrame, anchor=NW)
#    interiorFrame.pack(expand = 1, fill = BOTH)
    
    scrlbar.lift(interiorFrame);
        
    def _bound_to_mousewheel(event):
        canvas.bind_all("<MouseWheel>", _on_mousewheel)   

    def _unbound_to_mousewheel(event):
        canvas.unbind_all("<MouseWheel>") 

    def _on_mousewheel(event):
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")  
        
    def _configure_interior(event):
            # update the scrollbars to match the size of the inner frame
            size = (interiorFrame.winfo_reqwidth(), interiorFrame.winfo_reqheight())
            canvas.config(scrollregion="0 0 %s %s" % size)
            if interiorFrame.winfo_reqwidth() != canvas.winfo_width():
                # update the canvas's width to fit the inner frame
                canvas.config(width=interiorFrame.winfo_reqwidth());    

    def _configure_canvas(event):
        if interiorFrame.winfo_reqwidth() != canvas.winfo_width():
            # update the inner frame's width to fill the canvas
            canvas.itemconfigure(interior_id, width=canvas.winfo_width())
            
            
    canvas.bind('<Configure>', _configure_canvas)
    interiorFrame.bind('<Configure>', _configure_interior)
    scrlbar.bind('<Enter>', _bound_to_mousewheel)
    scrlbar.bind('<Leave>', _unbound_to_mousewheel)
    return [interiorFrame, canvas, scrlbar]