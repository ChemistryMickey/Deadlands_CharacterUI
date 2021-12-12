from tkinter import *
"""
Goal:
    See if there's a systematic way to find a particular button in a dynamic array of buttons
    
Observations:
    All buttons had the output "This is button 9" no matter which button was pressed using the lambda
    Command isn't frozen. If iBut changes, then the command for all the buttons changes. So the variable c must be declared to refer to the individual button. 
        That's the key to identifying rows in the deadlands gui 
"""

root = Tk();

butList = [];
for iBut in range(10):
#    butList.append( Button( root, width = 10, text = 'Button {}'.format( iBut ), command = lambda: print('This is Button {}'.format( iBut ) ) ) ); #observation 1
    butList.append( Button( root, width = 10, text = 'Button {}'.format( iBut ), command = lambda c = iBut: print( butList[c].cget('text') ) ) );
    butList[iBut].pack();


root.mainloop();