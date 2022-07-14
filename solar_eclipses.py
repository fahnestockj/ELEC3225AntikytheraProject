import sqlite3
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from astropy.time import Time
from astroquery.jplhorizons import Horizons
import solar_eclipse_dates
from solar_eclipse_dates import *

conn = sqlite3.connect('solar_eclipses.db')

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
conn.execute("""INSERT OR IGNORE INTO SOLAR_ECLIPSES VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", (solar_eclipse_dates.date1, mercury_x, mercury_y, mercury_vx, mercury_vy, venus_x, venus_y, venus_vx, venus_vy, earth_x, earth_y, earth_vx, earth_vy, mars_x, mars_y, mars_vx, mars_vy, jupiter_x, jupiter_y, jupiter_vx, jupiter_vy, saturn_x, saturn_y, saturn_vx, saturn_vy, uranus_x, uranus_y, uranus_vx, uranus_vy, neptune_x, neptune_y, neptune_vx, neptune_vy, pluto_x, pluto_y, pluto_vx, pluto_vy))

conn.commit()
conn.close()