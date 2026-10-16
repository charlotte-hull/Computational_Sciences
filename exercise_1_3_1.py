'''
Exercise 1.3.1 - Consider a point of mass m at height z with its motion being governed by Newton's equation
where g is the gravitational constant. Calculate the analytical trajectory of the point mass given the initial conditions z0
and v0. 
Implement the solution in Python so that the user can specify the initial conditions and the physical constants of mass
and gravitation and plot the graph of the solution.
'''
#%%
import matplotlib.pyplot as plt
import numpy as np
# %%
class State:
    def __init__(self, position: float, velocity: float):
        self.position = position
        self.velocity = velocity

class Constants:
    def __init__(self, mass: float, gravitation: float):
        self.mass = mass
        self.gravitation = gravitation

class Trajectory:
    def __init__(self, initial_state: State):
        self.positions = np.array([initial_state.position])
        self.velocities = np.array([initial_state.velocity])

    def append_state(self, state: State):
        self.positions = np.append(self.positions, state.position)
        self.velocities = np.append(self.velocities, state.velocity)

    def get_state_at_step(self, step: int):
        return State(self.positions[step], self.velocities[step])

    def get_positions(self):
        return np.copy(self.positions)

    def get_velocities(self):
        return np.copy(self.velocities)

def evaluate_states_at_times(time_grid: np.ndarray, initial_state: State, constants: Constants):
    trajectory = Trajectory(initial_state)
    for t in time_grid:
        trajectory.append_state(evaluate_state_at_time(t, initial_state, constants))
    return trajectory

def evaluate_state_at_time(time: float, initial_state: State, constants: Constants):
    position = initial_state.position + initial_state.velocity * time - 0.5 * constants.gravitation * time**2
    velocity = initial_state.velocity - constants.gravitation * time
    return State(position, velocity)
# %%
time_grid = np.linspace(0, 10, 100)
initial_state = State(position=10.0, velocity=0.0)
constants = Constants(mass=1.0, gravitation=9.81)
trajectory = evaluate_states_at_times(time_grid, initial_state, constants)

plt.plot(time_grid, trajectory.get_positions()[1:], label='Position')
plt.plot(time_grid, trajectory.get_velocities()[1:], label='Velocity')
plt.xlabel(r'Time in $s$')
plt.ylabel(r'Position in $m$ / Velocity in $m/s$')
plt.title('Trajectory of a Point Mass')
plt.grid(True)
plt.legend()
plt.show()
# %%
