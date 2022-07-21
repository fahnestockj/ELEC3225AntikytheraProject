# Implementation for all the databases --> will put together the Solar, Events, Lunar, and Bodies db into one file


import sqlite3
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from astropy.time import Time
from astroquery.jplhorizons import Horizons
import conj
from conj import *
import solar_eclipse_dates
from solar_eclipse_dates import *
import lunar_eclipse_dates
from lunar_eclipse_dates import *


conn = sqlite3.connect('Database.db')
print("Opened database successfully");

# cursor objects are used to traverse, search, grab, etc. information from the database, similar to indices or pointers  
cursor = conn.cursor()

#Creates the table that will be used for attributes. Commented out now for testing.

# SQL command to create a table in the database 

#----------------BODIES STUFF-------------------#
		#---create Bodies table----
sql_command = """CREATE TABLE IF NOT EXISTS BODIES (
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
#print("BODIES table created successfully");

# SQL command to insert the data in the table, must be done one at a time 

		#SUN
sql_command = """INSERT OR IGNORE INTO BODIES VALUES(1, 'SUN', 1988500000000000000000000000000, 696342000, 1410000000000000000, 0, 1997000, 0);"""
cursor.execute(sql_command) 
#print("SUN created successfully");

		#MERCURY
sql_command = """INSERT OR IGNORE INTO BODIES VALUES(2, 'MERCURY', 330110000000000000000000, 2439700, 60830000000, 47360, 3.026, 58000000000);"""
cursor.execute(sql_command) 
#print("Mercury created successfully");

		#VENUS
sql_command = """INSERT OR IGNORE INTO BODIES VALUES(3, 'VENUS', 4867500000000000000000000, 60518000, 928430000000, 35020, 1.81, 108000000000);"""
cursor.execute(sql_command) 
#print("Venus created successfully");

		#Earth
sql_command = """INSERT OR IGNORE INTO BODIES VALUES(4, 'EARTH', 5972370000000000000000000, 6371, 1083210000000, 29780, 465.1, 150000000000);"""
cursor.execute(sql_command) 
#print("Earth created successfully");

		#MARS
sql_command = """INSERT OR IGNORE INTO BODIES VALUES(5, 'MARS', 641710000000000000000000, 3396200, 163118000000, 24070, 241, 228000000000);"""
cursor.execute(sql_command) 
#print("Mars created successfully");

		#JUPITER
sql_command = """INSERT OR IGNORE INTO BODIES VALUES(6, 'Jupiter', 1898200000000000000000000000, 71492000, 1431300000000000, 13070, 12600, 484000000000);"""
cursor.execute(sql_command) 
#print("Jupiter created successfully");

		#SATURN
sql_command = """INSERT OR IGNORE INTO BODIES VALUES(7, 'Saturn', 568340000000000000000000000, 60268000, 827130000000000, 9680, 12600, 1400000000000);"""
cursor.execute(sql_command) 
#print("Saturn created successfully");

		#URANUS
sql_command = """INSERT OR IGNORE INTO BODIES VALUES(8, 'URANUS', 86810000000000000000000000, 25559000, 68330000000000, 6800, 2590, 2800000000000);"""
cursor.execute(sql_command) 
#print("Uranus created successfully");

		#NEPTUNE
sql_command = """INSERT OR IGNORE INTO BODIES VALUES(9, 'NEPTUNE', 102413000000000000000000000, 24341000, 62530000000000, 5430, 2800, 4500000000000);"""
cursor.execute(sql_command) 
#print("Neptune created successfully");

		#PLUTO
sql_command = """INSERT OR IGNORE INTO BODIES VALUES(10, 'PLUTO', 13090000000000000000000000, 1151000, 6387259783000, 4670, 13.1, 4500000000000);"""
cursor.execute(sql_command) 
#print("PLUTO created successfully");

#----------------MOON STUFF-------------------#

		#---create MOON table----
sql_command = """CREATE TABLE IF NOT EXISTS MOON (
	MOON NAME TEXT PRIMARY KEY NOT NULL,
	PLANET NAME TEXT NOT NULL,
	MASS real NOT NULL,
	RADIUS real NOT NULL,
	VOLUME real NOT NULL,
	ORBITAL VELOCITY real NOT NULL,
	ROTATIONAL VELOCITY real NOT NULL,
	AVG DISTANCE real NULL)
;"""

# execute the statement 
cursor.execute(sql_command) 
#print("MOON table created successfully");

		# Earth's MOON
sql_command = """INSERT OR IGNORE INTO MOON VALUES('MOON', 'SUN', 734800000000000000000000000000, 17374000, 2190000000000000000, 1022, 0, 384399);"""
cursor.execute(sql_command) 
#print("Earth's moon created successfully");

		# Earth's MOON
sql_command = """INSERT OR IGNORE INTO MOON VALUES('MOON', 'SUN', 734800000000000000000000000000, 17374000, 2190000000000000000, 1022, 0, 384399);"""
cursor.execute(sql_command) 
#print("Earth's moon (MOON) created successfully");

		# Mar's MOON PHOBOS
sql_command = """INSERT OR IGNORE INTO MOON VALUES('PHOBOS', 'MARS', 1065900000000000000000000000000, 112667000, 5783610000000000000000, 2138, 00031, 6000);"""
cursor.execute(sql_command) 
#print("Mar's moon (PHOBOS) created successfully");

		# Mar's MOON DEIMOS
sql_command = """INSERT OR IGNORE INTO MOON VALUES('DEIMOS', 'MARS', 1476200000000000000000000000000, 6200, 999780000000000000000, 13513, 0, 23458);"""
cursor.execute(sql_command) 
#print("Mar's moon (DEIMOS) created successfully");

		# JUPITER's MOON IO
sql_command = """INSERT OR IGNORE INTO MOON VALUES('IO', 'JUPITER', 8931900000000000000000000000000, 18216, 253190649070000000000000000, 1734, 75.3, 421800);"""
cursor.execute(sql_command) 
#print("JUPITER's moon (IO) created successfully");

		# JUPITER's MOON EUROPA
sql_command = """INSERT OR IGNORE INTO MOON VALUES('EUROPA', 'JUPITER', 47998438387492700000000000, 1560800, 159268679180000000000000000, 13740, 0, 671100);"""
cursor.execute(sql_command) 
#print("JUPITER's moon (EUROPA) created successfully");

		# JUPITER's MOON GANYMEDE
sql_command = """INSERT OR IGNORE INTO MOON VALUES('GANYMEDE', 'JUPITER', 14818584687505200000000000, 2631200, 763045069980000000000000000, 10880, 0, 1070400000);"""
cursor.execute(sql_command) 
#print("JUPITER's moon (GANYMEDE) created successfully");

		# JUPITER's MOON CALLISTO
sql_command = """INSERT OR IGNORE INTO MOON VALUES('CALLISTO', 'JUPITER', 10759373796381900000000000, 2410300, 58654577603000, 8203, 0, 1882700000);"""
cursor.execute(sql_command) 
#print("JUPITER's moon (CALLISTO) created successfully");

		# SATURN's MOON TITAN
sql_command = """INSERT OR IGNORE INTO MOON VALUES('TITAN', 'SATURN', 134552523083241000000000000, 2574700, 71496320086000, 5570, 0, 1221865000);"""
cursor.execute(sql_command) 
#print("SATURN's moon (TITAN) created successfully");

		# SATURN's MOON RHEA
sql_command = """INSERT OR IGNORE INTO MOON VALUES('RHEA', 'SATURN', 2307089151289080000000000000, 764300, 1870166133000, 8484, 0, 527068000);"""
cursor.execute(sql_command) 
#print("SATURN's moon (RHEA) created successfully");

		# URANUS's MOON MIRANDA
sql_command = """INSERT OR IGNORE INTO MOON VALUES('MIRANDA', 'URANUS', 65941411056276500000000, 235800, 5491867000, 6685, 0, 129900000);"""
cursor.execute(sql_command) 
#print("URANUS's moon (MIRANDA) created successfully");

		# URANUS's MOON ARIEL
sql_command = """INSERT OR IGNORE INTO MOON VALUES('ARIEL', 'URANUS', 1294849526195970000000000, 578900, 812641988000, 5509, 0, 190900000);"""
cursor.execute(sql_command) 
#print("URANUS's moon (ARIEL) created successfully");

		# URANUS's MOON UMBRIEL
sql_command = """INSERT OR IGNORE INTO MOON VALUES('UMBRIEL', 'URANUS', 12214147729742100000000000, 584700, 837313109000, 4668, 0, 266000000);"""
cursor.execute(sql_command) 
#print("URANUS's moon (UMBRIEL) created successfully");

		# URANUS's MOON TITANIA
sql_command = """INSERT OR IGNORE INTO MOON VALUES('TITANIA', 'URANUS', 3419961364327790000000000, 788900, 2056622001000, 3640, 0, 436300000);"""
cursor.execute(sql_command) 
#print("URANUS's moon (TITANIA) created successfully");

		# URANUS's MOON OBERON
sql_command = """INSERT OR IGNORE INTO MOON VALUES('OBERON', 'URANUS', 2883438065279000000000000, 761400, 1848958769000, 3640, 0, 583500000);"""
cursor.execute(sql_command) 
#print("URANUS's moon (OBERON) created successfully");

		# NEPTUNE's MOON TRITON
sql_command = """INSERT OR IGNORE INTO MOON VALUES('TRITON', 'NEPTUNE', 21394990550895500000000000, 1353400, 10384058491000, 4390, 0, 354759000);"""
cursor.execute(sql_command) 
#print("NEPTUNE's moon (TRITON) created successfully");

		# PLUTO's MOON TRITON
sql_command = """INSERT OR IGNORE INTO MOON VALUES('CHARON', 'PLUTO', 1546625822956300000000000, 603600, 921162612000, 199.7, 0, 17536000);"""
cursor.execute(sql_command) 
#print("PLUTO's moon (CHARON) created successfully");


# date = "date"
# for line in solar_eclipse_dates:
#         if date in 
#         new_date = 

#----------------PLANET EVENTS STUFF-------------------#

#conn.execute("""DROP TABLE CONJUNCTION""")

sql_command = """CREATE TABLE IF NOT EXISTS CONJUNCTION (
DATE STRING PRIMARY KEY NOT NULL,  
FIRST_PLANET INT NOT NULL,
SECOND_PLANET INT NOT NULL,
MERCURY_X FLOAT NOT NULL,
MERCURY_Y FLOAT NOT NULL,
MERCURY_VX FLOAT NOT NULL,
MERCURY_VY FLOAT NOT NULL,
VENUS_X FLOAT NOT NULL,
VENUS_Y FLOAT NOT NULL,
VENUS_VX FLOAT NOT NULL,
VENUS_VY FLOAT NOT NULL,
EARTH_X FLOAT NOT NULL,
EARTH_Y FLOAT NOT NULL,
EARTH_VX FLOAT NOT NULL,
EARTH_VY FLOAT NOT NULL,
MARS_X FLOAT NOT NULL,
MARS_Y FLOAT NOT NULL,
MARS_VX FLOAT NOT NULL,
MARS_VY FLOAT NOT NULL,
JUPITER_X FLOAT NOT NULL,
JUPITER_Y FLOAT NOT NULL,
JUPITER_VX FLOAT NOT NULL,
JUPITER_VY FLOAT NOT NULL,
SATURN_X FLOAT NOT NULL,
SATURN_Y FLOAT NOT NULL,
SATURN_VX FLOAT NOT NULL,
SATURN_VY FLOAT NOT NULL,
URANUS_X FLOAT NOT NULL,
URANUS_Y FLOAT NOT NULL,
URANUS_VX FLOAT NOT NULL,
URANUS_VY FLOAT NOT NULL,
NEPTUNE_X FLOAT NOT NULL,
NEPUTNE_Y FLOAT NOT NULL,
NEPTUNE_VX FLOAT NOT NULL,
NEPTUNE_VY FLOAT NOT NULL,
PLUTO_X FLOAT NOT NULL,
PLUTO_Y FLOAT NOT NULL,
PLUTO_VX FLOAT NOT NULL,
PLUTO_VY FLOAT NOT NULL)
;"""
cursor.execute(sql_command)

#Planet ID
mercury_id = 1
venus_id = 2
earth_id = 3
mars_id = 4
jupiter_id = 5
saturn_id = 6
uranus_id = 7
neptune_id = 8
pluto_id = 9
sun_id = 10

mercury_x = float(Horizons(id=mercury_id, location="@sun", epochs=Time(conj.date5).jd).vectors()["x"])
mercury_y = float(Horizons(id=mercury_id, location="@sun", epochs=Time(conj.date5).jd).vectors()["y"])
mercury_vx = float(Horizons(id=mercury_id, location="@sun", epochs=Time(conj.date5).jd).vectors()["vx"])
mercury_vy = float(Horizons(id=mercury_id, location="@sun", epochs=Time(conj.date5).jd).vectors()["vy"])

venus_x = float(Horizons(id=venus_id, location="@sun", epochs=Time(conj.date5).jd).vectors()["x"])
venus_y = float(Horizons(id=venus_id, location="@sun", epochs=Time(conj.date5).jd).vectors()["y"])
venus_vx = float(Horizons(id=venus_id, location="@sun", epochs=Time(conj.date5).jd).vectors()["vx"])
venus_vy = float(Horizons(id=venus_id, location="@sun", epochs=Time(conj.date5).jd).vectors()["vy"])

earth_x = float(Horizons(id=earth_id, location="@sun", epochs=Time(conj.date5).jd).vectors()["x"])
earth_y = float(Horizons(id=earth_id, location="@sun", epochs=Time(conj.date5).jd).vectors()["y"])
earth_vx = float(Horizons(id=earth_id, location="@sun", epochs=Time(conj.date5).jd).vectors()["vx"])
earth_vy = float(Horizons(id=earth_id, location="@sun", epochs=Time(conj.date5).jd).vectors()["vy"])

mars_x = float(Horizons(id=mars_id, location="@sun", epochs=Time(conj.date5).jd).vectors()["x"])
mars_y = float(Horizons(id=mars_id, location="@sun", epochs=Time(conj.date5).jd).vectors()["y"])
mars_vx = float(Horizons(id=mars_id, location="@sun", epochs=Time(conj.date5).jd).vectors()["vx"])
mars_vy = float(Horizons(id=mars_id, location="@sun", epochs=Time(conj.date5).jd).vectors()["vy"])

jupiter_x = float(Horizons(id=jupiter_id, location="@sun", epochs=Time(conj.date5).jd).vectors()["x"])
jupiter_y = float(Horizons(id=jupiter_id, location="@sun", epochs=Time(conj.date5).jd).vectors()["y"])
jupiter_vx = float(Horizons(id=jupiter_id, location="@sun", epochs=Time(conj.date5).jd).vectors()["vx"])
jupiter_vy = float(Horizons(id=jupiter_id, location="@sun", epochs=Time(conj.date5).jd).vectors()["vy"])

saturn_x = float(Horizons(id=saturn_id, location="@sun", epochs=Time(conj.date5).jd).vectors()["x"])
saturn_y = float(Horizons(id=saturn_id, location="@sun", epochs=Time(conj.date5).jd).vectors()["y"])
saturn_vx = float(Horizons(id=saturn_id, location="@sun", epochs=Time(conj.date5).jd).vectors()["vx"])
saturn_vy = float(Horizons(id=saturn_id, location="@sun", epochs=Time(conj.date5).jd).vectors()["vy"])

uranus_x = float(Horizons(id=uranus_id, location="@sun", epochs=Time(conj.date5).jd).vectors()["x"])
uranus_y = float(Horizons(id=uranus_id, location="@sun", epochs=Time(conj.date5).jd).vectors()["y"])
uranus_vx = float(Horizons(id=uranus_id, location="@sun", epochs=Time(conj.date5).jd).vectors()["vx"])
uranus_vy = float(Horizons(id=uranus_id, location="@sun", epochs=Time(conj.date5).jd).vectors()["vy"])

neptune_x = float(Horizons(id=neptune_id, location="@sun", epochs=Time(conj.date5).jd).vectors()["x"])
neptune_y = float(Horizons(id=neptune_id, location="@sun", epochs=Time(conj.date5).jd).vectors()["y"])
neptune_vx = float(Horizons(id=neptune_id, location="@sun", epochs=Time(conj.date5).jd).vectors()["vx"])
neptune_vy = float(Horizons(id=neptune_id, location="@sun", epochs=Time(conj.date5).jd).vectors()["vy"])

pluto_x = float(Horizons(id=pluto_id, location="@sun", epochs=Time(conj.date5).jd).vectors()["x"])
pluto_y = float(Horizons(id=pluto_id, location="@sun", epochs=Time(conj.date5).jd).vectors()["y"])
pluto_vx = float(Horizons(id=pluto_id, location="@sun", epochs=Time(conj.date5).jd).vectors()["vx"])
pluto_vy = float(Horizons(id=pluto_id, location="@sun", epochs=Time(conj.date5).jd).vectors()["vy"])

cursor.execute("""INSERT OR IGNORE INTO CONJUNCTION VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", (conj.date5, saturn_id, uranus_id, mercury_x, mercury_y, mercury_vx, mercury_vy, venus_x, venus_y, venus_vx, venus_vy, earth_x, earth_y, earth_vx, earth_vy, mars_x, mars_y, mars_vx, mars_vy, jupiter_x, jupiter_y, jupiter_vx, jupiter_vy, saturn_x, saturn_y, saturn_vx, saturn_vy, uranus_x, uranus_y, uranus_vx, uranus_vy, neptune_x, neptune_y, neptune_vx, neptune_vy, pluto_x, pluto_y, pluto_vx, pluto_vy))


#----------------SOLAR ECLIPSE STUFF-------------------#

#conn.execute("""DROP TABLE SOLAR_ECLIPSES""")
sql_command = """CREATE TABLE IF NOT EXISTS SOLAR_ECLIPSES 
        (DATE STRING PRIMARY KEY,
        MERCURY_X FLOAT,
        MERCURY_Y FLOAT,
        MERCURY_VX FLOAT,
        MERCURY_VY FLOAT,
        VENUS_X FLOAT,
        VENUS_Y FLOAT,
        VENUS_VX FLOAT,
        VENUS_VY FLOAT,
        EARTH_X FLOAT,
        EARTH_Y FLOAT,
        EARTH_VX FLOAT,
        EARTH_VY FLOAT,
        MARS_X FLOAT,
        MARS_Y FLOAT,
        MARS_VX FLOAT,
        MARS_VY FLOAT,
        JUPITER_X FLOAT,
        JUPITER_Y FLOAT,
        JUPITER_VX FLOAT,
        JUPITER_VY FLOAT,
        SATURN_X FLOAT,
        SATURN_Y FLOAT,
        SATURN_VX FLOAT,
        SATURN_VY FLOAT,
        URANUS_X FLOAT,
        URANUS_Y FLOAT,
        URANUS_VX FLOAT,
        URANUS_VY FLOAT,
        NEPTUNE_X FLOAT,
        NEPTUNE_Y FLOAT,
        NEPTUNE_VX FLOAT,
        NEPTUNE_VY FLOAT,
        PLUTO_X FLOAT,
        PLUTO_Y FLOAT,
        PLUTO_VX FLOAT,
        PLUTO_VY FLOAT
        );"""
conn.execute(sql_command)

time = Time(solar_eclipse_dates.date1).jd

mercury_x = float(Horizons(id=1, location="@sun", epochs=time).vectors()["x"])
mercury_y = float(Horizons(id=1, location="@sun", epochs=time).vectors()["y"])
mercury_vx = float(Horizons(id=1, location="@sun", epochs=time).vectors()["vx"])
mercury_vy = float(Horizons(id=1, location="@sun", epochs=time).vectors()["vy"])
venus_x = float(Horizons(id=2, location="@sun", epochs=time).vectors()["x"])
venus_y = float(Horizons(id=2, location="@sun", epochs=time).vectors()["y"])
venus_vx = float(Horizons(id=2, location="@sun", epochs=time).vectors()["vx"])
venus_vy = float(Horizons(id=2, location="@sun", epochs=time).vectors()["vy"])
earth_x = float(Horizons(id=3, location="@sun", epochs=time).vectors()["x"])
earth_y = float(Horizons(id=3, location="@sun", epochs=time).vectors()["y"])
earth_vx = float(Horizons(id=3, location="@sun", epochs=time).vectors()["vx"])
earth_vy = float(Horizons(id=3, location="@sun", epochs=time).vectors()["vy"])
mars_x = float(Horizons(id=4, location="@sun", epochs=time).vectors()["x"])
mars_y = float(Horizons(id=4, location="@sun", epochs=time).vectors()["y"])
mars_vx = float(Horizons(id=4, location="@sun", epochs=time).vectors()["vx"])
mars_vy = float(Horizons(id=4, location="@sun", epochs=time).vectors()["vy"])
jupiter_x = float(Horizons(id=5, location="@sun", epochs=time).vectors()["x"])
jupiter_y = float(Horizons(id=5, location="@sun", epochs=time).vectors()["y"])
jupiter_vx = float(Horizons(id=5, location="@sun", epochs=time).vectors()["vx"])
jupiter_vy = float(Horizons(id=5, location="@sun", epochs=time).vectors()["vy"])
saturn_x = float(Horizons(id=6, location="@sun", epochs=time).vectors()["x"])
saturn_y = float(Horizons(id=6, location="@sun", epochs=time).vectors()["y"])
saturn_vx = float(Horizons(id=6, location="@sun", epochs=time).vectors()["vx"])
saturn_vy = float(Horizons(id=6, location="@sun", epochs=time).vectors()["vy"])
uranus_x = float(Horizons(id=7, location="@sun", epochs=time).vectors()["x"])
uranus_y = float(Horizons(id=7, location="@sun", epochs=time).vectors()["y"])
uranus_vx = float(Horizons(id=7, location="@sun", epochs=time).vectors()["vx"])
uranus_vy = float(Horizons(id=7, location="@sun", epochs=time).vectors()["vy"])
neptune_x = float(Horizons(id=8, location="@sun", epochs=time).vectors()["x"])
neptune_y = float(Horizons(id=8, location="@sun", epochs=time).vectors()["y"])
neptune_vx = float(Horizons(id=8, location="@sun", epochs=time).vectors()["vx"])
neptune_vy = float(Horizons(id=8, location="@sun", epochs=time).vectors()["vy"])
pluto_x = float(Horizons(id=9, location="@sun", epochs=time).vectors()["x"])
pluto_y = float(Horizons(id=9, location="@sun", epochs=time).vectors()["y"])
pluto_vx = float(Horizons(id=9, location="@sun", epochs=time).vectors()["vx"])
pluto_vy = float(Horizons(id=9, location="@sun", epochs=time).vectors()["vy"])
conn.execute("""INSERT OR IGNORE INTO SOLAR_ECLIPSES VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", (solar_eclipse_dates.date24, mercury_x, mercury_y, mercury_vx, mercury_vy, venus_x, venus_y, venus_vx, venus_vy, earth_x, earth_y, earth_vx, earth_vy, mars_x, mars_y, mars_vx, mars_vy, jupiter_x, jupiter_y, jupiter_vx, jupiter_vy, saturn_x, saturn_y, saturn_vx, saturn_vy, uranus_x, uranus_y, uranus_vx, uranus_vy, neptune_x, neptune_y, neptune_vx, neptune_vy, pluto_x, pluto_y, pluto_vx, pluto_vy))

#----------------LUNAR ECLIPSES STUFF-------------------#
#conn.execute("""DROP TABLE LUNAR_ECLIPSES""")
sql_command = """CREATE TABLE IF NOT EXISTS LUNAR_ECLIPSES 
        (DATE STRING PRIMARY KEY,
        MERCURY_X FLOAT,
        MERCURY_Y FLOAT,
        MERCURY_VX FLOAT,
        MERCURY_VY FLOAT,
        VENUS_X FLOAT,
        VENUS_Y FLOAT,
        VENUS_VX FLOAT,
        VENUS_VY FLOAT,
        EARTH_X FLOAT,
        EARTH_Y FLOAT,
        EARTH_VX FLOAT,
        EARTH_VY FLOAT,
        MARS_X FLOAT,
        MARS_Y FLOAT,
        MARS_VX FLOAT,
        MARS_VY FLOAT,
        JUPITER_X FLOAT,
        JUPITER_Y FLOAT,
        JUPITER_VX FLOAT,
        JUPITER_VY FLOAT,
        SATURN_X FLOAT,
        SATURN_Y FLOAT,
        SATURN_VX FLOAT,
        SATURN_VY FLOAT,
        URANUS_X FLOAT,
        URANUS_Y FLOAT,
        URANUS_VX FLOAT,
        URANUS_VY FLOAT,
        NEPTUNE_X FLOAT,
        NEPTUNE_Y FLOAT,
        NEPTUNE_VX FLOAT,
        NEPTUNE_VY FLOAT,
        PLUTO_X FLOAT,
        PLUTO_Y FLOAT,
        PLUTO_VX FLOAT,
        PLUTO_VY FLOAT
        );"""
conn.execute(sql_command)

time = Time(lunar_eclipse_dates.date1).jd

mercury_x = float(Horizons(id=1, location="@sun", epochs=time).vectors()["x"])
mercury_y = float(Horizons(id=1, location="@sun", epochs=time).vectors()["y"])
mercury_vx = float(Horizons(id=1, location="@sun", epochs=time).vectors()["vx"])
mercury_vy = float(Horizons(id=1, location="@sun", epochs=time).vectors()["vy"])
venus_x = float(Horizons(id=2, location="@sun", epochs=time).vectors()["x"])
venus_y = float(Horizons(id=2, location="@sun", epochs=time).vectors()["y"])
venus_vx = float(Horizons(id=2, location="@sun", epochs=time).vectors()["vx"])
venus_vy = float(Horizons(id=2, location="@sun", epochs=time).vectors()["vy"])
earth_x = float(Horizons(id=3, location="@sun", epochs=time).vectors()["x"])
earth_y = float(Horizons(id=3, location="@sun", epochs=time).vectors()["y"])
earth_vx = float(Horizons(id=3, location="@sun", epochs=time).vectors()["vx"])
earth_vy = float(Horizons(id=3, location="@sun", epochs=time).vectors()["vy"])
mars_x = float(Horizons(id=4, location="@sun", epochs=time).vectors()["x"])
mars_y = float(Horizons(id=4, location="@sun", epochs=time).vectors()["y"])
mars_vx = float(Horizons(id=4, location="@sun", epochs=time).vectors()["vx"])
mars_vy = float(Horizons(id=4, location="@sun", epochs=time).vectors()["vy"])
jupiter_x = float(Horizons(id=5, location="@sun", epochs=time).vectors()["x"])
jupiter_y = float(Horizons(id=5, location="@sun", epochs=time).vectors()["y"])
jupiter_vx = float(Horizons(id=5, location="@sun", epochs=time).vectors()["vx"])
jupiter_vy = float(Horizons(id=5, location="@sun", epochs=time).vectors()["vy"])
saturn_x = float(Horizons(id=6, location="@sun", epochs=time).vectors()["x"])
saturn_y = float(Horizons(id=6, location="@sun", epochs=time).vectors()["y"])
saturn_vx = float(Horizons(id=6, location="@sun", epochs=time).vectors()["vx"])
saturn_vy = float(Horizons(id=6, location="@sun", epochs=time).vectors()["vy"])
uranus_x = float(Horizons(id=7, location="@sun", epochs=time).vectors()["x"])
uranus_y = float(Horizons(id=7, location="@sun", epochs=time).vectors()["y"])
uranus_vx = float(Horizons(id=7, location="@sun", epochs=time).vectors()["vx"])
uranus_vy = float(Horizons(id=7, location="@sun", epochs=time).vectors()["vy"])
neptune_x = float(Horizons(id=8, location="@sun", epochs=time).vectors()["x"])
neptune_y = float(Horizons(id=8, location="@sun", epochs=time).vectors()["y"])
neptune_vx = float(Horizons(id=8, location="@sun", epochs=time).vectors()["vx"])
neptune_vy = float(Horizons(id=8, location="@sun", epochs=time).vectors()["vy"])
pluto_x = float(Horizons(id=9, location="@sun", epochs=time).vectors()["x"])
pluto_y = float(Horizons(id=9, location="@sun", epochs=time).vectors()["y"])
pluto_vx = float(Horizons(id=9, location="@sun", epochs=time).vectors()["vx"])
pluto_vy = float(Horizons(id=9, location="@sun", epochs=time).vectors()["vy"])
conn.execute("""INSERT OR IGNORE INTO LUNAR_ECLIPSES VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", (lunar_eclipse_dates.date25, mercury_x, mercury_y, mercury_vx, mercury_vy, venus_x, venus_y, venus_vx, venus_vy, earth_x, earth_y, earth_vx, earth_vy, mars_x, mars_y, mars_vx, mars_vy, jupiter_x, jupiter_y, jupiter_vx, jupiter_vy, saturn_x, saturn_y, saturn_vx, saturn_vy, uranus_x, uranus_y, uranus_vx, uranus_vy, neptune_x, neptune_y, neptune_vx, neptune_vy, pluto_x, pluto_y, pluto_vx, pluto_vy))




# QUERY FOR ALL BODIES
# print("Entire BODIES table")
# cursor.execute("""SELECT * FROM BODIES""")
# query_result = cursor.fetchall()
# for i in query_result:
# 	print(i)

conn.commit() 

conn.close()
