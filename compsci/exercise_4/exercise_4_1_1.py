# %%
import numpy as np
import matplotlib.pyplot as plt

from compsci.exercise_3.data import State
from compsci.exercise_3.integration import Explicit_euler, Heuns_method, Runge_kutta, Implicit_euler
from compsci.exercise_3.util import compute_phase_distance
# %%
positions = np.array([[0.0, 1.5, 2.0], [1.0, 0.0, 0.0]])
velocities = np.array([[0.0, 0.0, 0.0], [0.0, 0.0, 0.0]])
state_ee = State(positions, velocities)
state_heun = State(positions, velocities)
state_rk = State(positions, velocities)
state_ie = State(positions, velocities)
time_step = 0.01
time_steps = 10000
tolerance = 1e-6
# %%
# initialize time grid and integrators
time_grid = np.arange(0, time_steps * time_step, time_step)
integrator_ee = Explicit_euler(time_step)
integrator_heun = Heuns_method(time_step)
integrator_rk = Runge_kutta(time_step)
integrator_ie = Implicit_euler(time_step, tolerance)

# initialize output 
distance_ee = np.zeros_like(time_grid)
distance_heun = np.zeros_like(time_grid)
distance_rk = np.zeros_like(time_grid)
distance_ie = np.zeros_like(time_grid)
# %%
state_ref = State(positions, velocities)
resolution = 10
time_grid_ref = np.arange(0, time_steps * time_step, time_step/resolution)
trajectory = [State(positions, velocities)]
# integrate reference state over time
integrator_ref = Runge_kutta(time_step/resolution)
for idx, t in enumerate(time_grid_ref):
    print("ref step =", idx, end='\r')
    integrator_ref.integrate(state_ref)
    if idx % resolution == 0 and idx != 0:
        trajectory.append(State(state_ref.position, state_ref.velocity))
# %%
# integrate state over time 
for idx, t in enumerate(time_grid):
    print("step =", idx, end='\r')

    integrator_ee.integrate(state_ee)
    integrator_heun.integrate(state_heun)
    integrator_rk.integrate(state_rk)
    integrator_ie.integrate(state_ie)

    distance_ee[idx] = compute_phase_distance(trajectory[idx], state_ee)
    distance_heun[idx] = compute_phase_distance(trajectory[idx], state_heun)
    distance_rk[idx] = compute_phase_distance(trajectory[idx], state_rk)
    distance_ie[idx] = compute_phase_distance(trajectory[idx], state_ie)
# %%
plt.plot(time_grid, distance_ee, label='Explicit Euler')
plt.plot(time_grid, distance_heun, label="Heun's Method")
plt.plot(time_grid, distance_rk, label='Runge-Kutta')
plt.plot(time_grid, distance_ie, label='Implicit Euler')
plt.ylim(0, 10)
plt.xlabel(r'Time in $\tau$')
plt.ylabel(r'Phase Distance in $1$')
plt.legend()
plt.show()
# %%