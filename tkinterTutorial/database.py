from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk();
root.title('Database');
root.geometry('400x400');

#Databases

#Create a database and cursor
conn = sqlite3.connect('address_book.db');
c = conn.cursor(); #Create cursor

#Create table
# ~ c.execute( """CREATE TABLE addresses(
	# ~ firstName text,
	# ~ lastName text,
	# ~ address text,
	# ~ city text,
	# ~ state text,
	# ~ zipCode integer)""" );
	
#Create submit function for database
def submit():
	# Clear the text boxes;
	firstName.delete(0, END);
	lastName.delete(0, END);
	address.delete(0, END);
	city.delete(0, END);
	state.delete(0, END);
	zipCode.delete(0, END);
	
	# Connect to database
	conn = sqlite3.connect( 'address_book.db' );
	c = conn.cursor();
	
	c.execute("INSERT INTO addresses VALUES (:firstName, :lastName, :address, :city, :state, :zipCode)", 
		{
			'firstName' : firstName.get(),
			'lastName' : lastName.get(),
			'address' : address.get(),
			'city' : city.get(),
			'state' : state.get(),
			'zipCode' : zipCode.get()
		}
	);
	
	conn.commit();
	conn.close();
	
def query():
	# Connect to database
	conn = sqlite3.connect( 'address_book.db' );
	c = conn.cursor();
	
	# Query the database
	c.execute("SELECT *, oid FROM addresses");
	records = c.fetchall();
	# ~ print( records );
	
	print_records = '';
	for record in records[0]:
		print_records += str(record) + '\n';
		
	queryLabel = Label( root, text = print_records );
	queryLabel.grid(row = 8, column = 0, columnspan = 2);
	
	conn.commit();
	conn.close();

	return;
# Create Text Boxes
firstName = Entry( root, width = 30 );
firstName.grid( row = 0, column = 1, padx = 20 );

lastName = Entry( root, width = 30 );
lastName.grid( row = 1, column = 1, padx = 20 );

address = Entry( root, width = 30 );
address.grid( row = 2, column = 1, padx = 20 );

city = Entry( root, width = 30 );
city.grid( row = 3, column = 1, padx = 20 );

state = Entry( root, width = 30 );
state.grid( row = 4, column = 1, padx = 20 );

zipCode = Entry( root, width = 30 );
zipCode.grid( row = 5, column = 1, padx = 20 );

# Create Text Box Labels
fnLabel = Label(root, text = "First Name" );
fnLabel.grid( row = 0, column = 0 );

lnLabel = Label(root, text = "Last Name" );
lnLabel.grid( row = 1, column = 0 );

adLabel = Label(root, text = "Address" );
adLabel.grid( row = 2, column = 0 );

cityLabel = Label(root, text = "City" );
cityLabel.grid( row = 3, column = 0 );

stateLabel = Label(root, text = "State" );
stateLabel.grid( row = 4, column = 0 );

zipLabel = Label(root, text = "Zip Code" );
zipLabel.grid( row = 5, column = 0 );

# Create submit button
submitButton = Button( root, text = "Add record to Database", command = submit );
submitButton.grid( row = 6, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 100 );

# Create query button
queryButton = Button( root, text = "Show Records", command = query );
queryButton.grid( row = 7, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 137 );

#Commit changes
conn.commit();

#Close connection
conn.close();

root.mainloop()
