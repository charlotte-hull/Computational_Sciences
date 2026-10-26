import numpy as np
import matplotlib.pyplot as plt

def V_LJ(r_ij, sigma, epsilon):
    return 4*epsilon*((sigma/r_ij)**12-(sigma/r_ij)**6)

r_ij=np.linspace(0,3,1000)


sigma=np.linspace(0.25,1,4)
epsilon=np.linspace(0.25,1,4)
for i in range(len(sigma)):
    for j in range(len(epsilon)):
        V_LJ_values=V_LJ(r_ij, sigma[i], epsilon[j])
        label=rf'$\sigma$ ={sigma[i]}, $\epsilon$ ={epsilon[j]}'
        plt.plot(r_ij,V_LJ_values, label=label)
''''
sigma=0.5
epsilon=0.5
V_LJ_values=V_LJ(r_ij, sigma, epsilon)

print(V_LJ_values)
plt.plot(r_ij,V_LJ_values)
'''

plt.ylim(-2,7)
plt.legend(prop={'size': 8})
plt.grid(True)
plt.title('Lennard-Jones Potential against Distance')
plt.xlabel(r'$r_{ij}$')
plt.ylabel(r'$V_{LJ}(r_{ij})$')
plt.show()

