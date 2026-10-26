#%%
import numpy as np
#%%
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
        self.states = [initial_state]

    def append_state(self, state: State):
        self.states.append(state)

    def get_state_at_step(self, step: int):
        return self.states[step]

    def get_positions(self):
        return np.array([state.position for state in self.states])

    def get_velocities(self):
        return np.array([state.velocity for state in self.states])
#%%
def evaluate_states_at_times(time_grid: np.ndarray, initial_state: State, constants: Constants):
    trajectory = Trajectory(initial_state)
    for t in time_grid[1:]:
        trajectory.append_state(evaluate_state_at_time(t, initial_state, constants))
    return trajectory

def evaluate_state_at_time(time: float, initial_state: State, constants: Constants):
    state = State(initial_state.position, initial_state.velocity)
    update_state(time, state, constants)
    return state

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