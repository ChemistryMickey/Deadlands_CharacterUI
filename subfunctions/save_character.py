import json
from Character import Character
from tkinter import StringVar
def save_character( root, woundDict, chipDict ):
    #Get Current Character
    curChar = get_current_character(root, woundDict, chipDict)
                
    #create JSON dictionary of character
    charJSON = json.dumps( curChar.__dict__, indent = 4 );
    
    #write JSON dictionary to file
    f = open( './data/{}.txt'.format( curChar.name ), 'w' );
    f.write( charJSON );
    f.close();

def get_current_character(root, woundDict, chipDict):
    rootList = all_children( root );
    charFrame = rootList[3]; #is it smart to have this hardcoded?
    
    # Get stats in Character Tab
    charChildren = all_children( charFrame );
    for iItem in range( len( charChildren ) ):
        #Print all things in this frame
        print( '{}: {} <{}>'.format( iItem, charChildren[iItem], charChildren[iItem].winfo_class() ) );
        #Check if it's an entry
        charProps = {};
        if( charChildren[iItem].winfo_class() == 'Entry' ):    
            charProps[charChildren[iItem - 1].cget('text')] = charChildren[iItem].get();
#            print( '{}: {}'.format( charChildren[iItem - 1], charChildren[iItem - 1].cget('text') ) );
#            print( '{}: {}'.format( charChildren[iItem], charChildren[iItem].get() ) );
            
        #Check if it's a dropdown
        if( charChildren[iItem].winfo_class() == 'Menubutton' ):    
#            charProps[charChildren[iItem - 1].cget('text')] = charChildren[iItem].get();
            print( '{}: {}'.format( charChildren[iItem - 1], charChildren[iItem - 1].cget('text') ) );
            print( '{}: {}'.format( charChildren[iItem], dir( charChildren[iItem] ) ) );
            print( '{}: {}'.format( charChildren[iItem], charChildren[iItem].get_selection() ) );

    # Get Arcane Abilities in AB tab
    
    # Get EandD in EandD tab
    This is an error test
    # Get Equipment in equipment tab
    
    # Get character notes
    
    # Get game notes
    
    #Build character
    return Character();

def all_children (wid) :
    _list = wid.winfo_children()

    for item in _list :
        if item.winfo_children() :
            _list.extend(item.winfo_children())

    return _list
