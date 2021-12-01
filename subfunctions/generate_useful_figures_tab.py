#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 23:19:08 2021

@author: mickey
"""
from tkinter import *
from PIL import ImageTk, Image
from os import listdir
from MDCG_log import db_log

def generate_useful_figures( figuresTab, figureLoc = './data/figures' ):
    figures = listdir( figureLoc );
    images = [];
    imageLabels = [];
    curRow = 0;
    curCol = -1;
    for figure in figures:
        imagePath = '{}/{}'.format( figureLoc, figure );
        db_log( 'Opening {}...'.format( imagePath ) );
        images.append( ImageTk.PhotoImage( Image.open( imagePath ) ) );
        imageLabels.append( Label( figuresTab, image = images[-1] ) );
        
        curCol += 1;
        if( curCol == 5 ):
            curCol = 0;
            curRow += 1;
            
        imageLabels[-1].grid( row = curRow, column = curCol, padx = 5, pady = 10 );
        
    return [images, imageLabels];
        
    
    