from tkinter import *
from tkinter import ttk
from MDCG_log import db_log
from copy import deepcopy

import pandas as pd
from config import attrAbr, horseTypes, horseSkills, standardHorse
from functools import partial

maxRows = 10;
maxCols = 14;


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
    exampleData = {'Item' : 'Example', 'Quantity' : 5, 'Individual Value' : 10};
    inv = {};
    db_log( 'Created Equipment Tab Layout' );
    
    return [cashVar];

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
            statInd = attrAbr.index( horseStats[iStat] );
            steedList[6][requestedStat][1].set( standardStat );
        except ValueError:
            try:
                statInd = horseSkills.index( horseStats[iStat] );
                steedList[7][requestedStat][1].set( standardStat );
            except ValueError:
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
    steedList[5].grid( row = 0, column = 7, columnspan = 2, padx = 5, pady = 5 );

    
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
