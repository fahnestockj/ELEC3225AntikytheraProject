# IMPORTANT: Each function returns multiple variables, so in the main function, you need to set the function equal to a list when you call it.
# Example: conj_vectors = query.searchConj(date)
import sqlite3
database = sqlite3.connect("Database.db")

def searchConj(x):
    cursor = database.cursor()
    cursor.execute("""SELECT CONJUNCTION.DATE, CONJUNCTION.MERCURY_VX, CONJUNCTION.MERCURY_VY, CONJUNCTION.VENUS_VX, CONJUNCTION.VENUS_VY, CONJUNCTION.EARTH_VX, CONJUNCTION.EARTH_VY, CONJUNCTION.MARS_VX, CONJUNCTION.MARS_VY, CONJUNCTION.JUPITER_VX, CONJUNCTION.JUPITER_VY, CONJUNCTION.SATURN_VX, CONJUNCTION.SATURN_VY, CONJUNCTION.URANUS_VX, CONJUNCTION.URANUS_VY, CONJUNCTION.NEPTUNE_VX, CONJUNCTION.NEPTUNE_VY, CONJUNCTION.PLUTO_VX, CONJUNCTION.PLUTO_VY 
    FROM CONJUNCTION 
    WHERE DATE LIKE ?
    """, (f'%{x}',))

    vector_result = cursor.fetchall()
    for i in vector_result:
        startDate = vector_result[0][0]
        startMercury_vx = vector_result[0][1]
        startMercury_vy = vector_result[0][2]
        startVenus_vx = vector_result[0][3]
        startVenus_vy = vector_result[0][4]
        startEarth_vx = vector_result[0][5]
        startEarth_vy = vector_result[0][6]
        startMars_vx = vector_result[0][7]
        startMars_vy = vector_result[0][8]
        startJupiter_vx = vector_result[0][9]
        startJupiter_vy = vector_result[0][10]
        startSaturn_vx = vector_result[0][11]
        startSaturn_vy = vector_result[0][12]
        startUranus_vx = vector_result[0][13]
        startUranus_vy = vector_result[0][14]
        startNeptune_vx = vector_result[0][15]
        startNeptune_vy = vector_result[0][16]
        startPluto_vx = vector_result[0][17]
        startPluto_vy = vector_result[0][18]
    database.commit()
    #print(str(startMercury_vx) + "\n")
    if(vector_result == []):
        return "No results found"

    return startDate, startMercury_vx, startMercury_vy, startVenus_vx, startVenus_vy, startEarth_vx, startEarth_vy, startMars_vx, startMars_vy, startJupiter_vx, startJupiter_vy, startSaturn_vx, startSaturn_vy, startUranus_vx, startUranus_vy, startNeptune_vx, startNeptune_vy, startPluto_vx, startPluto_vy

def searchSolar(x):
    cursor = database.cursor()
    cursor.execute("""SELECT SOLAR_ECLIPSES.DATE, SOLAR_ECLIPSES.MERCURY_VX, SOLAR_ECLIPSES.MERCURY_VY, SOLAR_ECLIPSES.VENUS_VX, SOLAR_ECLIPSES.VENUS_VY, SOLAR_ECLIPSES.EARTH_VX, SOLAR_ECLIPSES.EARTH_VY, SOLAR_ECLIPSES.MARS_VX, SOLAR_ECLIPSES.MARS_VY, SOLAR_ECLIPSES.JUPITER_VX, SOLAR_ECLIPSES.JUPITER_VY, SOLAR_ECLIPSES.SATURN_VX, SOLAR_ECLIPSES.SATURN_VY, SOLAR_ECLIPSES.URANUS_VX, SOLAR_ECLIPSES.URANUS_VY, SOLAR_ECLIPSES.NEPTUNE_VX, SOLAR_ECLIPSES.NEPTUNE_VY, SOLAR_ECLIPSES.PLUTO_VX, SOLAR_ECLIPSES.PLUTO_VY 
    FROM SOLAR_ECLIPSES 
    WHERE DATE LIKE ?
    """, (f'%{x}',))

    vector_result = cursor.fetchall()

    for i in vector_result:
        startDate = vector_result[0][0]
        startMercury_vx = vector_result[0][1]
        startMercury_vy = vector_result[0][2]
        startVenus_vx = vector_result[0][3]
        startVenus_vy = vector_result[0][4]
        startEarth_vx = vector_result[0][5]
        startEarth_vy = vector_result[0][6]
        startMars_vx = vector_result[0][7]
        startMars_vy = vector_result[0][8]
        startJupiter_vx = vector_result[0][9]
        startJupiter_vy = vector_result[0][10]
        startSaturn_vx = vector_result[0][11]
        startSaturn_vy = vector_result[0][12]
        startUranus_vx = vector_result[0][13]
        startUranus_vy = vector_result[0][14]
        startNeptune_vx = vector_result[0][15]
        startNeptune_vy = vector_result[0][16]
        startPluto_vx = vector_result[0][17]
        startPluto_vy = vector_result[0][18]
    database.commit()
    #print(str(startMercury_vx) + "\n")
    if(vector_result == []):
        return "no results found"
    return startDate, startMercury_vx, startMercury_vy, startVenus_vx, startVenus_vy, startEarth_vx, startEarth_vy, startMars_vx, startMars_vy, startJupiter_vx, startJupiter_vy, startSaturn_vx, startSaturn_vy, startUranus_vx, startUranus_vy, startNeptune_vx, startNeptune_vy, startPluto_vx, startPluto_vy

def searchLunar(x):
    cursor = database.cursor()
    cursor.execute("""SELECT LUNAR_ECLIPSES.DATE, LUNAR_ECLIPSES.MERCURY_VX, LUNAR_ECLIPSES.MERCURY_VY, LUNAR_ECLIPSES.VENUS_VX, LUNAR_ECLIPSES.VENUS_VY, LUNAR_ECLIPSES.EARTH_VX, LUNAR_ECLIPSES.EARTH_VY, LUNAR_ECLIPSES.MARS_VX, LUNAR_ECLIPSES.MARS_VY, LUNAR_ECLIPSES.JUPITER_VX, LUNAR_ECLIPSES.JUPITER_VY, LUNAR_ECLIPSES.SATURN_VX, LUNAR_ECLIPSES.SATURN_VY, LUNAR_ECLIPSES.URANUS_VX, LUNAR_ECLIPSES.URANUS_VY, LUNAR_ECLIPSES.NEPTUNE_VX, LUNAR_ECLIPSES.NEPTUNE_VY, LUNAR_ECLIPSES.PLUTO_VX, LUNAR_ECLIPSES.PLUTO_VY 
    FROM LUNAR_ECLIPSES 
    WHERE DATE LIKE ?
    """, (f'%{x}',))

    vector_result = cursor.fetchall()

    for i in vector_result:
        startDate = vector_result[0][0]
        startMercury_vx = vector_result[0][1]
        startMercury_vy = vector_result[0][2]
        startVenus_vx = vector_result[0][3]
        startVenus_vy = vector_result[0][4]
        startEarth_vx = vector_result[0][5]
        startEarth_vy = vector_result[0][6]
        startMars_vx = vector_result[0][7]
        startMars_vy = vector_result[0][8]
        startJupiter_vx = vector_result[0][9]
        startJupiter_vy = vector_result[0][10]
        startSaturn_vx = vector_result[0][11]
        startSaturn_vy = vector_result[0][12]
        startUranus_vx = vector_result[0][13]
        startUranus_vy = vector_result[0][14]
        startNeptune_vx = vector_result[0][15]
        startNeptune_vy = vector_result[0][16]
        startPluto_vx = vector_result[0][17]
        startPluto_vy = vector_result[0][18]
    database.commit()
    if(vector_result == []):
        return "no results found"

    #print(str(startMercury_vx) + "\n")
    return startDate, startMercury_vx, startMercury_vy, startVenus_vx, startVenus_vy, startEarth_vx, startEarth_vy, startMars_vx, startMars_vy, startJupiter_vx, startJupiter_vy, startSaturn_vx, startSaturn_vy, startUranus_vx, startUranus_vy, startNeptune_vx, startNeptune_vy, startPluto_vx, startPluto_vy

def searchBodies(x):
    cursor = database.cursor()
    cursor.execute("""SELECT BODIES.NAME, BODIES.MASS, BODIES.RADIUS, BODIES.VOLUME, BODIES.ORBITAL, BODIES.ROTATIONAL, BODIES.DISTANCE
    FROM BODIES 
    WHERE NAME LIKE ?
    """, (f'%{x}',))

    vector_result = cursor.fetchall()

    for i in vector_result:
        name = vector_result[0][0]
        mass = vector_result[0][1]
        radius = vector_result[0][2]
        volume = vector_result[0][3]
        orbital = vector_result[0][4]
        rotational = vector_result[0][5]
        distance = vector_result[0][6]
    database.commit()
    if(vector_result == []):
      return "no results found"
    return name, mass, radius, volume, orbital, rotational, distance

def searchMoons(x):
    cursor = database.cursor()
    cursor.execute("""SELECT MOON.MOON, MOON.PLANET, MOON.MASS, MOON.RADIUS, MOON.VOLUME, MOON.ORBITAL, MOON.ROTATIONAL, MOON.AVG
    FROM MOON 
    WHERE MOON LIKE ?
    """, (f'%{x}',))

    vector_result = cursor.fetchall()

    for i in vector_result:
        moon = vector_result[0][0]
        planet = vector_result[0][1]
        mass = vector_result[0][2]
        radius = vector_result[0][3]
        volume = vector_result[0][4]
        orbital = vector_result[0][5]
        rotational = vector_result[0][6]
        avg = vector_result[0][7]
    database.commit()
    if(vector_result == []):
      return "no results found"
    return moon, planet, mass, radius, volume, orbital, rotational, avg


def close():
    database.close()