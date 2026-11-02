# %%
import numpy as np

from compsci.exercise_3.data import State
# %%
def compute_phase_distance(state1: State, state2: State):
    position_diff = state1.position - state2.position
    velocity_diff = state1.velocity - state2.velocity
    return np.sqrt(np.sum(position_diff**2) + np.sum(velocity_diff**2))
# %%