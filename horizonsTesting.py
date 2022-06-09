
from astroquery.jplhorizons import Horizons
from astropy.time import Time

# The main package we're using is [JPL Horizons](https://ssd.jpl.nasa.gov/horizons.cgi).
# Nasa Id - 0 is barycenter of the solar system (we should define barycenter somewhere) 
#-> 1 is Mercury -> 2 is Venus -> 3 is Earth -> 4 is Mars -> 5 is Jupiter -> 6 is Saturn -> 7 is Uranus -> 8 is Neptune -> 9 is Pluto
#I haven't found a list of these yet in documentation but it would be helpful to have.

sim_start_date = "2018-01-01"     # simulating a solar system starting from this date
time = Time(sim_start_date).jd
nasaid = 1 # Mercury

mercury = Horizons(id=nasaid, location="@sun", epochs=time).vectors() # fetches the vectors 
print(mercury)

Venus = Horizons(id=2, location="@sun", epochs=time).ephemerides() #ephemerides is a bunch of other data we can fetch
print(Venus)