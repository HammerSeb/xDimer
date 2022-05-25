import math as m
import numpy as np

def boltzmann_distribution(Temp_list, vib_zero_point_energy, no_of_states= 50):
    """
    Generates a Boltzmann probability distribution for a quantum-mechanical harmonic oscillator with zero point energy "vib_zero_point_energy"

    Args:
        Temp_list (list of Floates): list of temperature values in Kelvin 
        vib_zero_point_energy (_type_): vibrational zero point energy in eV
        No_of_states (int, optional): number of simulated excited states for canocial partion sum. Defaults to 50.

    Returns:
        dictionary: key (Float): entries of Temp_list; 
                    values (ndarray): (2 x no_of_states); [0]: vibrational level, [1]: corresponding occupation probability
    """

    kb = 8.6173e-5   
    P = dict()
    for T in Temp_list:
        Z=0
        for n in range(no_of_states):
            Z += m.exp(-n*2*vib_zero_point_energy/(kb*T)) 
        N = list()
        p = list()
        for n in range(no_of_states):
            N.append(n)
            p.append(m.exp(-n*2*vib_zero_point_energy/(kb*T))/Z)
        P[T] = np.vstack((N,p))
    return P

def gauss(x, A, w, xc):
    """
    gauss function as line shape function
    Args:
        x (ndarray): x-values
        A (Float): area under the curve
        w (Float): standard deviation
        xc (Float): x center

    Returns:
       nadarry: function values at x-values
    """
    return A/m.sqrt(2*m.pi*w**2)*np.exp(-(x-xc)**2/(2*w**2))
