#Generate RNGesus Tab
maxNumDice = 16; #maximum number of dice you can roll in RNGesus frame
maxNumCards = 20;

from tkinter import *
from tkinter import ttk
from MDCG_log import db_log


def generate_RNG_tab( RNGTab ):
	db_log( 'Praying to RNGesus' );

	wellLabel = Label( RNGTab, text = 'Thus Spake RNGesus' );
	wellLabel.grid( row = 0, column = 0, padx = 10, pady = 10 );
	rollWellStr = StringVar();
	rollWell = Label( RNGTab, textvariable = rollWellStr, relief = RAISED, width = 50 );
	rollWell.grid(row = 0, column = 1, columnspan = 2, padx = 10, pady = 10);

	sumLabel = Label( RNGTab, text = 'Prodigal Sum Returns' );
	sumLabel.grid( row = 0, column = 3, padx = 10, pady = 10 );
	sumStr = StringVar();
	sumWell = Label( RNGTab, textvariable = sumStr, relief = RAISED, width = 15 );
	sumWell.grid( row = 0, column = 4, padx = 10, pady = 10 );

	Label( RNGTab, text = 'Max of Dice Rolls: ' ).grid( row = 0, column = 5, padx = 10, pady = 10 );
	maxStr = StringVar();
	maxWell = Label( RNGTab, textvariable = maxStr, relief = RAISED, width = 15 ).grid( row = 0, column = 6, padx = 10, pady = 10 );

	#Label( RNGTab, text = 'Enable Exploding Dice' ).grid( row = 1, column = 2, padx = 10, pady = 10 );
	enableExplDice = IntVar();
	Checkbutton( RNGTab, text = "Enable Exploding Dice", variable = enableExplDice ).grid( row = 1, column = 2, padx = 10, pady = 10 );
	
	explDiceRoll = StringVar();
	explDiceOptions = ['max', 'max - 1', 'max - 2', 'max - 3'];
	explDiceRoll.set( explDiceOptions[0] );
	explDiceOption = OptionMenu( RNGTab, explDiceRoll, *explDiceOptions );
	Label( RNGTab, text = 'Explode On:' ).grid( row = 1, column = 3, padx = 5, pady = 10 );
	explDiceOption.grid( row = 1, column = 4, padx = 5, pady = 10 );

	# Create Dice buttons
	from Temple_of_RNGesus import roll_dice, display_dice
	optionList = range(1, maxNumDice); #only 16 fit comfortably in the frame
	clicked = StringVar();
	clicked.set(optionList[0]);
	drop = OptionMenu( RNGTab, clicked, *optionList )
	Label( RNGTab, text = "Number of Dice to Roll: " ).grid( row = 1, column = 0, padx = 10, pady = 10 );
	drop.grid(row = 1, column = 1, padx = 10, pady = 10);
	db_log( 'Dice dropdown created' );

	# ~ numDice = OptionMenu( RNGTab, clicked, *optionList )
	d4Button = Button( RNGTab, text = 'd4', command = lambda: display_dice( roll_dice( 4, int(clicked.get()), int(enableExplDice.get()), str(explDiceRoll.get()) ), rollWellStr, sumStr, maxStr ) );
	d6Button = Button( RNGTab, text = 'd6', command = lambda: display_dice( roll_dice( 6, int(clicked.get()), int(enableExplDice.get()), str(explDiceRoll.get()) ), rollWellStr, sumStr, maxStr ) );
	d8Button = Button( RNGTab, text = 'd8', command = lambda: display_dice( roll_dice( 8, int(clicked.get()), int(enableExplDice.get()), str(explDiceRoll.get()) ), rollWellStr, sumStr, maxStr ) );
	d10Button = Button( RNGTab, text = 'd10', command = lambda: display_dice( roll_dice( 10, int(clicked.get()), int(enableExplDice.get()), str(explDiceRoll.get()) ), rollWellStr, sumStr, maxStr ) );
	d12Button = Button( RNGTab, text = 'd12', command = lambda: display_dice( roll_dice( 12, int(clicked.get()), int(enableExplDice.get()), str(explDiceRoll.get()) ), rollWellStr, sumStr, maxStr ) );
	d20Button = Button( RNGTab, text = 'd20', command = lambda: display_dice( roll_dice( 20, int(clicked.get()), int(enableExplDice.get()), str(explDiceRoll.get()) ), rollWellStr, sumStr, maxStr ) );
	d100Button = Button( RNGTab, text = 'd100', command = lambda: display_dice( roll_dice( 100, int(clicked.get()), int(enableExplDice.get()), str(explDiceRoll.get()) ), rollWellStr, sumStr, maxStr ) );

	d4Button.grid( row = 2, column = 0, padx = 5, pady = 5 );
	d6Button.grid( row = 2, column = 1, padx = 5, pady = 5 );
	d8Button.grid( row = 2, column = 2, padx = 5, pady = 5 );
	d10Button.grid( row = 2, column = 3, padx = 5, pady = 5 );
	d12Button.grid( row = 2, column = 4, padx = 5, pady = 5 );
	d20Button.grid( row = 2, column = 5, padx = 5, pady = 5 );
	d100Button.grid( row = 2, column = 6, padx = 5, pady = 5 );
	db_log( 'Dice Created' );

	#Spacer
	Label( RNGTab, text = 'Worship', width = 100 ).grid( row = 5, column = 0, columnspan = 7, pady = 50 );

	# Create Cards
	from Temple_of_RNGesus import display_cards, draw_cards
	cardWellLabel = Label( RNGTab, text = 'Card Counter:' ).grid( row = 6, column = 0, padx = 10, pady = 10 );
	cardWellStr = StringVar();
	cardWell = Label( RNGTab, textvariable = cardWellStr, relief = RAISED, width = 75 );
	cardWell.grid( row = 6, column = 1, columnspan = 5, padx = 10, pady = 10 );

	# Number of cards to draw
	numCardRange = range(1, maxNumCards); #only 16 fit comfortably in the frame
	chosenNumCards = StringVar();
	chosenNumCards.set(numCardRange[0]);
	cardDrop = OptionMenu( RNGTab, chosenNumCards, *numCardRange )
	Label( RNGTab, text = "Number Cards to Draw: " ).grid( row = 7, column = 0, padx = 10, pady = 10 );
	cardDrop.grid(row = 7, column = 1, padx = 10, pady = 10);
	db_log( 'Card Dropdown Menu' );

	# Draw cards
	drawCardButton = Button( RNGTab, text = 'Draw Cards', command = lambda: display_cards( draw_cards( int(chosenNumCards.get()) ), cardWellStr ) );
	drawCardButton.grid( row = 7, column = 3, columnspan = 5, padx = 10, pady = 10 );
	
	db_log( 'Prayers heard but unanswered' );

	return True;
