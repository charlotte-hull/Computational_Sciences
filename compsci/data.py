# %%
import numpy as np
# %%
class State:
    def __init__(self, position: np.ndarray, velocity: np.ndarray, force = None):
        assert(position.shape == velocity.shape) # assert that positions and velocities are consistent
        assert(len(position.shape) == 2) # assert that positions and velocities are rank 2 (num_particles, dim)
        assert(position.shape[0] > 0) # assert that there is at least one particle
        assert(position.shape[1] > 0) # assert that the dimension of the space is larger than zero

        self.position = np.copy(position)
        self.velocity = np.copy(velocity)

        if force is None:
            self.force = np.zeros_like(position)
        else:
            assert(force.shape == position.shape) # assert that force has the same shape as position
            self.force = np.copy(force)
# %%
class Trajectory:
    def __init__(self, initial_state: State):
        self.states = [State(initial_state.position, initial_state.velocity, initial_state.force)]

    def append(self, state: State):
        self.states.append(state)

    def get_state_at_step(self, step: int):
        return self.states[step]

    def get_positions(self):
        return np.array([state.position for state in self.states])

    def get_velocities(self):
        return np.array([state.velocity for state in self.states])

    def get_forces(self):
        return np.array([state.force for state in self.states])