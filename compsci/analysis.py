# %%
import numpy as np
# %%
# %%
def compute_kinetic_energy(velocities: np.ndarray):
    return 0.5 * np.sum(velocities**2)
# %%