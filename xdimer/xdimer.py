"""
xdimer package
"""
import math as m
import numpy as np

from .xdimer import semiclassical
from .emission import boltzmann_distribution

class xDimerModeError(Exception):
    """
    Raised if instance of dimer_system class is created using an unknown setup mode
    """

class dimer_system():
    """
    this class defines a dimer system with its attributes such as 
    * reduced mass
    * ground state ponetial parameters
    * excited state potential parameters
    * energetic displacement
    * 
    """
    def __init__(self, mass , gs , xs , q_xs, e_offset, setup_mode = 'vib_energy'):
        self.mass = mass
        self.mass_si = mass*1.66054e-27 
        self.q_xs = q_xs
        self.e_offset = e_offset
        self.setup_mode = setup_mode
        if self.setup_mode == 'vib_energy' or self.setup_mode == 'osc_const':
            print(f'Dimer system set up in {self.setup_mode} mode')
            self.gs_definition = gs
            self.xs_definition = xs
        else:
            raise xDimerModeError('Unknown setup mode: use \' vib_energy\' or \' osc_const\' ')
        
        '''global values for conversion calculations'''
        self.hJ = 1.0456e-34 # hbar in J/s
        self.eCharge = 1.6022e-19 # elementary charge 



    @property
    def xs_vib_energy(self):
        """excited state vibrational energy quantum in eV"""
        if self.setup_mode == 'vib_energy':
            return self.xs_definition
        else:
            return m.sqrt((2*self.xs_definition*(self.eCharge*1e20))/self.mass_si)*self.hJ/self.eCharge
    
    @property
    def gs_vib_energy(self):
        """ground state vibrational energy quantum in eV"""
        if self.setup_mode == 'vib_energy':
            return self.gs_definition
        else:
            return m.sqrt((2*self.gs_definition*(self.eCharge*1e20))/self.mass_si)*self.hJ/self.eCharge

    @property
    def xs_potential(self):
        """excited state oscillator constant in eV/angstrom**2"""
        if self.setup_mode == 'osc_const':
            return self.xs_definition
        else:
            return self.mass_si/(2*self.hJ**2)*(self.xs_definition*self.eCharge)**2*(1e-20/self.eCharge)

    @property
    def gs_potential(self):
        """excited state oscillator constant in eV/angstrom**2"""
        if self.setup_mode == 'osc_const':
            return self.gs_definition
        else:
            return self.mass_si/(2*self.hJ**2)*(self.gs_definition*self.eCharge)**2*(1e-20/self.eCharge)

    @property
    def xs_parameter(self):
        """oscillator parameter of excited state quantum-mechanical oscillator in 1/Angstrom**2 (alpha in manuscript)"""
        return (self.mass_si/self.hJ**2)*(self.xs_vib_energy*self.eCharge)*1e-20

    @property
    def gs_parameter(self):
        """oscillator parameter of excited state quantum-mechanical oscillator in 1/Angstrom**2 (alpha in manuscript)"""
        return (self.mass_si/self.hJ**2)*(self.gs_vib_energy*self.eCharge)*1e-20
    
        

def semiclassical_emission(E, temp, dimer):
    """
    Args:
        E (1-D ndarray): photon emission energy in eV
        temp (list/Float): either list of floats or float: List of temperature values or single temperature value in Kelvin
        dimer (instance dimer_system): dimer system as defined in dimer_system class

    Returns:
        dict/ndarray:   if temp is list, dictionary (key = temp): ndarrays containing emission spectra for respective temperature temp
                        if temp is float: ndarrays containing emission spectra for respective temperature temp
                        array structure: [8, size(E)]:  array[0]   = E # emission energy
                                                        array[i+1] = X-dimer emission spectrum from the i-th excited vibrational state (i in [0,...,5])
                                                        array[7]   = Semi-classical X-dimer emission spectrum at temperature "temp" considering the first six vibrational levels of the excited state oscillator
    """
    if type(temp) is list:
        list_flag = True
    else:
        temp = [temp]
        list_flag = False
    
    boltzmann_dist = boltzmann_distribution(temp)

    out = dict
    for T in temp:
        spectra = np.zeros((8,np.size(E)))
        spectra[0] = E
        spectra[1] = boltzmann_dist[T][1,0]*semiclassical.xdimer_sc_emission_0(E, dimer.gs_potential, dimer.xs_parameter, 0.5*dimer.xs_vib_energy, dimer.e_offset, dimer.q_xs)
        spectra[2] = boltzmann_dist[T][1,0]*semiclassical.xdimer_sc_emission_1(E, dimer.gs_potential, dimer.xs_parameter, 0.5*dimer.xs_vib_energy, dimer.e_offset, dimer.q_xs)
        spectra[3] = boltzmann_dist[T][1,0]*semiclassical.xdimer_sc_emission_2(E, dimer.gs_potential, dimer.xs_parameter, 0.5*dimer.xs_vib_energy, dimer.e_offset, dimer.q_xs)
        spectra[4] = boltzmann_dist[T][1,0]*semiclassical.xdimer_sc_emission_3(E, dimer.gs_potential, dimer.xs_parameter, 0.5*dimer.xs_vib_energy, dimer.e_offset, dimer.q_xs)
        spectra[5] = boltzmann_dist[T][1,0]*semiclassical.xdimer_sc_emission_4(E, dimer.gs_potential, dimer.xs_parameter, 0.5*dimer.xs_vib_energy, dimer.e_offset, dimer.q_xs)
        spectra[6] = boltzmann_dist[T][1,0]*semiclassical.xdimer_sc_emission_5(E, dimer.gs_potential, dimer.xs_parameter, 0.5*dimer.xs_vib_energy, dimer.e_offset, dimer.q_xs)
        spectra[7] = boltzmann_dist[T][1,0]*semiclassical.xdimer_sc_total_emission(E, dimer.gs_potential, dimer.xs_parameter, 0.5*dimer.xs_vib_energy, dimer.e_offset, dimer.q_xs, boltzmann_dist, T)

        out[T] = spectra
    
    if list_flag == True:
        return out
    else:
        return out[temp[0]]


if __name__ == '__main__':
    print('xdimer module called')
