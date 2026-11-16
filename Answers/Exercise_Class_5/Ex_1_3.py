"""
Implement a function that applies the force exhibited by the harmonic potential
to a system of particles in analogy to the Lennard-Jones potential of exercise 3.
"""

import numpy as np
import matplotlib.pyplot as plt

from Answers.Exercise_Class_5.Ex_1_2 import apply_HO_force as ho
from compsci.integration import Integrator
from compsci.data import State
from compsci.interaction import apply_harmonic_oscillator_forces_to_particles 
from compsci.integration import Explicit_euler
from compsci.integration import Runge_kutta

state_exp_euler = State(np.array([[1.0]]), np.array([[1.0]]))
state_rk=State(np.array([[1.0]]), np.array([[1.0]]))

dt = 0.01
time = np.arange(dt, 100, dt)
tolerance = 0.01

velocity_ee = np.zeros((len(time),1))
position_ee = np.zeros((len(time),1))
velocity_rk = np.zeros((len(time),1))
position_rk = np.zeros((len(time),1))

ee = Explicit_euler(dt, ho)
rk= Runge_kutta(dt, ho)

for i in range(len(time)):

    ee.integrate(state_exp_euler)
    rk.integrate(state_rk)

    velocity_ee[i] = state_exp_euler.velocity[0]
    position_ee[i] = state_exp_euler.position[0]
    velocity_rk[i] = state_rk.velocity[0]
    position_rk[i] = state_rk.position[0]

plt.subplot(221)
plt.plot(time, velocity_ee)
plt.plot(time, velocity_rk)

plt.subplot(222)
plt.plot(time,position_ee)
plt.plot(time,position_rk)

plt.subplot(223)
plt.plot(velocity_ee,position_ee)
plt.plot(velocity_rk,position_rk)

plt.show()
