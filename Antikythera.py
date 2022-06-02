#Base Class (Astronomical Body)
class Astro_Body:
   #Constructor 
   def __init__(self,mass,radius,volume,orbitvelocity,rotationvelocity,distance_sun):
       self.mass = mass
       self.radius = radius 
       self.volume = volume
       self.orbitvelocity = orbitvelocity
       self.rotationalvelocity = rotationalvelocity
       self.distance_sun = distance_sun
# Methods (Astronomical Body)

# Derived Class (Planet) 
class Planet(Astro_Body):
   def __init__(self,mass,radius,volume,orbitvelocity,rotationvelocity,distance_sun):
       super().__init__()

# Methods (Planets)

# Derived Class (Moon)
class Moon(Astro_Body):
   def __init__(self,mass,radius,volume,orbitvelocity,rotationvelocity,distance_sun):
       super().__init__()

# Methods (Moon)

# Derived Class (Stars)
class Star(Astro_Body):
    def __init__(self,mass,radius,volume,orbitvelocity,rotationvelocity,distance_sun):
       super().__init__()

# Methods (Stars)
 
# Derived Class (Comet) 
class Comet(Astro_Body):
    def __init__(self,mass,radius,volume,orbitvelocity,rotationvelocity,distance_sun):
       super().__init__()
# Methods (Comet)

# Derived Class (Asteroid)
class Asteroid(Astro_Body):
    def __init__(self,mass,radius,volume,orbitvelocity,rotationvelocity,distance_sun):
       super().__init__()

# Methods (Asteroid) 




    



    