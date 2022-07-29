#MUTUAL PLANETARY CONJUNCTIONS- planets eclipsing eachother from earths perspective
#missing uranus-neptune conjunction

import sqlite3
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from astropy.time import Time
from astroquery.jplhorizons import Horizons
import conj
from conj import *

conn = sqlite3.connect('Database.db')

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
conn.execute(sql_command)

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

mercury_x = float(Horizons(id=mercury_id, location="@sun", epochs=Time(conj.date21).jd).vectors()["x"])
mercury_y = float(Horizons(id=mercury_id, location="@sun", epochs=Time(conj.date21).jd).vectors()["y"])
mercury_vx = float(Horizons(id=mercury_id, location="@sun", epochs=Time(conj.date21).jd).vectors()["vx"])
mercury_vy = float(Horizons(id=mercury_id, location="@sun", epochs=Time(conj.date21).jd).vectors()["vy"])

venus_x = float(Horizons(id=venus_id, location="@sun", epochs=Time(conj.date21).jd).vectors()["x"])
venus_y = float(Horizons(id=venus_id, location="@sun", epochs=Time(conj.date21).jd).vectors()["y"])
venus_vx = float(Horizons(id=venus_id, location="@sun", epochs=Time(conj.date21).jd).vectors()["vx"])
venus_vy = float(Horizons(id=venus_id, location="@sun", epochs=Time(conj.date21).jd).vectors()["vy"])

earth_x = float(Horizons(id=earth_id, location="@sun", epochs=Time(conj.date21).jd).vectors()["x"])
earth_y = float(Horizons(id=earth_id, location="@sun", epochs=Time(conj.date21).jd).vectors()["y"])
earth_vx = float(Horizons(id=earth_id, location="@sun", epochs=Time(conj.date21).jd).vectors()["vx"])
earth_vy = float(Horizons(id=earth_id, location="@sun", epochs=Time(conj.date21).jd).vectors()["vy"])

mars_x = float(Horizons(id=mars_id, location="@sun", epochs=Time(conj.date21).jd).vectors()["x"])
mars_y = float(Horizons(id=mars_id, location="@sun", epochs=Time(conj.date21).jd).vectors()["y"])
mars_vx = float(Horizons(id=mars_id, location="@sun", epochs=Time(conj.date21).jd).vectors()["vx"])
mars_vy = float(Horizons(id=mars_id, location="@sun", epochs=Time(conj.date21).jd).vectors()["vy"])

jupiter_x = float(Horizons(id=jupiter_id, location="@sun", epochs=Time(conj.date21).jd).vectors()["x"])
jupiter_y = float(Horizons(id=jupiter_id, location="@sun", epochs=Time(conj.date21).jd).vectors()["y"])
jupiter_vx = float(Horizons(id=jupiter_id, location="@sun", epochs=Time(conj.date21).jd).vectors()["vx"])
jupiter_vy = float(Horizons(id=jupiter_id, location="@sun", epochs=Time(conj.date21).jd).vectors()["vy"])

saturn_x = float(Horizons(id=saturn_id, location="@sun", epochs=Time(conj.date21).jd).vectors()["x"])
saturn_y = float(Horizons(id=saturn_id, location="@sun", epochs=Time(conj.date21).jd).vectors()["y"])
saturn_vx = float(Horizons(id=saturn_id, location="@sun", epochs=Time(conj.date21).jd).vectors()["vx"])
saturn_vy = float(Horizons(id=saturn_id, location="@sun", epochs=Time(conj.date21).jd).vectors()["vy"])

uranus_x = float(Horizons(id=uranus_id, location="@sun", epochs=Time(conj.date21).jd).vectors()["x"])
uranus_y = float(Horizons(id=uranus_id, location="@sun", epochs=Time(conj.date21).jd).vectors()["y"])
uranus_vx = float(Horizons(id=uranus_id, location="@sun", epochs=Time(conj.date21).jd).vectors()["vx"])
uranus_vy = float(Horizons(id=uranus_id, location="@sun", epochs=Time(conj.date21).jd).vectors()["vy"])

neptune_x = float(Horizons(id=neptune_id, location="@sun", epochs=Time(conj.date21).jd).vectors()["x"])
neptune_y = float(Horizons(id=neptune_id, location="@sun", epochs=Time(conj.date21).jd).vectors()["y"])
neptune_vx = float(Horizons(id=neptune_id, location="@sun", epochs=Time(conj.date21).jd).vectors()["vx"])
neptune_vy = float(Horizons(id=neptune_id, location="@sun", epochs=Time(conj.date21).jd).vectors()["vy"])

pluto_x = float(Horizons(id=pluto_id, location="@sun", epochs=Time(conj.date21).jd).vectors()["x"])
pluto_y = float(Horizons(id=pluto_id, location="@sun", epochs=Time(conj.date21).jd).vectors()["y"])
pluto_vx = float(Horizons(id=pluto_id, location="@sun", epochs=Time(conj.date21).jd).vectors()["vx"])
pluto_vy = float(Horizons(id=pluto_id, location="@sun", epochs=Time(conj.date21).jd).vectors()["vy"])

conn.execute("""INSERT OR IGNORE INTO CONJUNCTION VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", (conj.date21, saturn_id, uranus_id, mercury_x, mercury_y, mercury_vx, mercury_vy, venus_x, venus_y, venus_vx, venus_vy, earth_x, earth_y, earth_vx, earth_vy, mars_x, mars_y, mars_vx, mars_vy, jupiter_x, jupiter_y, jupiter_vx, jupiter_vy, saturn_x, saturn_y, saturn_vx, saturn_vy, uranus_x, uranus_y, uranus_vx, uranus_vy, neptune_x, neptune_y, neptune_vx, neptune_vy, pluto_x, pluto_y, pluto_vx, pluto_vy))

conn.commit()
conn.close()