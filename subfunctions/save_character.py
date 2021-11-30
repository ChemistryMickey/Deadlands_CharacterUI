import json
from Character import Character
from MDCG_log import db_log
from config import maxEandD
from os.path import exists
from tkinter import messagebox

def save_character( charNameTuple, charClassTuple, attrDict, subAtrDict, \
                   woundDict, chipDict, characterNotes, gameNotes, edgeList, hindList ):
    #Get Current Character
    curChar = get_current_character(charNameTuple, charClassTuple, attrDict, \
                                    subAtrDict, woundDict, chipDict, characterNotes, gameNotes, edgeList, hindList)
    db_log( 'Gathered Current Caracter Data' );
    #create JSON dictionary of character
    charJSON = json.dumps( curChar.__dict__, indent = 4 );
    db_log( 'Saving... {}'.format( charJSON ) );
    #write JSON dictionary to file
    filePath = './data/characters/{}.dead'.format( curChar.name );
    if( exists( filePath ) ):
        overwriteOK = check_if_overwrite_ok();
    
    if( overwriteOK ):
        f = open( filePath, 'w' );
        f.write( charJSON );
        f.close();
        db_log( 'Saved!' );
    return;
    
def check_if_overwrite_ok():
    return messagebox.askokcancel("Overwite Character File", "OK to overwrite existing character?");

def get_current_character( charNameTuple, charClassTuple, attrDict,\
                          subAtrDict, woundDict, chipDict, characterNotes, gameNotes, edgeList, hindList ):
    curChar = Character();
    # Get character name
    curChar.name = charNameTuple[1].get();
    db_log( 'Name: {}'.format( curChar.name ) );
    
    # Get character class
    curChar.charClass = charClassTuple[1].get();
    db_log( 'Class: {}'.format( curChar.charClass ) );
    
    # Get Attributes
    curChar.attrib = {};
    for item in attrDict:
        curChar.attrib[attrDict[item][0]['text']] = attrDict[item][1].get();
#        print( '{}: {} --> {}'.format( item, attrDict[item][0]['text'], attrDict[item][1].get() ) );
    db_log( curChar.attrib );
        
    # Get Subattributes
    curChar.subAttr = {};
    for item in subAtrDict:
        curChar.subAttr[subAtrDict[item][0]['text']] = subAtrDict[item][1].get();
    db_log( curChar.subAttr );

    # Get Arcane Abilities in AB tab
    
    # Get EandD in EandD tab
    curChar.EandD.clear();
    for iEdge in range( maxEandD ):
        curChar.EandD[edgeList[iEdge][0].get()] = {'Value'  : edgeList[iEdge][2].get(), \
                                                   'Effect' : edgeList[iEdge][4].get() }
        
    for iHind in range( maxEandD ):
        curChar.EandD[hindList[iHind][0].get()] = {'Value' : hindList[iHind][2].get(), \
                                                  'Effect' : hindList[iHind][4].get() }
    # Get Equipment in equipment tab
    
    # Get Wounds
    curChar.wounds = {};
    for item in woundDict:
        curChar.wounds[woundDict[item][0]] = woundDict[item][2].get();
    db_log( curChar.wounds );
    # Get Chips
    curChar.chips = {};
    for item in chipDict:
        curChar.chips[chipDict[item][0]['text']] = chipDict[item][1].get();
    db_log( curChar.chips );
    
    # Get character notes
    curChar.charNotes[characterNotes[0]] = characterNotes[1].get("1.0", 'end');
    db_log( curChar.charNotes );
    
    # Get game notes
    curChar.gameNotes[gameNotes[0]] = gameNotes[1].get("1.0", 'end');
    db_log( curChar.gameNotes );
    #Build character
    return curChar;
