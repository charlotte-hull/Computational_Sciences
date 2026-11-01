'''
==============
Exercise 3.1.2
==============
Select a unique time integrator out of the ones given in the lecture notes. 
Implement that time integrator going through the entire development cycle
'''
# %%
import numpy as np
import matplotlib.pyplot as plt
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
# %%
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
class Integrator:
    def __init__(self, time_step: float):
        self.time_step = time_step

    def integrate(self, state: State):
        raise NotImplementedError("Integrator subclasses must implement the integrate method.")

    def apply_forces(self, state: State):
        apply_lennard_jones_forces_to_particles(state)

    def reset_forces(self, state: State):
        state.force.fill(0)  # Reset forces after integration
# %%
class Explicit_euler(Integrator):
    def integrate(self, state: State):
        self.apply_forces(state)
        state.position += state.velocity * self.time_step
        state.velocity += state.force * self.time_step
        self.reset_forces(state)
# %%
class Heuns_method(Integrator):
    def compute_intermediate_state(self, state: State):
        intermediate_state = State(np.copy(state.position), np.copy(state.velocity), np.copy(state.force))
        intermediate_state.position += intermediate_state.velocity * self.time_step
        intermediate_state.velocity += intermediate_state.force * self.time_step
        self.reset_forces(intermediate_state)
        self.apply_forces(intermediate_state)
        return intermediate_state

    def integrate(self, state: State):
        # Update forces of the current state before integration
        self.apply_forces(state)

        # Compute intermediate state using Euler step
        intermediate_state = self.compute_intermediate_state(state)

        # Update original state using average of initial and intermediate forces and velocities
        state.position += 0.5 * self.time_step * (state.velocity + intermediate_state.velocity)
        state.velocity += 0.5 * self.time_step * (state.force + intermediate_state.force)
        self.reset_forces(state)
# %%
class Runge_kutta(Integrator):
    def compute_intermediate_state(self, state: State, slope: State, time_step: float):
        intermediate_state = State(np.copy(state.position), np.copy(state.velocity), np.copy(state.force))
        intermediate_state.position += slope.velocity * time_step
        intermediate_state.velocity += slope.force * time_step
        self.reset_forces(intermediate_state)
        self.apply_forces(intermediate_state)
        return intermediate_state
        
    def integrate(self, state: State):
        # Update forces of the current state before integration
        self.apply_forces(state)

        # Compute intermediate states
        slope_1 = State(np.copy(state.position), np.copy(state.velocity), np.copy(state.force))
        slope_2 = self.compute_intermediate_state(state, slope_1, 0.5 * self.time_step)
        slope_3 = self.compute_intermediate_state(state, slope_2, 0.5 * self.time_step)
        slope_4 = self.compute_intermediate_state(state, slope_3, self.time_step)

        # Update original state using weighted average of forces and velocities
        state.position += (self.time_step / 6.0) * (slope_1.velocity + 2 * slope_2.velocity + 2 * slope_3.velocity + slope_4.velocity)
        state.velocity += (self.time_step / 6.0) * (slope_1.force + 2 * slope_2.force + 2 * slope_3.force + slope_4.force)
        self.reset_forces(state)