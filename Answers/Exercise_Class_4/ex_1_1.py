'''
Write a python program using the solutions to the exercises that integrates the
initial state of a 2-particle system. At each point in time, create a data point of
the phase distance and store it in an array that has the same dimensions as the
time grid. Plot the data against the time grid.
How do the different integrators perform in terms of that observable? Does it
always make sense to choose the "best" one amongst them? How does the graph
change with time step size and number of time steps?
What happens if you put the two particles on the same initial positions? Why
does that happen?
'''
import numpy as np
import matplotlib.pyplot as plt

from compsci.exercise_3.integration import Explicit_euler 
from compsci.exercise_3.integration import Heuns_method
from compsci.exercise_3.integration import Runge_kutta
from compsci.exercise_3.integration import Implicit_euler

from compsci.exercise_3.util import compute_phase_distance as phase
from compsci.exercise_3.data import State


dt=0.01
time=np.arange(dt,10,dt)
distance_ee=np.zeros(len(time))
distance_heun=np.zeros(len(time))
distance_IE=np.zeros(len(time))
positions = np.array([[0.0,1.5,2.0],[1.0,0.0,0.0]])
velocities = np.array(([0.0,0.0,0.0],[0.0,0.0,0.0]))
tolerance=0.01

state1=State(positions,velocities)
state2=State(positions,velocities)
state3=State(positions,velocities)
state4=State(positions,velocities)

ref=np.zeros(len(time))
runge=Runge_kutta(dt)
ie=Implicit_euler(dt,tolerance)
ee= Explicit_euler(dt)
heun = Heuns_method(dt)
    
for i in range(len(time)):
    ee.integrate(state1)
    runge.integrate(state2)
    heun.integrate(state3)
    ie.integrate(state4)
    distance_ee[i]=phase(state2,state1)
    distance_heun[i]=phase(state2,state3)
    distance_IE[i]=phase(state2,state4)
    

plt.plot(time,distance_ee)
plt.plot(time,distance_heun)
plt.plot(time,distance_IE)
plt.ylim(-0.2,2)
plt.show()







