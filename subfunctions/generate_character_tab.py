from tkinter import *
from tkinter import ttk
from MDCG_log import db_log

from config import attributeLabels, subAttributeLabels, woundLevels, bodyPartLabels, bodyPartAbbr, chipNames, chipTypes

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
    charNameStr = StringVar();
    charName = Entry( mainFrame, textvariable = charNameStr, width = 35, borderwidth = 5 );
    charName.grid( row = 0, column = 1, columnspan = 3, padx = 10, pady = 10 );
    charNameTuple = (charNameLabel, charNameStr, charName);

    charClassLabel = Label( mainFrame, text = 'Class: ' );
    charClassLabel.grid( row = 0, column = 4, padx = 10, pady = 10 );
    classStr = StringVar();
    className = Entry( mainFrame, textvariable = classStr, width = 30, borderwidth = 5 );
    className.grid( row = 0, column = 5, columnspan = 2, padx = 10, pady = 10 );
    charClassTuple = (charClassLabel, classStr, className);
    maxRows = 8;
    maxCols = 14;
    
    # Going with a dictionary with 'attr' : ('attribute', Label, Entry)
    attrDict = {};
    curRow = 0;
    curCol = -2;
    attrStrs = [];
    for iCol in range( len( attributeLabels ) ):
        curCol += 2;
        if( curCol == maxCols ):
            curCol = 0;
            curRow += 1;
            
        attrStrs.append( StringVar() );
        attrDict[attributeLabels[iCol]] = (Label( attrFrame, text = attributeLabels[iCol] ), attrStrs[iCol], Entry( attrFrame, textvariable = attrStrs[iCol], \
                                    width = 10, borderwidth = 3 ));
        attrDict[attributeLabels[iCol]][0].grid( row = curRow, column = curCol, padx = 10, pady = 10 );
        attrDict[attributeLabels[iCol]][2].grid( row = curRow, column = curCol + 1, padx = 10, pady = 10 );

    #46 subatributes
    curCol = 0;
    curRow = 0;
    subAttrStrs = [];
    subAtrDict = {};
    for iSubAtr in range( len( subAttributeLabels ) ):
        curRow += 1;
        
        subAttrStrs.append( StringVar() );
        subAtrDict[subAttributeLabels[iSubAtr]] = (Label( subAttrFrame, text = subAttributeLabels[iSubAtr], font = ('Helvatica', 8) ), subAttrStrs[iSubAtr], \
                                                     Entry( subAttrFrame, textvariable = subAttrStrs[iSubAtr], width = 5, borderwidth = 3, font = ('Helvatica', 8) ));
        subAtrDict[subAttributeLabels[iSubAtr]][0].grid( row = curRow, column = curCol, padx = 10, pady = 10 );
        subAtrDict[subAttributeLabels[iSubAtr]][2].grid( row = curRow, column = curCol + 1, padx = 10, pady = 10 );
        
        if( curRow == maxRows ):
            curRow = 0;
            curCol += 2;
    
    # Wounds
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
    chipVals = [StringVar(), StringVar(), StringVar(), StringVar()]
    chipRange = range(0, 10);
    chipDict  = {};
    for iChip in range( len( chipNames ) ):
        chipVals[iChip].set(0); #default
        chipDict[chipTypes[iChip]] = (Label( chipFrame, text = chipNames[iChip] ), chipVals[iChip], OptionMenu( chipFrame, chipVals[iChip], *chipRange ));
        chipDict[chipTypes[iChip]][0].grid( row = 0, column = iChip * 2, padx = 10, pady = 10 );
        chipDict[chipTypes[iChip]][2].grid( row = 0, column = iChip * 2 + 1, padx = 10, pady = 10 );

    db_log( 'Created Character Tab' );
    return [charNameTuple, charClassTuple, attrDict, subAtrDict, woundDict, chipDict];