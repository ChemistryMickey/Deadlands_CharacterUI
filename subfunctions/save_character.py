import json
from Character import Character
from MDCG_log import db_log
from config import maxEandD
from os.path import exists
from tkinter import messagebox

def save_character( charNameTuple, charClassTuple, attrDict, subAtrDict, \
                   woundDict, chipDict, characterNotes, gameNotes, edgeList, hindList, equipList ):
    #Get Current Character
    curChar = get_current_character(charNameTuple, charClassTuple, attrDict, \
                                    subAtrDict, woundDict, chipDict, characterNotes, gameNotes, edgeList, hindList, equipList)
    db_log( 'Gathered Current Caracter Data' );
    #create JSON dictionary of character
    charJSON = json.dumps( curChar.__dict__, indent = 4 );
    db_log( 'Saving... {}'.format( charJSON ) );
    #write JSON dictionary to file
    filePath = './data/characters/{}.dead'.format( curChar.name );
    if( exists( filePath ) ):
        overwriteOK = check_if_overwrite_ok();
    else:
        overwriteOK = True;
    
    if( overwriteOK ):
        f = open( filePath, 'w' );
        f.write( charJSON );
        f.close();
        db_log( 'Saved!' );
    return;
    
def check_if_overwrite_ok():
    return messagebox.askokcancel("Overwite Character File", "OK to overwrite existing character?");

def get_current_character( charNameTuple, charClassTuple, attrDict,\
                          subAtrDict, woundDict, chipDict, characterNotes, gameNotes, edgeList, hindList, equipList ):
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
    curChar.edges.clear();
    for iEdge in range( len( edgeList ) ):
        curChar.edges[edgeList[iEdge][0].get()] = {'Value'  : edgeList[iEdge][2].get(), \
                                                   'Effect' : edgeList[iEdge][4].get() }
    curChar.hinds.clear();    
    for iHind in range( len( hindList ) ):
        curChar.hinds[hindList[iHind][0].get()] = {'Value' : hindList[iHind][2].get(), \
                                                  'Effect' : hindList[iHind][4].get() }
    # Get Equipment in equipment tab
    curChar.equip = {'Cash' : equipList[0].get()};
    
    curChar.equip['weapons'] = {};
    for iWeap in range( len( equipList[2] ) ):
        curWeapon = equipList[2][iWeap][-1].get();
        curShots = equipList[2][iWeap][3].get();
        curChar.equip['weapons'][curWeapon] = curShots;
        
    curChar.equip['clothes'] = {};
    db_log( 'Clothes Equipment List: {}'.format( equipList[3] ) );
    for iCloth in range( len( equipList[3] ) ):
        curChar.equip['clothes'][equipList[3][iCloth][-1].get()] = 0;
    
    curChar.equip['inventory'] = {};
    for iInv in range( len( equipList[4] ) ):
        curItem = equipList[4][iInv][-1].get()
        itemQuant = equipList[4][iInv][3].get();
        curChar.equip['inventory'][curItem] = itemQuant; #get quantity
    
    #Horse
    # Get every entry in the steed list
    curChar.equip['horse'] = {};
    curChar.equip['horse']['name'] = equipList[1][0].get();
    curChar.equip['horse']['special'] = equipList[1][2].get();
    curChar.equip['horse']['note'] = equipList[1][4].get();
    for iTObj in range( len( equipList[1] ) ):
        curObj = equipList[1][iTObj];
        #db_log( 'Object type: {}'.format( type(curObj) ) );
        if(  str(type(curObj)) == "<class 'dict'>" ): 
            #then it's a stat dictionary
            curDict = equipList[1][iTObj];
            dictKeys = list( curDict.keys() );
            for key in dictKeys:
                db_log( 'Appending {} to "horse" {}'.format( curDict[key][1].get(), key ) );
                curChar.equip['horse'][key] = curDict[key][1].get();
    
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
