# %%
import numpy as np

from compsci.data import State
#%%
def apply_lennard_jones_forces_to_particles(state: State):
    for idx in range(len(state.position)):
        for jdx in range(len(state.position)):
            if idx == jdx:
                continue
            displacement = state.position[idx] - state.position[jdx]
            distance = np.linalg.norm(displacement)
            force_magnitude = compute_lennard_jones_radial_force(distance)
            force_vector = force_magnitude * displacement / distance
            state.force[idx] += force_vector                

def compute_lennard_jones_radial_force(distance: float):
    return 24 * ((2 / distance**13) - (1 / distance**7))
# %%
def apply_harmonic_oscillator_forces_to_particles(state: State):
    for idx in range(len(state.position)):
        state.force[idx] += compute_harmonic_oscillator_single_particle_force(state.position[idx])

def compute_harmonic_oscillator_single_particle_force(position: float):
    return -position

def compute_harmonic_oscillator_many_particle_potential_energy(state: State):
    return 0.5 * np.sum(state.position**2)