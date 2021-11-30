from MDCG_log import db_log
from tkinter import filedialog as fd
import json

from config import attributeLabels, subAttributeLabels, maxEandD,\
                bodyPartLabels, bodyPartAbbr, chipNames, chipTypes

def load_character(charNameTuple, charClassTuple, attrDict, \
                       subAtrDict, woundDict, chipDict, \
                       characterNotes, gameNotes, edgeList, hindList, equipList):
    curCharFile = open_character_file();
    db_log( 'Successfully opened {} file!'.format( curCharFile ) );
    
    curChar = read_character_file(curCharFile);
    db_log( 'Successfully read character: {}'.format( curChar ) );
    
    write_character_to_GUI( curChar, charNameTuple, charClassTuple, attrDict, \
                           subAtrDict, woundDict, chipDict, \
                           characterNotes, gameNotes, edgeList, hindList, equipList );
    db_log( 'Successfully wrote character data to GUI!' );
    
def open_character_file():
    # use UI getter to get character file
    filetypes = (('Deadlands Character File', '*.dead'), ('All Files', '*.*'));
    filename = fd.askopenfilename( title = 'Open a Character', initialdir = './data/characters', filetypes = filetypes );
    
    return filename; 
    
def read_character_file( curCharFile ):
    f = open( curCharFile );
    loadedChar = json.load( f ); #well that was easy
    f.close();
    
    return loadedChar;
    
def write_character_to_GUI( curChar, charNameTuple, charClassTuple, attrDict, \
                           subAtrDict, woundDict, chipDict, \
                           characterNotes, gameNotes, edgeList, hindList, equipList ):
    charNameTuple[1].set(curChar['name']);
    charClassTuple[1].set(curChar['charClass']);
    
    #Write Attributes
    curAttrs = curChar['attrib']; #This is a dictionary with the Attribute Labels as the keys
    for iAttr in range( len( attributeLabels ) ):
        attrDict[attributeLabels[iAttr]][1].set( curAttrs[attributeLabels[iAttr]] );
        
    #Write Subattributes
    curSubAttrs = curChar['subAttr']; #dictionary with subAttributeLabels as keys
    for iSub in range( len( subAttributeLabels ) ):
        subAtrDict[subAttributeLabels[iSub]][1].set( curSubAttrs[subAttributeLabels[iSub]] );
        
    #Write Wounds
    curWounds = curChar['wounds']; #dict with bodyPartLabels as keys
    for iPart in range( len( bodyPartAbbr ) ):
        woundDict[bodyPartAbbr[iPart]][2].set( curWounds[bodyPartLabels[iPart]] );
        
    #Write Chips
    curChips = curChar['chips']; #dict with chipNames as keys
    for iChip in range( len( chipNames ) ):
        chipDict[chipTypes[iChip]][1].set( curChips[chipNames[iChip]] );
    
    #Write Equipment
    curEquip = curChar['equip'];
    equipList[0].set( curEquip['Cash'] );
    #Write AA
    
    #Write EandD
    curEandD = curChar['EandD'];
    curEandD_keys = list( curEandD.keys() );
    db_log( 'Current Edges and Hinderances: {}'.format( curEandD_keys ) );
    if( curEandD_keys[0] != '' ):
        for iEdge in range( maxEandD ):
            edgeList[iEdge][0].set( curEandD_keys[iEdge] );
            edgeList[iEdge][2].set( curEandD[curEandD_keys[iEdge]]['Value'] );
            edgeList[iEdge][4].set( curEandD[curEandD_keys[iEdge]]['Effect'] );
        
        for iHind in range( maxEandD ):
            hindList[iHind][0].set( curEandD_keys[iHind + maxEandD] );
            hindList[iHind][2].set( curEandD[curEandD_keys[iHind + maxEandD]]['Value'] );
            hindList[iHind][4].set( curEandD[curEandD_keys[iHind + maxEandD]]['Effect'] );
        
    #Write Game Notes
    curLog = curChar['gameNotes'];
    gameNotes[1].insert( "1.0", curLog['Game Notes'] );
    
    #Write Character Notes
    curNotes = curChar['charNotes'];
    characterNotes[1].insert( "1.0", curNotes['Character Notes'] );
    return;
    