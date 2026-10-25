'''
Exercise 1.3.2 - Consider a point of mass m at height z with its motion being governed by Newton's equation
where g is the gravitational constant. Calculate the analytical trajectory of the point mass given the initial conditions z0
and v0. 
Implement the solution in Python so that the user can specify the initial conditions and the physical constants of mass
and gravitation and plot the graph of the solution.
'''
#%%
import matplotlib.pyplot as plt
import numpy as np

from compsci.exercise_1_3_1 import State, Constants, Trajectory, evaluate_states_at_times
# %%
def evaluate_states_at_times_with_update(time_grid: np.ndarray, initial_state: State, constants: Constants):
    trajectory = Trajectory(State(initial_state.position, initial_state.velocity))
    state = State(initial_state.position, initial_state.velocity)
    for i in range(1, len(time_grid)):
        dt = time_grid[i] - time_grid[i - 1]
        state = update_state(dt, state, constants)
        state_to_append = State(state.position, state.velocity)
        trajectory.append_state(state_to_append)
    return trajectory

def update_state(dt: float, state: State, constants: Constants):
    state.position = state.position + state.velocity * dt - 0.5 * constants.gravitation * dt**2
    state.velocity = state.velocity - constants.gravitation * dt
    return state
# %%
if __name__ == "__main__":
    time_grid = np.linspace(0, 10, 100)
    initial_state = State(position=10.0, velocity=0.0)
    constants = Constants(mass=1.0, gravitation=9.81)
    trajectory_with_update = evaluate_states_at_times_with_update(time_grid, initial_state, constants)

    plt.plot(time_grid, trajectory_with_update.get_positions(), label='Position (update)', linestyle='-')
    plt.plot(time_grid, trajectory_with_update.get_velocities(), label='Velocity (update)', linestyle='-')
    plt.plot(time_grid, evaluate_states_at_times(time_grid, initial_state, constants).get_positions(), label='Position', linestyle='--')
    plt.plot(time_grid, evaluate_states_at_times(time_grid, initial_state, constants).get_velocities(), label='Velocity', linestyle='--')

    plt.xlabel(r'Time in $s$')
    plt.ylabel(r'Position in $m$ / Velocity in $m/s$')
    plt.title('Trajectory of a Point Mass')
    plt.grid(True)
    plt.legend()
    plt.show()
# %%