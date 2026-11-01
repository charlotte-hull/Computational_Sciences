# %%
import numpy as np

from compsci.exercise_3.interaction import apply_lennard_jones_forces_to_particles
from compsci.exercise_3.data import State
from compsci.exercise_3.util import compute_phase_distance
# %%
class Integrator_explicit:
    def __init__(self, time_step: float):
        self.time_step = time_step

    def integrate(self, state: State):
        raise NotImplementedError("Integrator subclasses must implement the integrate method.")

    def apply_forces(self, state: State):
        apply_lennard_jones_forces_to_particles(state)

    def reset_forces(self, state: State):
        state.force.fill(0)  # Reset forces after integration
# %%
class Explicit_euler(Integrator_explicit):
    def integrate(self, state: State):
        self.apply_forces(state)
        state.position += state.velocity * self.time_step
        state.velocity += state.force * self.time_step
        self.reset_forces(state)
# %%
class Heuns_method(Integrator_explicit):
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
class Runge_kutta(Integrator_explicit):
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
# %%
class Integrator_implicit:
    def __init__(self, time_step: float, tolerance: float, max_iterations: int = 10):
        self.time_step = time_step
        self.tolerance = tolerance
        self.max_iterations = max_iterations

    def integrate(self, state: State):
        raise NotImplementedError("Integrator subclasses must implement the integrate method.")

    def apply_forces(self, state: State):
        apply_lennard_jones_forces_to_particles(state)

    def reset_forces(self, state: State):
        state.force.fill(0)  # Reset forces after integration

class Implicit_euler(Integrator_implicit):
    def compute_intermediate_state(self, state: State):
        intermediate_state = State(np.copy(state.position), np.copy(state.velocity), np.copy(state.force))
        intermediate_state.position += intermediate_state.velocity * self.time_step
        intermediate_state.velocity += intermediate_state.force * self.time_step
        self.reset_forces(intermediate_state)
        self.apply_forces(intermediate_state)
        return intermediate_state

    def compute_corrected_state(self, state: State, intermediate_state: State):
        corrected_state = State(np.copy(state.position), np.copy(state.velocity), np.copy(state.force))
        corrected_state.position += intermediate_state.velocity * self.time_step
        corrected_state.velocity += intermediate_state.force * self.time_step
        self.reset_forces(corrected_state)
        self.apply_forces(corrected_state)
        return corrected_state

    def integrate(self, state: State):
        # Update forces of the current state before integration
        self.apply_forces(state)

        # Calculate intermediate state for predictor corrector scheme
        corrected_state = self.compute_intermediate_state(state)

        error = np.inf
        iteration = 0

        while (error > self.tolerance) and (iteration < self.max_iterations):
            corrected_state_new = self.compute_corrected_state(state, corrected_state)
            error = compute_phase_distance(corrected_state_new, corrected_state)
            corrected_state = corrected_state_new
            iteration += 1

        # Update the original state with the converged corrected state      
        state.position = corrected_state.position
        state.velocity = corrected_state.velocity
        state.force = corrected_state.force
        self.reset_forces(state)
# %%
