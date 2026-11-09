# %%
import numpy as np
# %%
class State:
    def __init__(self, position: np.ndarray, velocity: np.ndarray, force = None):
        assert(position.shape == velocity.shape) # assert that positions and velocities are consistent
        assert(len(position.shape) == 2) # assert that positions and velocities are 2-dimensional (num_particles, dim)
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