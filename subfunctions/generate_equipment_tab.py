from tkinter import *
from tkinter import ttk
from MDCG_log import db_log
from copy import deepcopy, copy

import pandas as pd
from config import attrAbr, horseTypes, horseSkills, standardHorse, weaponAttrs
from functools import partial

maxRows = 10;
maxCols = 14;

def generate_equipment_tab( root, equipmentTab ):
    
    db_log( 'Preparing Equipment Tab Layout' );
    weaponFrame = LabelFrame( equipmentTab, text = 'Weapons' );
    moneyFrame  = LabelFrame( equipmentTab, text = 'Cash' );
    clothesFrame = LabelFrame( equipmentTab, text = 'Clothing' );
    steedFrame = LabelFrame( equipmentTab, text = 'Mighty Steed' );
    invFrame = LabelFrame( equipmentTab, text = 'Ruck' );
    
    weaponFrame.grid( row = 0, column = 0, columnspan = 2, padx = 10, pady = 10 );
    weaponList = generate_weapon_frame( root, weaponFrame );
    
    clothesFrame.grid( row = 1, column = 0, padx = 10, pady = 10 );
    clothesAttrs = ['Name', 'Armour', 'Value'];
    for iClothes in range( len( clothesAttrs ) ):
        Label( clothesFrame, text = clothesAttrs[iClothes] ).grid( row = 0, column = iClothes, padx = 10, pady = 5 );
    
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

def generate_weapon_frame( root, weaponFrame ):
    weaponList = [];
    for iWeapon in range( len( weaponAttrs ) ):
        Label( weaponFrame, text = weaponAttrs[iWeapon] ).grid( row = 0, column = iWeapon, padx = 20, pady = 5 );
    addWeapon = Button( weaponFrame, text = '+', command = lambda: add_weapon_entry( root, weaponFrame, weaponList ) );
    removeWeapon = Button( weaponFrame, text = '-', command = lambda: remove_weapon_entry( weaponFrame, weaponList ) );
    
    addWeapon.grid( row = 0, column = 11, padx = 0, pady = 5 );
    removeWeapon.grid( row = 0, column = 12, padx = 0, pady = 5 );
    
        
    
    defaultTuple = (StringVar(), \
                    Entry( weaponFrame, width = 40, borderwidth = 3, font = ('Helvetica', 8) ),\
                    StringVar(),\
                    Entry( weaponFrame, width = 10, borderwidth = 3, font = ('Helvetica', 8) ),\
                    StringVar(),\
                    Entry( weaponFrame, width = 10, borderwidth = 3, font = ('Helvetica', 8 ) ),\
                    StringVar(), \
                    Entry( weaponFrame, width = 10, borderwidth = 3, font = ('Helvetica', 8) ),\
                    StringVar(), \
                    Entry( weaponFrame, width = 10, borderwidth = 3, font = ('Helvetica', 8) ),\
                    StringVar(), \
                    Entry( weaponFrame, width = 10, borderwidth = 3, font = ('Helvetica', 8) ),\
                    StringVar(), \
                    Entry( weaponFrame, width = 10, borderwidth = 3, font = ('Helvetica', 8) ),\
                    StringVar(), \
                    Entry( weaponFrame, width = 10, borderwidth = 3, font = ('Helvetica', 8) ),\
                    StringVar(), \
                    Entry( weaponFrame, width = 10, borderwidth = 3, font = ('Helvetica', 8) ),\
                    StringVar(), \
                    Entry( weaponFrame, width = 10, borderwidth = 3, font = ('Helvetica', 8) ));
    weaponList.append( defaultTuple );
    
    for iCol in range(10):
        weaponList[0][2*iCol + 1].config( textvariable = defaultTuple[2*iCol] );
        weaponList[0][2*iCol + 1].grid( row = 1, column = iCol, padx = 2, pady = 5 );
    
def add_weapon_entry( root, weaponFrame, weaponList ):
    numWeapons = len( weaponList );
    db_log( 'Attempting to add an entry to the weapon table: {} weapons currently'.format( numWeapons ) );
    defaultTuple = (StringVar(), \
                    Entry( weaponFrame, width = 40, borderwidth = 3, font = ('Helvetica', 8) ),\
                    StringVar(),\
                    Entry( weaponFrame, width = 10, borderwidth = 3, font = ('Helvetica', 8) ),\
                    StringVar(),\
                    Entry( weaponFrame, width = 10, borderwidth = 3, font = ('Helvetica', 8) ),\
                    StringVar(), \
                    Entry( weaponFrame, width = 10, borderwidth = 3, font = ('Helvetica', 8) ),\
                    StringVar(), \
                    Entry( weaponFrame, width = 10, borderwidth = 3, font = ('Helvetica', 8) ),\
                    StringVar(), \
                    Entry( weaponFrame, width = 10, borderwidth = 3, font = ('Helvetica', 8) ),\
                    StringVar(), \
                    Entry( weaponFrame, width = 10, borderwidth = 3, font = ('Helvetica', 8 ) ),\
                    StringVar(), \
                    Entry( weaponFrame, width = 10, borderwidth = 3, font = ('Helvetica', 8) ),\
                    StringVar(), \
                    Entry( weaponFrame, width = 10, borderwidth = 3, font = ('Helvetica', 8) ),\
                    StringVar(), \
                    Entry( weaponFrame, width = 10, borderwidth = 3, font = ('Helvetica', 8) ));
    
    requestedWeapon = item_window( root, 'weapon', defaultTuple );
    weaponList.append( defaultTuple );
    
    for iCol in range(10):
        weaponList[-1][2*iCol + 1].config( textvariable = defaultTuple[2*iCol] );
        weaponList[-1][2*iCol + 1].grid( row = numWeapons + 1, column = iCol, padx = 2, pady = 5 );
    db_log( 'Added weapon to row {}'.format( numWeapons + 1 ) );
    
    db_log('Appended new weapon to weapon list: {}'.format( weaponList ) );
    return weaponList;

def item_window( root, itemClass, dataStruct ):
    newWindow = Toplevel( root );
    if( itemClass == 'weapon' ):
        #grab weapon data
        shootingIrons = pd.read_csv('./data/items/shooting_irons.csv');
        db_log('Read Shooting Irons: {}'.format( shootingIrons ) );
        fullList = list( shootingIrons['Item'] );
        
        melee = pd.read_csv( './data/items/fighting_weapons.csv' );
        db_log('Read Melee Weapons: {}'.format( melee ) );
        fullList.extend( list( melee['Item'] ) )
        
        otherRange = pd.read_csv( './data/items/other_ranged_weapons.csv' );
        db_log('Read Other Ranged Weapons: {}'.format( otherRange ) );
        fullList.extend( list( otherRange['Item'] ) );
        
        weaponTableList = [shootingIrons, melee, otherRange];
        fullWeaponTable = pd.concat( weaponTableList );
        
        fullList.sort(); #These are your options for the dropdown
        
        #select labels
        fullLabels = weaponAttrs;
        
    
    #build dropdown of available items (alphabetized please Mickey)
    selectFrame = Frame( newWindow );
    selectFrame.grid(row = 0, column = 0);
    selectVar = StringVar();
    itemMenu = OptionMenu( selectFrame, selectVar, *fullList );
    itemMenu.grid( row = 0, column = 0, padx = 10, pady = 10 );

    #create custom weapon request
    custStrs = {};
    for iLabel in range( len( fullLabels ) ):
        custStrs[fullLabels[iLabel]] = StringVar();
        Label( selectFrame, text = fullLabels[iLabel], width = 15 ).grid( row = 1, column = iLabel, padx = 0, pady = 10 );
        Entry( selectFrame, textvariable = custStrs[fullLabels[iLabel]], width = 15 ).grid( row = 2, column = iLabel, padx = 0, pady = 10 );
    
    #Trace selectVar such that it updates the custStrs if you change the item 
    selectVar.trace("w", partial( update_weapon_choice, selectVar, custStrs, fullWeaponTable ) );
    #Add buttons to confirm or cancel your choice
    # Open window
    newWindow.mainloop();
    
def update_weapon_choice( chosenWeapon, weaponLabels, weaponTable, *args ):
    db_log( 'Requesting {} from Weapons Table'.format( chosenWeapon.get() ) );
    #Get the table entries for the desired weapon
    requestedInd = weaponTable['Item'].values.tolist().index( chosenWeapon.get() );
    
    for label in weaponAttrs:
        weaponLabels[label].set( weaponTable[label].values[requestedInd] );
        
    return;
        

    
    
def remove_weapon_entry( weaponFrame, weaponList ):
    db_log( 'Attempting to remove entry from the weapon table' );
    lastTuple = weaponList[-1];
    for iItem in range( len( lastTuple ) ):
        try:
            lastTuple[iItem].destroy();
        except:
            db_log("Can't destroy {}".format( lastTuple[iItem] ) );
    weaponList.pop(-1);
    return;


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
