import sqlite3
conn = sqlite3.connect('Cel_Bodies.db')
print("Opened database successfully");

# cursor objects are used to traverse, search, grab, etc. information from the database, similar to indices or pointers  
cursor = conn.cursor()

#Creates the table that will be used for attributes. Commented out now for testing.

# SQL command to create a table in the database 
sql_command = """CREATE TABLE IF NOT EXISTS ATTRIBUTES (
	ID INTEGER PRIMARY KEY NOT NULL,
	NAME TEXT NOT NULL,
	MASS real NOT NULL,
	RADIUS real NOT NULL,
	VOLUME real NOT NULL,
	ORBITAL VELOCITY real NOT NULL,
	ROTATIONAL VELOCITY real NOT NULL, 
	DISTANCE SUN real NOT NULL)
;"""

# execute the statement 
cursor.execute(sql_command) 
print("Table created successfully");


# SQL command to insert the data in the table, must be done one at a time 

		#SUN
sql_command = """INSERT INTO ATTRIBUTES VALUES(1, 'SUN', 1988500000000000000000000000000, 696342000, 1410000000000000000, 0, 1997000, 0);"""
cursor.execute(sql_command) 
print("SUN created successfully");

		#MERCURY
sql_command = """INSERT INTO ATTRIBUTES VALUES(2, 'MERCURY', 330110000000000000000000, 2439700, 60830000000, 47360, 3.026, 58000000000);"""
cursor.execute(sql_command) 
print("Mercury created successfully");

		#VENUS
sql_command = """INSERT INTO ATTRIBUTES VALUES(3, 'VENUS', 4867500000000000000000000, 60518000, 928430000000, 35020, 1.81, 108000000000);"""
cursor.execute(sql_command) 
print("Venus created successfully");

		#Earth
sql_command = """INSERT INTO ATTRIBUTES VALUES(4, 'EARTH', 5972370000000000000000000, 6371, 1083210000000, 29780, 465.1, 150000000000);"""
cursor.execute(sql_command) 
print("Earth created successfully");

		#MARS
sql_command = """INSERT INTO ATTRIBUTES VALUES(5, 'MARS', 641710000000000000000000, 3396200, 163118000000, 24070, 241, 228000000000);"""
cursor.execute(sql_command) 
print("Mars created successfully");

		#JUPITER
sql_command = """INSERT INTO ATTRIBUTES VALUES(6, 'Jupiter', 1898200000000000000000000000, 71492000, 1431300000000000, 13070, 12600, 484000000000);"""
cursor.execute(sql_command) 
print("Jupiter created successfully");

		#SATURN
sql_command = """INSERT INTO ATTRIBUTES VALUES(7, 'Saturn', 568340000000000000000000000, 60268000, 827130000000000, 9680, 12600, 1400000000000);"""
cursor.execute(sql_command) 
print("Saturn created successfully");

		#URANUS
sql_command = """INSERT INTO ATTRIBUTES VALUES(8, 'URANUS', 86810000000000000000000000, 25559000, 68330000000000, 6800, 2590, 2800000000000);"""
cursor.execute(sql_command) 
print("Uranus created successfully");

		#NEPTUNE
sql_command = """INSERT INTO ATTRIBUTES VALUES(9, 'NEPTUNE', 102413000000000000000000000, 24341000, 62530000000000, 5430, 2800, 4500000000000);"""
cursor.execute(sql_command) 
print("Neptune created successfully");


# QUERY FOR ALL
print("Entire ATTRIBUTES table")
cursor.execute("""SELECT * FROM ATTRIBUTES""")
query_result = cursor.fetchall()
for i in query_result:
	print(i)

conn.commit() 

conn.close()
