import json
from Character import Character
from tkinter import StringVar
from MDCG_log import db_log


def save_character( charNameTuple, charClassTuple, attrDict, subAtrDict, \
                   woundDict, chipDict, characterNotes, gameNotes ):
    #Get Current Character
    curChar = get_current_character(charNameTuple, charClassTuple, attrDict, subAtrDict, woundDict, chipDict, characterNotes, gameNotes)
    db_log( 'Gathered Current Caracter Data' );
    #create JSON dictionary of character
    charJSON = json.dumps( curChar.__dict__, indent = 4 );
    db_log( 'Saving... {}'.format( charJSON ) );
    #write JSON dictionary to file
    f = open( './data/{}.dead'.format( curChar.name ), 'w' );
    f.write( charJSON );
    f.close();
    db_log( 'Saved!' );

def get_current_character( charNameTuple, charClassTuple, attrDict, subAtrDict, woundDict, chipDict, characterNotes, gameNotes ):
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

def all_children (wid) :
    _list = wid.winfo_children()

    for item in _list :
        if item.winfo_children() :
            _list.extend(item.winfo_children())

    return _list
