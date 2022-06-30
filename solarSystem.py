# code from https://medium.com/analytics-vidhya/simulating-the-solar-system-with-under-100-lines-of-python-code-5c53b3039fc6
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from astropy.time import Time
from astroquery.jplhorizons import Horizons
from matplotlib.widgets import Button

sim_start_date = "2018-01-01"     # simulating a solar system starting from this date
# sim_duration = 2 * 365                # (int) simulation duration in days
sim_duration = 2*365
 
class Object:                   # define the objects: the Sun, Earth, Mercury, etc
    def __init__(self, name, rad, color, r, v):
        self.name = name
        self.r    = np.array(r, dtype=float)
        self.v    = np.array(v, dtype=float)
        self.xs = []
        self.ys = []
        self.plot = ax.scatter(r[0], r[1], color=color, s=rad, edgecolors=None, zorder=10)
        self.line, = ax.plot([], [], color=color, linewidth=1.4)

class SolarSystem:
    def __init__(self, thesun):
        self.thesun = thesun
        self.planets = []
        self.time = None
        self.timestamp = ax.text(.03, .94, 'Date: ', color='w', transform=ax.transAxes, fontsize='x-large')
    def add_planet(self, planet):
        self.planets.append(planet)
    def evolve(self):           # evolve the trajectories
        dt = 1.0
        self.time += dt
        plots = []
        lines = []
        for p in self.planets:
            p.r += p.v * dt
            #print(str(p.name) + ": " + str(p.r))
            acc = -2.959e-4 * p.r / np.sum(p.r**2)**(3./2)   # in units of AU/day^2
            p.v += acc * dt
            p.xs.append(p.r[0])
            p.ys.append(p.r[1])
            p.plot.set_offsets(p.r[:2])
            p.line.set_xdata(p.xs)
            p.line.set_ydata(p.ys)
            plots.append(p.plot)
            lines.append(p.line)
        self.timestamp.set_text('Date: ' + Time(self.time, format='jd', out_subfmt='float').iso)
        return plots + lines + [self.timestamp]

plt.style.use('dark_background')
fig = plt.figure(figsize=[15, 8])
ax = plt.axes([0., 0., 1., 1.], xlim=(-40, 40), ylim=(-40, 40))
ax.set_aspect('equal')
ax.axis('off')
ss = SolarSystem(Object("Sun", 28, 'red', [0, 0, 0], [0, 0, 0]))
ss.time = Time(sim_start_date).jd
colors = ['gray', 'orange', 'blue', 'chocolate', 'green', 'red', 'purple', 'pink', 'brown']

# https://solarsystem.nasa.gov/resources/686/solar-system-sizes/
# Mercury – 1,516mi (2,440km) radius; about 1/3 the size of Earth
# Venus – 3,760mi (6,052km) radius; only slightly smaller than Earth
# Earth – 3,959mi (6,371km) radius
# Mars – 2,106mi (3,390km) radius; about half the size of Earth
# Jupiter – 43,441mi (69,911km) radius; 11x Earth’s size
# Saturn – 36,184mi (58,232km) radius; 9x larger than Earth
# Uranus – 15,759mi (25,362km) radius; 4x Earth’s size
# Neptune – 15,299mi (24,622km) radius; only slightly smaller than Uranus
sizes = [0.38, 0.95, 1., 0.53, 11.2, 9.0, 4.0, 3, 9]
newSizes = []
for size in sizes:
    newSizes.append(size/10)
# print(sizes)
names = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']
texty = [.47, .73, 1, 1.5, 6.2, 10, 15, 25, 35]
for i, nasaid in enumerate([1, 2, 3, 4, 5, 6, 7, 8, 9]):  # The 1st, 2nd, 3rd, 4th planet in solar system
    obj = Horizons(id=nasaid, location="@sun", epochs=ss.time).vectors()
    ss.add_planet(Object(names[i], 20 * newSizes[i], colors[i], 
                         [np.double(obj[xi]) for xi in ['x', 'y', 'z']], 
                         [np.double(obj[vxi]) for vxi in ['vx', 'vy', 'vz']]))
    ax.text(0, - (texty[i] + 0.1), names[i], color=colors[i], zorder=1000, ha='center', fontsize='large')
def animate(i):
    return ss.evolve()

class BTNCallbacks:
  def pause(self, event):
    ani.pause()
    plt.draw()

  def resume(self, event):
    ani.resume()

#buttons!
callback = BTNCallbacks()
axPause = plt.axes([0.81, 0.05, 0.1, 0.075])
bpause = Button(axPause, 'Pause', color='red', hovercolor='red')
bpause.on_clicked(callback.pause)
axResume = plt.axes([0.7, 0.05, 0.1, 0.075])
bResume = Button(axResume, 'Resume', color='green', hovercolor='green')
bResume.on_clicked(callback.resume)


# matplotlib table
cell_text
the_table = plt.table(cellText=cell_text,
                      rowLabels=rows,
                      rowColours=colors,
                      colLabels=columns,
                      loc='bottom')



ani = animation.FuncAnimation(fig, animate, repeat=False, frames=sim_duration, blit=True, interval=20,)

plt.show()
# ani.save('solar_system_6in_150dpi.mp4', fps=60, dpi=150)