from tkinter import *
from tkinter import ttk
from MDCG_log import db_log


def generate_character_tab( characterTab ):
    db_log( 'Preparing Character Tab' );
    
    mainFrame = Frame( characterTab );
    attrFrame = Frame( characterTab );
    subAttrFrame = Frame( characterTab );
    woundFrame = Frame( characterTab );
    chipFrame = Frame( characterTab );
    
    mainFrame.grid( row = 0, column = 0, columnspan = 2, padx = 10, pady = 10 );
    attrFrame.grid( row = 1, column = 0, columnspan = 2, padx = 10, pady = 10 );
    subAttrFrame.grid( row = 2, column = 0, columnspan = 2, padx = 10, pady = 10 );
    woundFrame.grid( row = 3, column = 0, padx = 10, pady = 10 );
    chipFrame.grid( row = 3, column = 1, padx = 10, pady = 10 );
    
    charNameLabel = Label( mainFrame, text = 'Character Name:' );
    charNameLabel.grid( row = 0, column = 0, padx = 10, pady = 10 );
    charName = Entry( mainFrame, width = 35, borderwidth = 5 );
    charName.grid( row = 0, column = 1, columnspan = 3, padx = 10, pady = 10 );
    charNameTuple = (charNameLabel, charName);

    charClassLabel = Label( mainFrame, text = 'Class: ' );
    charClassLabel.grid( row = 0, column = 4, padx = 10, pady = 10 );
    className = Entry( mainFrame, width = 30, borderwidth = 5 );
    className.grid( row = 0, column = 5, columnspan = 2, padx = 10, pady = 10 );
    charClassTuple = (charClassLabel, className);
    maxRows = 8;
    
    # Going with a dictionary with 'attr' : ('attribute', Label, Entry)
    from config import attrAbr, attributeLabels
    attrDict = {};
    curRow = 0;
    curCol = -2;
    halfAttr = int( len( attrAbr ) / 2 );
    for iCol in range( 0, halfAttr ):
        curCol += 2;
        attrDict[attrAbr[iCol]] = (Label( attrFrame, text = attributeLabels[iCol] ), Entry( attrFrame, width = 10, borderwidth = 3 ));
        attrDict[attrAbr[iCol]][0].grid( row = 0, column = curCol, padx = 10, pady = 10 );
        attrDict[attrAbr[iCol]][1].grid( row = 0, column = curCol + 1, padx = 10, pady = 10 );
        
        attrDict[attrAbr[iCol + halfAttr]] = (Label( attrFrame, text = attributeLabels[iCol + halfAttr] ), Entry( attrFrame, width = 10, borderwidth = 3 ));
        attrDict[attrAbr[iCol + halfAttr]][0].grid( row = 1, column = curCol, padx = 10, pady = 10 );
        attrDict[attrAbr[iCol + halfAttr]][1].grid( row = 1, column = curCol + 1, padx = 10, pady = 10 );
        

    #46 subatributes
    from config import subAtrAbr, subAttributeLabels
    curCol = 0;
    curRow = 0;
    subAtrDict = {};
    for iSubAtr in range( len( subAtrAbr ) ):
        curRow += 1;
        subAtrDict[subAtrAbr[iSubAtr]] = (Label( subAttrFrame, text = subAttributeLabels[iSubAtr], font = ('Helvatica', 8) ), \
                                                     Entry( subAttrFrame, width = 5, borderwidth = 3, font = ('Helvatica', 8) ));
        subAtrDict[subAtrAbr[iSubAtr]][0].grid( row = curRow, column = curCol, padx = 10, pady = 10 );
        subAtrDict[subAtrAbr[iSubAtr]][1].grid( row = curRow, column = curCol + 1, padx = 10, pady = 10 );
        
        if( curRow == maxRows ):
            curRow = 0;
            curCol += 2;
    
    # Wounds
    woundLevels = ['None', 'Light', 'Heavy', 'Serious', 'Critical', 'Maimed'];
    bodyPartLabels = ['Head', 'R. Arm', 'L. Arm', 'Guts', 'R. Leg', 'L. Leg'];
    bodyPartAbbr = ['head', 'rarm', 'larm', 'guts', 'rleg', 'lleg'];
    woundVals = [];
    woundDict = {};
    for iPart in range( len( bodyPartAbbr ) ):
        woundVals.append( StringVar() );
        woundVals[iPart].set( woundLevels[0] );
        woundDict[bodyPartAbbr[iPart]] = (bodyPartLabels[iPart], Label( woundFrame, text = bodyPartLabels[iPart] ), \
                                                        woundVals[iPart], OptionMenu( woundFrame, woundVals[iPart], *woundLevels ));
    
    curCol = -2;
    for iPart in range( int( len( bodyPartAbbr ) / 2 ) ):
        curCol += 2;
        woundDict[bodyPartAbbr[iPart]][1].grid( row = 0, column = curCol, padx = 10, pady = 10 );
        woundDict[bodyPartAbbr[iPart]][3].grid( row = 0, column = curCol + 1, padx = 10, pady = 10 );
        
        woundDict[bodyPartAbbr[iPart + int( len( bodyPartAbbr ) / 2 ) ]][1].grid( row = 1, column = curCol, padx = 10, pady = 10 );
        woundDict[bodyPartAbbr[iPart + int( len( bodyPartAbbr ) / 2 ) ]][3].grid( row = 1, column = curCol + 1, padx = 10, pady = 10 );
        
    #Chips
    chipNames = ['White Chips', 'Red Chips', 'Blue Chips', 'Green Chips'];
    chipTypes = ['white', 'red', 'blue', 'green'];
    chipVals = [StringVar(), StringVar(), StringVar(), StringVar()]
    chipRange = range(0, 7);
    chipDict  = {};
    for iChip in range( len( chipNames ) ):
        chipVals[iChip].set(0); #default
        chipDict[chipTypes[iChip]] = (Label( chipFrame, text = chipNames[iChip] ), chipVals[iChip], OptionMenu( chipFrame, chipVals[iChip], *chipRange ));
        chipDict[chipTypes[iChip]][0].grid( row = 0, column = iChip * 2, padx = 10, pady = 10 );
        chipDict[chipTypes[iChip]][2].grid( row = 0, column = iChip * 2 + 1, padx = 10, pady = 10 );

    db_log( 'Created Character Tab' );
    return [charNameTuple, charClassTuple, attrDict, subAtrDict, woundDict, chipDict];