from scipy.constants import Boltzmann, Avogadro, angstrom
import numpy as np
class LJ_Argon:
    sigma=3.405*angstrom
    epsilon=119.8*Boltzmann
    m=39.948*10**(-3)/Avogadro
    tau=sigma*np.sqrt(m/epsilon)


class simulated_units:
    n = 10**(-9) 
    p = 10**(-12)  
    d = 1/(1000*Avogadro)
    length=LJ_Argon.sigma/n
    energy=LJ_Argon.epsilon/(d*n**2/p**2)
    mass=LJ_Argon.m/d
    time=LJ_Argon.tau/p

class SI_units:
    length=LJ_Argon.sigma
    energy=LJ_Argon.epsilon
    mass=LJ_Argon.m
    time=LJ_Argon.tau

print(simulated_units.length,simulated_units.energy,simulated_units.mass,simulated_units.time)
print(SI_units.length,SI_units.energy,SI_units.mass,SI_units.time)

#not very useful for other systems other than argon, not repeatable