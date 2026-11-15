# %%
import numpy as np
import matplotlib.pyplot as plt

from compsci.data import State, Trajectory
from compsci.interaction import apply_harmonic_oscillator_forces_to_particles
from compsci.integration import Explicit_euler, Heuns_method, Runge_kutta, Implicit_euler, Integrator_explicit
from compsci.util import compute_phase_distance
# %%
class AnalyticalIntegrator_harmonicOscillator(Integrator_explicit):
    def integrate(self, state: State):
        state.position += state.velocity * self.time_step
        state.velocity -= state.position * self.time_step
# %%
class Config():
    def __init__(self):
        self.positions = np.array([[0.0]])
        self.velocities = np.array([[1.0]])
        self.time_step = 0.01
        self.total_steps = 10000

def run_simulation(config: Config):
    # initialize initial state
    state_ana = State(config.positions, config.velocities)
    state_ee = State(config.positions, config.velocities)
    state_heun = State(config.positions, config.velocities)
    state_rk = State(config.positions, config.velocities)
    state_ie = State(config.positions, config.velocities)

    # initialize integrator
    integrator_ana = AnalyticalIntegrator_harmonicOscillator(config.time_step, apply_harmonic_oscillator_forces_to_particles)
    integrator_ee = Explicit_euler(config.time_step, apply_harmonic_oscillator_forces_to_particles)
    integrator_heun = Heuns_method(config.time_step, apply_harmonic_oscillator_forces_to_particles)
    integrator_rk = Runge_kutta(config.time_step, apply_harmonic_oscillator_forces_to_particles)
    integrator_ie = Implicit_euler(config.time_step, apply_harmonic_oscillator_forces_to_particles)

    # initialize data container to store trajectory
    trajectory_ana = Trajectory(state_ana)
    trajectory_ee = Trajectory(state_ee)
    trajectory_heun = Trajectory(state_heun)
    trajectory_rk = Trajectory(state_rk)
    trajectory_ie = Trajectory(state_ie)

    # main simulation loop
    for step in range(config.total_steps):
        print("step =", step, end='\r')

        # integrate state
        integrator_ana.integrate(state_ana)
        integrator_ee.integrate(state_ee)
        integrator_heun.integrate(state_heun)
        integrator_rk.integrate(state_rk)
        integrator_ie.integrate(state_ie)

        # save current state to trajectory
        trajectory_ana.append(State(state_ana.position, state_ana.velocity, state_ana.force))
        trajectory_ee.append(State(state_ee.position, state_ee.velocity, state_ee.force))
        trajectory_heun.append(State(state_heun.position, state_heun.velocity, state_heun.force))
        trajectory_rk.append(State(state_rk.position, state_rk.velocity, state_rk.force))
        trajectory_ie.append(State(state_ie.position, state_ie.velocity, state_ie.force))

    return trajectory_ana, trajectory_ee, trajectory_heun, trajectory_rk, trajectory_ie
# %%
if __name__ == "__main__":
    config = Config()
    trajectory_ana, trajectory_ee, trajectory_heun, trajectory_rk, trajectory_ie = run_simulation(config)
    time_grid = np.arange(config.total_steps + 1) * config.time_step
# %%
    # create first figure with trajectory data
    fig, ax = plt.subplots(1, 3, figsize=(17, 5))

    # plot position vs time
    plt.sca(ax[0])
    plt.plot(time_grid, trajectory_ana.get_positions()[:, 0, 0], label="Analytical")
    plt.plot(time_grid, trajectory_ee.get_positions()[:, 0, 0], label="Explicit Euler")
    plt.plot(time_grid, trajectory_heun.get_positions()[:, 0, 0], label="Heun's Method")
    plt.plot(time_grid, trajectory_rk.get_positions()[:, 0, 0], label="Runge-Kutta")
    plt.plot(time_grid, trajectory_ie.get_positions()[:, 0, 0], label="Implicit Euler")
    plt.xlabel(r'Time in $\tau$')
    plt.ylabel(r'Position in $\sigma$')
    plt.legend()

    # plot velocity vs time
    plt.sca(ax[1])
    plt.plot(time_grid, trajectory_ana.get_velocities()[:, 0, 0], label="Analytical")
    plt.plot(time_grid, trajectory_ee.get_velocities()[:, 0, 0], label="Explicit Euler")
    plt.plot(time_grid, trajectory_heun.get_velocities()[:, 0, 0], label="Heun's Method")
    plt.plot(time_grid, trajectory_rk.get_velocities()[:, 0, 0], label="Runge-Kutta")
    plt.plot(time_grid, trajectory_ie.get_velocities()[:, 0, 0], label="Implicit Euler")
    plt.xlabel(r'Time in $\tau$')
    plt.ylabel(r'Velocity in $\sigma / \tau$')
    plt.legend()

    # plot phase space trajectories
    plt.sca(ax[2])
    plt.plot(trajectory_ana.get_positions()[:, 0, 0], trajectory_ana.get_velocities()[:, 0, 0], label="Analytical")
    plt.plot(trajectory_ee.get_positions()[:, 0, 0], trajectory_ee.get_velocities()[:, 0, 0], label="Explicit Euler")
    plt.plot(trajectory_heun.get_positions()[:, 0, 0], trajectory_heun.get_velocities()[:, 0, 0], label="Heun's Method")
    plt.plot(trajectory_rk.get_positions()[:, 0, 0], trajectory_rk.get_velocities()[:, 0, 0], label="Runge-Kutta")
    plt.plot(trajectory_ie.get_positions()[:, 0, 0], trajectory_ie.get_velocities()[:, 0, 0], label="Implicit Euler")
    plt.xlabel(r'Position in $\sigma$')
    plt.ylabel(r'Velocity in $\sigma / \tau$')
    plt.legend()

    plt.show()
# %%