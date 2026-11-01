'''
==============
Exercise 3.1.2
==============
Implement a function calculating this force for a given distance. Then imple-
ment a function that applies the according forces to a group of particles taking
into account the predefined State class in the base repo.
'''
# %%
import numpy as np

from compsci.exercise_3.data import State
# %%
def apply_lennard_jones_forces_to_particles(state: State):
    # TODO: implement the application of the Lennard-Jones force to the particles stored in state
    return 

def compute_lennard_jones_radial_force(distance: float):
    # TODO: implement the calculation of the Lennard-Jones radial force for a given distance
    return # force
# %%
if __name__ == "__main__":
    # Example usage
    positions = np.array([[0.0, 1.5, 2.0], [1.0, 0.0, 0.0]])
    velocities = np.array([[0.0, 0.0, 0.0], [0.0, 0.0, 0.0]])
    state = State(positions, velocities)
    apply_lennard_jones_forces_to_particles(state)

    # if this passes without assertion error, the forces are computed correctly
    assert(np.isclose(state.force, np.array([[0.0086412,  -0.0129618,  -0.01728239], [-0.0086412,   0.0129618,   0.01728239]])).all())
# %%
