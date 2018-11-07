def calculate_force(mass,acceleration):
    if type(mass)==float and type(acceleration)==float:
        force = mass * acceleration
        return force 
    else:
        return (None)
  
from scipy.constants import c
def find_and_print_energy(mass):
    if type(mass) == float:
        energy = mass * pow(c,2)
        return energy
    else:
        return (None)
find_and_print_energy(0.009)

def find_and_print_energy(mass):
    if type(mass) == float:
        energy = mass * pow(c,2)
        print("The energy equivalent of mass",mass,"is",energy)
        return energy
    else:
        return (None)
