'''
==============
Exercise 2.1.1
==============

Implement the Lennard-Jones potential with the distance, the LJ-
length and the LJ-energy as arguments and plot it against the distance using 
matplotlib.

How do the two LJ parameters change the graph and what physical significance can you
attribute to them?

In what range of potentials and distances can you see the interesting features of the function for
a given pair of the two parameters?
'''
# %%
import numpy as np
import matplotlib.pyplot as plt
# %%
def calc_lennard_jones_potential(distance: float, lj_length: float, lj_energy: float) -> float:
    return 4 * lj_energy * ((lj_length / distance)**12 - (lj_length / distance)**6)
# %%
if __name__ == "__main__":
    distance_grid = np.linspace(0.1, 5.0, 10000)
    lj_lengths = [0.5, 1.0, 1.5]
    lj_energies = [0.5, 1.0, 1.5]

    for lj_length in lj_lengths:
        for lj_energy in lj_energies:
            potential = [calc_lennard_jones_potential(d, lj_length, lj_energy) for d in distance_grid]
            label = rf"$\sigma={lj_length}$, $\epsilon={lj_energy}$"
            plt.plot(distance_grid, potential, label=label)

    plt.xlabel(r"$r_{i, j}$")
    plt.ylabel(r"$v_{\mathrm{LJ}}(r_{i, j})$")
    plt.title("Lennard-Jones Potential vs Distance")
    plt.grid(True)
    plt.ylim(-2.0, 10.0)
    plt.legend()
    plt.show()
# %%
