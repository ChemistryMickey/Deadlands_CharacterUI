import random
from MDCG_log import db_log
#import itertools


def roll_dice( numSides, numDice, enableExploding, explOffset ):
    diceRolls = [];
    for iDice in range( numDice ):
        randInt = random.randint(1, numSides); #endpoint inclusive
        
        # Allow for explosions
        if( enableExploding == 1 ):
            #Find number required to get exploding dice
            if( explOffset[-1] == 'x' ):
                diceOffset = 0;
            else:
                diceOffset = int( explOffset[-1] );
                
            #Check to make sure that the explosion minimum is at least 1.
            explGoal = numSides - diceOffset;
            if( explGoal <= 1 ):
                explGoal = 2;
                
            #Check if it's exploded
            if( randInt >= explGoal ):
                # If it has, track that dice separately
                curDice = [];
                while( randInt >= explGoal ):
                    curDice.append( randInt );
                    randInt = random.randint(1, numSides);
                    
                curDice.append( randInt );
            else:
                curDice = randInt;
            
        diceRolls.append( curDice );
    
    db_log( 'Rolling {}d{} for: {}'.format( numDice, numSides, diceRolls ) );
    return diceRolls;

def display_dice( diceList, stringVar, sumVar, maxVar ):
    stringVar.set( str( diceList ) );
    maxVal = 0;
    sumVal = 0;
    for item in diceList:
        if( isinstance( item, list ) ):
            for val in item:
                sumVal += val;
            if( sum( item ) > maxVal ):
                maxVal = sum( item );
        else:
            sumVal += item;
            if( item > maxVal ):
                maxVal = item;        
        
    sumVar.set( str( sumVal ) );
    maxVar.set( str( maxVal ) );
    db_log( 'Rolls: {}, Sum: {}, Max: {}'.format( diceList, sumVal, maxVal ) );

def draw_cards( numCards ):
    suitList = ['s', 'h', 'd', 'c'];
    faceList = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'];
    
    extendedDeck = [];
    for suit in suitList:
        for face in faceList:
            extendedDeck.append( (face, suit) );
    
    extendedDeck.extend( [('Joker', 'b'), ('Joker', 'r')] );
    db_log( 'Extended Deck with Jokers: {}'.format( extendedDeck ) );

    # Draw a random number of cards from the list
    drawnCards = [];
    while( len( drawnCards ) < numCards ):
        propRandInd = random.randint( 0, len( extendedDeck ) - 1 );
        if( not( extendedDeck[propRandInd] in drawnCards ) ):
            drawnCards.append( extendedDeck[propRandInd] );
    
    db_log( 'Drawing {} cards: {}'.format( numCards, drawnCards ) );
    return drawnCards;

def display_cards( cardList, cardLabel ):
    cardStr = cardList[0][0] + cardList[0][1];
    if( len( cardList ) > 1 ):        
        for iCard in range( 1, len( cardList ) ):
            cardStr = cardStr + ', ' + cardList[iCard][0] + cardList[iCard][1];
        # ~ cardStr = cardStr + ', ' + cardList[-1][0] + cardList[-1][1];
    
    
    db_log( 'Entering {} into cardLabel'.format( cardStr ) );
    cardLabel.set( cardStr );
    return;
