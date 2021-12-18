import inspect
from datetime import datetime
from math import floor

global DEBUG_LEVEL
from config import DEBUG_LEVEL

def investigate( obj ):
    objMeths = [ method_name for method_name in dir( obj ) if callable( getattr( obj, method_name ) ) ];
    objVals  = [ val_name for val_name in dir( obj ) if not callable( getattr( obj, val_name ) ) ];
    
    print( 'Object: \t{}'.format( obj ) );
    print( 'Str Rep: \t{}'.format( str( obj ) ) );
    print( 'Type: \t\t{}'.format( type( obj ) ) );
    print();
    print( 'Methods:');
    print_vals( objMeths, 4 );
    print();
    print( 'Values:');
    print_vals( objVals, 4 );

def print_vals( listObj, numCols = 3 ):
    numRows = floor( len( listObj ) / numCols );
    longestWord = get_longest_entry( listObj );
    
    sepList = [];
    for iRow in range( numRows ):
        sepList.append( listObj[iRow * numCols : iRow*numCols + numCols] );
    if( (len( listObj ) / numCols) % numCols != 0 ):
        sepList.append( listObj[numRows*numCols :] ); # append the rest
    
    for valList in sepList:
        for item in valList:
            print( '{}'.format( item ), end = '' );
            for spaceBuff in range( longestWord - len( item ) ):
                print(' ', end = '' );
        print();
def get_longest_entry( listObj ):
    longestEntry = 0;
    for item in listObj:
        if( len(item) > longestEntry ):
            longestEntry = len( item );
    return longestEntry;
def MDCG_log( strIn, logFile = ''):
	#Print calling function information
	lastFunc 		= inspect.stack()[2]; #assumes this is always being called from db_log
	lastFuncLine 	= lastFunc[2];
	lastFuncName 	= lastFunc[3];
	logStr 			= '[{}] ({}: {}) --> {}\n'.format( datetime.now(), \
														lastFuncName, lastFuncLine, strIn);
	
	# Log in logfile for calling file
	firstFunc 			= inspect.stack()[-1]; #get last index
	callingFilename 	= firstFunc[2];
	callingFilename = callingFilename.rsplit( '.', 1 )[0]; #remove file extension
	
	# Write log
	if( logFile == '' ):
		logFile = callingFilename;
	f = open( '{}.log'.format( logFile ), 'a' );
	f.write( logStr );
	f.flush();
	f.close();

def MDCG_tee( strIn, color = '', logFile = ''):
	#Print calling function information
	# ~ print( inspect.stack()[2] ); 
	# ~ raise ValueError;
	lastFunc 		= inspect.stack()[2]; #assumes this is always being called from db_log
	lastFuncLine 	= lastFunc[2];
	lastFuncName 	= lastFunc[3];
	logStr 			= '[{}] ({}: {}) --> {}\n'.format( datetime.now(), \
														lastFuncName, lastFuncLine, strIn);
														
	colors = {
		'red' 		: '\033[91m',
		'green' 		: '\033[92m',
		'end' 		: '\033[0m',
		'err' 		: '\033[91m',
		'' 			: '\033[0m'
	};
	
	colorStr = '{}{}{} '.format( colors[color], logStr, colors['end'] );
	print( colorStr );
	
	# Log in logfile for calling file
	firstFunc 			= inspect.stack()[-1]; #get last index
	callingFilename 	= firstFunc[1];
	callingFilename = callingFilename.rsplit( '.', 1 )[0]; #remove file extension
	
	# Write log
	if( logFile == '' ):
		logFile = callingFilename;
	f = open( '{}.log'.format( logFile ), 'a' );
	f.write( logStr );
	f.flush();
	f.close();

def db_log( msg, dbFilename = '', color = '' ):
	if( DEBUG_LEVEL == 0 ): #error logging only
		if( color == 'err' ):
			MDCG_tee( msg, color, dbFilename );
	if( DEBUG_LEVEL == 1 ): #logging everything
		MDCG_log( msg, dbFilename );
	if( DEBUG_LEVEL == 2 ): #Tee everything
		MDCG_tee( msg, color, dbFilename );
