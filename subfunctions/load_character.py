from MDCG_log import db_log
from tkinter import filedialog as fd
import json
from copy import deepcopy 
from config import attributeLabels, subAttributeLabels, maxEandD,\
                bodyPartLabels, bodyPartAbbr, chipNames, chipTypes, \
                standardHorse, horseSkills, attrAbr

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
    equipList[1][0].set( curEquip['horse']['name'] );
    equipList[1][2].set( curEquip['horse']['special'] );
    equipList[1][4].set( curEquip['horse']['note'] );
    
    horseStats = list( standardHorse.keys() ); 
    
    specialHorse = curEquip['horse']['special'];
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
        
    equipList[1][4].set( noteStr );
    
    for iStat in range( len( horseStats ) ):
        # Find the stat label that corresponds to this stat
        requestedStat = horseStats[iStat];
        standardStat = statVals[requestedStat];
        db_log( 'Attempting to set standard horse stat {} to {}'.format( requestedStat, standardStat ) );
        try:
            equipList[1][6][requestedStat][1].set( standardStat );
        except (ValueError, KeyError) as e:
            try:
                equipList[1][7][requestedStat][1].set( standardStat );
            except (ValueError, KeyError) as e2:
                equipList[1][7]['Terror'][1].set( standardStat );
            
        
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
    