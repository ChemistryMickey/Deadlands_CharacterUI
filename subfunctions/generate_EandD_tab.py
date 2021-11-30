from tkinter import *
from config import maxEandD
from MDCG_log import db_log

from pandas import read_csv 
from numpy import zeros
from copy import deepcopy #so we can reuse lists

entryWidth = 150;
wrapLength = 1000;

def generate_EandD_tab( edgesTab ):
    # Create Label Frames
    edgeFrame = LabelFrame( edgesTab, text = 'Edges', width = 385, height = 460, relief = 'raised', borderwidth = 5 );
    hinderFrame = LabelFrame( edgesTab, text = 'Hinderances', width = 385, height = 460, relief = 'raised', borderwidth = 5 );
    
    edgeFrame.grid( row = 0, column = 0, padx = 10, pady = 30 );
    hinderFrame.grid( row = 1, column = 0, padx = 10, pady = 30 );
    
    # Create Edge Matrix
    [edgeDict, uniqueEdges] = create_EandD_dict();
    edgeSelections = [];
    edgePointSelections = [];
    edgeEffectText = [];
    pointVal = range( 6 );
    edgeList = [];
    for iEdge in range( maxEandD ):
        edgeSelections.append( StringVar() );
        edgePointSelections.append( StringVar() );
        edgeEffectText.append( StringVar() );
        edgeList.append( [edgeSelections[iEdge], OptionMenu( edgeFrame, edgeSelections[iEdge], *uniqueEdges ), \
                             edgePointSelections[iEdge], OptionMenu( edgeFrame, edgePointSelections[iEdge], *pointVal ), \
                             edgeEffectText[iEdge],\
                             Label( edgeFrame, textvariable = edgeEffectText[iEdge], width = entryWidth, font = "helvetica 10", wraplength = wrapLength )] );
        edgeList[iEdge][1].grid( row = iEdge, column = 0, padx = 10, pady = 10 );
        edgeList[iEdge][3].grid( row = iEdge, column = 1, padx = 10, pady = 10 );
        edgeList[iEdge][5].grid( row = iEdge, column = 2, padx = 10, pady = 10 );    
    
    
    [hindDict, uniqueHind] = create_EandD_dict( tableLoc = './data/EandD/hinderances.csv', prop = 'Hinderance' );
    hindSelections = [];
    hindPointSelections = [];
    hindEffectText = [];
    pointVal = range( 6 );
    hindList = [];
    for iHind in range( maxEandD ):
        hindSelections.append( StringVar() );
        hindPointSelections.append( StringVar() );
        hindEffectText.append( StringVar() );
        hindList.append( [hindSelections[iHind], OptionMenu( hinderFrame, hindSelections[iHind], *uniqueHind ), \
                             hindPointSelections[iHind], OptionMenu( hinderFrame, hindPointSelections[iHind], *pointVal ), \
                             hindEffectText[iHind], \
                             Label( hinderFrame, textvariable = hindEffectText[iHind], width = entryWidth, font = "helvetica 10", wraplength = wrapLength )] );
        hindList[iHind][1].grid( row = iHind, column = 0, padx = 10, pady = 10 );
        hindList[iHind][3].grid( row = iHind, column = 1, padx = 10, pady = 10 );
        hindList[iHind][5].grid( row = iHind, column = 2, padx = 10, pady = 10 );    


    #Add a button to update labels
    updateButton = Button( edgesTab, text = 'Update Labels', height = 2, width = 10,\
                          command = lambda: update_labels( edgeList, edgeDict, hindList, hindDict ) );
    updateButton.grid( row = 2, column = 0, padx = 10, pady = 10 );
    return [edgeList, hindList];
    
def update_labels( edgeList, edgeDict, hindList, hindDict ):
    for iEdge in range( maxEandD ):
        #Check that the edge isn't empty
        requestedEdge = edgeList[iEdge][0].get()
        db_log( 'Requested Edge: {}'.format( requestedEdge ) );
        if( requestedEdge != '' ):
            #Check that the point value exists in the dictionary
            requestedPoint = edgeList[iEdge][2].get();
            if( requestedPoint != '' ):
                requestedPoint = int( requestedPoint );
            else:
                requestedPoint = 0;
                
            pointValExists = requestedPoint in edgeDict[requestedEdge]['values'];
            if( pointValExists ):
                #Get the index of that requested point value
                dictInd = edgeDict[requestedEdge]['values'].index( requestedPoint );
                
                #Set the label to be that index
                edgeList[iEdge][4].set( edgeDict[requestedEdge]['effect'][dictInd] );
            else:
                edgeList[iEdge][4].set( "Point value doesn't exist for that edge. Available point values: {}".format( edgeDict[requestedEdge]['values'] ) );
        else:
            edgeList[iEdge][4].set( "Requested Edge not an option" );
            
    #Hinderances
    for iHind in range( maxEandD ):
        #Check that the edge isn't empty
        requestedHind = hindList[iHind][0].get()
        db_log( 'Requested Hinderance: {}'.format( requestedHind ) );
        if( requestedHind != '' ):
            #Check that the point value exists in the dictionary
            requestedPoint = hindList[iHind][2].get();
            if( requestedPoint != '' ):
                requestedPoint = int( requestedPoint );
            else:
                requestedPoint = 0;
                
            pointValExists = requestedPoint in hindDict[requestedHind]['values'];
            if( pointValExists ):
                #Get the index of that requested point value
                dictInd = hindDict[requestedHind]['values'].index( requestedPoint );
                
                #Set the label to be that index
                hindList[iHind][4].set( hindDict[requestedHind]['effect'][dictInd] );
            else:
                hindList[iHind][4].set( "Point value doesn't exist for that hinderance. Available point values: {}".format( hindDict[requestedHind]['values'] ) );
        else:
            hindList[iHind][4].set( "Requested Hinderance not an option" );
            
    
def create_EandD_dict( tableLoc = './data/EandD/edges.csv', prop = 'Edge' ):
    EandDTable = read_csv( tableLoc );
    db_log( 'Read {} list: {}'.format( prop, EandDTable.head() ) );
    
    # Get unique edges
    EandDList = EandDTable[prop].values.tolist();
    uniqueEandD = unique( EandDList );
    uniqueEandD = uniqueEandD[0]; #just the list, not the list and counts
    db_log( 'Unique {}: {}'.format( prop, uniqueEandD ) );
    
    # For each unique edge, go through the table and find the values and description of each instance
    EandDdict = {};
    for iEdge in range( len( uniqueEandD ) ):
        curEandD = uniqueEandD[iEdge];
        valueList = [];
        descriptionList = [];
        
        for iEntry in range( len( EandDTable ) ):
            if( EandDTable[prop][iEntry] == uniqueEandD[iEdge] ):
                valueList.append( EandDTable['Points'][iEntry] );
                descriptionList.append( EandDTable['Effect'][iEntry] );
        
        EandDdict[curEandD] = { 'values' : deepcopy( valueList ), 'effect' : deepcopy( descriptionList ) };
    
    db_log( 'Created {} dict: {}'.format( prop, EandDdict ) );
    return [EandDdict, uniqueEandD];
    
def unique( listIn ):
    listSet = set( listIn );
    uniqueList = ( list( listSet ) );
    
    #count number of instances
    counts = zeros( len( uniqueList ) );
    for iCount in range( len( uniqueList ) ):
        counts[iCount] = listIn.count( uniqueList[iCount] );
        
    return [uniqueList, counts];