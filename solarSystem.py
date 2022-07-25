# code from https://medium.com/analytics-vidhya/simulating-the-solar-system-with-under-100-lines-of-python-code-5c53b3039fc6
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from astropy.time import Time
from astroquery.jplhorizons import Horizons
from matplotlib.widgets import Button
from tabulate import tabulate


def simulation(simStartDate: str, simLength: str):
  sim_start_date = simStartDate # start date in yyyy-mm-dd format
  sim_duration = int(simLength) - 1 # sim stops 1 day after sim_duration so we just subtract 1

  
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
          self.planetText1 = ax.text(.7, .70, '', color='w', transform=ax.transAxes, fontsize='medium', horizontalalignment='left')
          self.planetText2 = ax.text(.8, .70, '', color='w', transform=ax.transAxes, fontsize='medium', horizontalalignment='left')
          self.planetText3 = ax.text(.9, .70, '', color='w', transform=ax.transAxes, fontsize='medium', horizontalalignment='left')
          self.chartDescription = ax.text(0.6, 0.95, 'Distance from the Barycenter of the Sun in AU', color='white', transform=ax.transAxes, fontsize='large', horizontalalignment='left')
      def add_planet(self, planet):
          self.planets.append(planet)
      def evolve(self):           # evolve the trajectories
          dt = 1.0
          self.time += dt
          plots = []
          lines = []
          for p in self.planets:
              p.r += p.v * dt
              acc = -2.959e-4 * p.r / np.sum(p.r**2)**(3./2)   # in units of AU/day^2
              p.v += acc * dt
              p.xs.append(p.r[0])
              p.ys.append(p.r[1])
              p.plot.set_offsets(p.r[:2])
              p.line.set_xdata(p.xs)
              p.line.set_ydata(p.ys)
              plots.append(p.plot)
              lines.append(p.line)
          self.timestamp.set_text('Date: ' + Time(self.time, format='jd', out_subfmt='float').iso[0:11])
          table1 = []
          table2 = []
          table3 = []
          table1.append(['Name'])
          table2.append(['X']) # , 'X', 'Y'
          table3.append(['Y'])
          for p in self.planets:
            table1.append([p.name])
            table2.append([str(round(p.r[0],4))])
            table3.append([str(round(p.r[1],4))])
          planetText1 = tabulate(table1, headers='firstrow', tablefmt='simple', floatfmt='.4f', numalign='left')
          planetText2 = tabulate(table2, headers='firstrow', tablefmt='simple', floatfmt='.4f', numalign='left')
          planetText3 = tabulate(table3, headers='firstrow', tablefmt='simple', floatfmt='.4f', numalign='left')
          self.planetText1.set_text(planetText1)
          self.planetText2.set_text(planetText2)
          self.planetText3.set_text(planetText3)
          
          #Animate sensitivity list (what gets rerendered on each frame)
          return plots + lines + [self.timestamp, self.planetText1, self.planetText2, self.planetText3] 

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
  names = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']
  texty = [.47, .73, 1, 1.5, 7, 12, 22, 33.5, 36]
  innerPlanetNameTextInstances = []
  outerPlanetNameTextInstances = []
  for i, nasaid in enumerate([1, 2, 3, 4, 5, 6, 7, 8, 9]): 
      obj = Horizons(id=nasaid, location="@sun", epochs=ss.time).vectors()
      ss.add_planet(Object(names[i], 20 * newSizes[i], colors[i], 
                          [np.double(obj[xi]) for xi in ['x', 'y', 'z']], 
                          [np.double(obj[vxi]) for vxi in ['vx', 'vy', 'vz']]))
      txtInstance = ax.text(0, - (texty[i] + 0.1), names[i], color=colors[i], zorder=1000, ha='center', fontsize='large')
      if(i <= 3):
          innerPlanetNameTextInstances.append(txtInstance)
      else:
          outerPlanetNameTextInstances.append(txtInstance)
  for txt in innerPlanetNameTextInstances:
      txt.set_visible(False)
  def animate(i):
      return ss.evolve()

  class BTNCallbacks:
    def pause(self, event):
      ani.pause()
      plt.draw()

    def resume(self, event):
      ani.resume()
      plt.draw()

    def innerzoom(self, event):
      ax.set_xlim(-1.8, 1.8)
      ax.set_ylim(-1.8, 1.8)
      for txt in innerPlanetNameTextInstances:
          txt.set_visible(True)
      for txt in outerPlanetNameTextInstances:
          txt.set_visible(False)
      plt.draw()

    def outerzoom(self, event):
      ax.set_xlim(-40, 40)
      ax.set_ylim(-40, 40)
      for txt in innerPlanetNameTextInstances:
          txt.set_visible(False)
      for txt in outerPlanetNameTextInstances:
          txt.set_visible(True)
      plt.draw()

  #buttons!
  callback = BTNCallbacks()
  axPause = plt.axes([0.89, 0.05, 0.1, 0.075])
  bpause = Button(axPause, 'Pause', color='red', hovercolor='red')
  bpause.on_clicked(callback.pause)
  axResume = plt.axes([0.78, 0.05, 0.1, 0.075])
  bResume = Button(axResume, 'Resume', color='green', hovercolor='green')
  bResume.on_clicked(callback.resume)


  axInnerZoom = plt.axes([0.78, 0.15, 0.1, 0.075])
  bInnerZoom = Button(axInnerZoom, 'Inner Planets', color='gray', hovercolor='gray')
  bInnerZoom.on_clicked(callback.innerzoom)

  axOuterZoom = plt.axes([0.89, 0.15, 0.1, 0.075])
  bOuterZoom = Button(axOuterZoom, 'Outer Planets', color='gray', hovercolor='gray')
  bOuterZoom.on_clicked(callback.outerzoom)


  # What planet is the closest to earth
  ani = animation.FuncAnimation(fig, animate, repeat=False, frames=sim_duration, blit=True, interval=200,)
  plt.show()
  # ani.save('solar_system_6in_150dpi.mp4', fps=60, dpi=150)
