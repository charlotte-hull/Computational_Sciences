'''
==============
Exercise 3.1.3
==============
Get together in groups of $3$ people. Then, as a group, select
a unique time integrator out of the ones given in chapter 4.2
p. 19 of the ODE/PDE lecture notes. Implement that time integrator 
going through the entire development cycle.
'''
# %%
import numpy as np

from compsci.exercise_3.interaction import apply_lennard_jones_forces_to_particles
from compsci.exercise_3.data import State
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
# %%
class Explicit_euler(Integrator_explicit):
    # TODO: implement the Explicit Euler integration method
# %%
class Heuns_method(Integrator_explicit):
    # TODO: implement Heun's method for integration
# %%
class Runge_kutta(Integrator_explicit):
    # TODO: implement the Runge-Kutta integration method
# %%
class Implicit_euler(Integrator_implicit):
    # TODO: implement the Implicit Euler integration method