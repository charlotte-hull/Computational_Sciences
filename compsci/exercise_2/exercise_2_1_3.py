# %%
from scipy.constants import Boltzmann, Avogadro, angstrom
import numpy as np
# %%
class Unit_System():
    length: float
    mass: float
    energy: float
#%%
class SI(Unit_System):
    length = 1 # m
    mass = 1 # kg
    energy = 1 # J
# %%
class LJ_Argon(Unit_System):
    sigma = 3.405 * angstrom # m
    atomic_mass = 39.948 * 10**(-3)/Avogadro # kg
    epsilon = 119.8 * Boltzmann       # J

    length = sigma 
    mass = atomic_mass
    energy = epsilon
# %%
class Simulation_Native(Unit_System):
    nanometer = 10**(-9) # m
    picoseconds = 10**(-12)  # s
    dalton = 10**(-3)/Avogadro # kg

    length = nanometer
    mass = dalton
    energy = dalton * nanometer**2/picoseconds**2 # J
# %%
class Conversions():
    "see https://matsci.org/t/some-confusions-about-units-lj/43138"
    def __init__(self, input_unit_system: type[Unit_System] = SI, target_unit_system: type[Unit_System] = SI):
        '''
        Default values are the SI unit system (-> 1.0 m, 1.0 J, 1.0 kg)
        '''
        # unit system in which the input is given
        self.length_input = input_unit_system.length 
        self.mass_input = input_unit_system.mass
        self.energy_input = input_unit_system.energy     
        
        # unit system in which the output is wanted
        self.length_target = target_unit_system.length
        self.mass_target = target_unit_system.mass
        self.energy_target = target_unit_system.energy

    def convert_length(self, length):
        return length * self.length_input/self.length_target
    
    def convert_mass(self, mass):
        return mass * self.mass_input/self.mass_target
    
    def convert_time(self, time):
        return time * (self.length_input/np.sqrt(self.energy_input/self.mass_input))/(self.length_target/np.sqrt(self.energy_target/self.mass_target))
    
    def convert_energy(self, energy):
        return energy * self.energy_input/self.energy_target
# %%
if __name__ == "__main__":
    convert_argon_to_sim = Conversions(input_unit_system=LJ_Argon, target_unit_system=Simulation_Native)
    length_in_sim = convert_argon_to_sim.convert_length(1.0) # 1 sigma in sim units
    print(f"1 sigma in sim units: {length_in_sim}")
    energy_in_sim = convert_argon_to_sim.convert_energy(1.0) # 1 epsilon in sim units
    print(f"1 epsilon in sim units: {energy_in_sim}")
    time_in_sim = convert_argon_to_sim.convert_time(1.0) # 1 tau in sim units
    print(f"1 tau in sim units: {time_in_sim}")
    mass_in_sim = convert_argon_to_sim.convert_mass(1.0) # 1 atomic mass unit in sim units
    print(f"1 atomic mass unit in sim units: {mass_in_sim}")

    convert_argon_to_si = Conversions(input_unit_system=LJ_Argon, target_unit_system=SI)
    length_in_si = convert_argon_to_si.convert_length(1.0) # 1 sigma in SI units
    print(f"1 sigma in SI units: {length_in_si}")
    energy_in_si = convert_argon_to_si.convert_energy(1.0) # 1 epsilon in SI units
    print(f"1 epsilon in SI units: {energy_in_si}")
    time_in_si = convert_argon_to_si.convert_time(1.0) # 1 tau in SI units
    print(f"1 tau in SI units: {time_in_si}")
    mass_in_si = convert_argon_to_si.convert_mass(1.0) # 1 atomic mass unit in SI units
    print(f"1 atomic mass unit in SI units: {mass_in_si}")
# %%
