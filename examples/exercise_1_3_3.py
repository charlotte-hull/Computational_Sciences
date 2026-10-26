'''
Exercise 1.3.1 - Modularize your code such that you have an example script taking 
care of the plotting which simply imports the required functions from the package compsci.
Save your changes in your forked remote repository.
'''
# %%
import matplotlib.pyplot as plt
import numpy as np

from compsci.exercise_1.gravitation import State, Constants, evaluate_states_at_times, evaluate_states_at_times_with_update
# %%
time_grid = np.linspace(0, 10, 100)
initial_state = State(position=10.0, velocity=0.0)
constants = Constants(mass=1.0, gravitation=9.81)
trajectory = evaluate_states_at_times(time_grid, initial_state, constants)
trajectory_with_update = evaluate_states_at_times_with_update(time_grid, initial_state, constants)

plt.plot(time_grid, trajectory_with_update.get_positions(), label='Position (update)', linestyle='-')
plt.plot(time_grid, trajectory_with_update.get_velocities(), label='Velocity (update)', linestyle='-')
plt.plot(time_grid, trajectory.get_positions(), label='Position', linestyle='--')
plt.plot(time_grid, trajectory.get_velocities(), label='Velocity', linestyle='--')

plt.xlabel(r'Time in $s$')
plt.ylabel(r'Position in $m$ / Velocity in $m/s$')
plt.title('Trajectory of a Point Mass')
plt.grid(True)
plt.legend()
plt.show()
# %%
