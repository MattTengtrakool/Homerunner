
sqlite3 homerunner.db

CREATE TABLE IF NOT EXISTS users(
	id  INTEGER PRIMARY KEY AUTOINCREMENT,  
	UserName  text  UNIQUE NOT NULL,
	hash text NOT NULL,
	UserType text  NOT NULL,
	FirstName text NOT NULL,
	LastName text NOT NULL,	
	Address  text NULL,
	City text NULL,
	State text NULL,
	Country text NULL,
	ZipCode text NULL,	
	Phone text  NULL,	
	Email text NOT NULL,	
	Note text Null
	);


CREATE TABLE   contact_message(
	id  INTEGER PRIMARY KEY AUTOINCREMENT,  
	Name  text   NOT NULL,		
	Email text NOT NULL,	
	Phone text  NULL,	
	Title text  NULL
	);

CREATE TABLE 'requests' ('requestid' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 'location' TEXT NOT NULL, 'username' TEXT NOT NULL, 'request' TEXT NOT NULL);
