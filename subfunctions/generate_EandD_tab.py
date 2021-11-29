from tkinter import *
from config import maxEandD
from MDCG_log import db_log

from pandas import read_csv 
from numpy import zeros
from copy import deepcopy #so we can reuse lists

def generate_EandD_tab( edgesTab ):
    # Get Edge Table
    edgeDict = create_EandD_dict();
    
    
    hinderDict = create_EandD_dict( tableLoc = './data/hinderances.csv', prop = 'Hinderance' );
    return;
    
def create_EandD_dict( tableLoc = './data/edges.csv', prop = 'Edge' ):
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
    return EandDdict;
    
def unique( listIn ):
    listSet = set( listIn );
    uniqueList = ( list( listSet ) );
    
    #count number of instances
    counts = zeros( len( uniqueList ) );
    for iCount in range( len( uniqueList ) ):
        counts[iCount] = listIn.count( uniqueList[iCount] );
        
    return [uniqueList, counts];