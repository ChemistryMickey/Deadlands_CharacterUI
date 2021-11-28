import inspect
from datetime import datetime

global DEBUG_LEVEL
from config import DEBUG_LEVEL

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
