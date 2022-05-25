import sys
from .. import xdimer
from .. import semiclassical as sc
import numpy as np
from matplotlib import pyplot as plt

if __name__ == '__main__':
    print('xDimer example - enter temperature in Kelvin:')
    temperature = float(input()) #temperature user input

    # Set up dimer system with reduced mass 0.5*577.916u (ZnPc dimer), ground state vibrational energy 22 meV, excited state displaced by 0.1 Angstrom, with vibrational energy 26 meV and an energetic offset of 1.5 eV
    dimer = xdimer.dimer_system(577.916/2, .022, .030, 0.1, 1.55)
    
    # generate energy axis
    energy_axis = np.linspace(1,1.8, num=500)

    ### Semi-classcial emission spectra

    # calculate singularity in emission spectrum which has lowest energy
    singularity = sc.excited_state_energy(0, 0.5*dimer.xs_vib_energy, dimer.e_offset)
    
    # generate semi-classical emission spectrum
    emission_spectrum = xdimer.semiclassical_emission(energy_axis, temperature, dimer)

    figure, ax = plt.subplots()
    colors_plot = ['blueviolet', 'skyblue', 'darkorange', 'forestgreen', 'red', 'aqua', 'fuchsia']
    max_plot = emission_spectrum[7].max() + 0.15*emission_spectrum[7].max()
    ax.set_xlim((1,1.8))
    ax.set_ylim((0,max_plot))
    ax.set_ylabel('Intensity [a.u.]')
    ax.set_xlabel('Energy [eV]')
    ax.set_title('Semi-classical')

    ax.vlines(singularity, ymin=0, ymax=max_plot, colors = 'black', linestyle = 'solid')
    ax.text(singularity+0.01,0.5*max_plot, 'singularity', rotation = 'vertical' )
    ax.plot(emission_spectrum[0], emission_spectrum[1], color = colors_plot[1], label = '0. vib.', linestyle = '--', linewidth = 2, zorder = 2)
    if temperature >= 100:
        ax.plot(emission_spectrum[0], emission_spectrum[2], color = colors_plot[2], label = '1. vib.', linestyle = '--', linewidth = 2, zorder = 3)
    if temperature >= 170:
        ax.plot(emission_spectrum[0], emission_spectrum[3], color = colors_plot[3], label = '2. vib.', linestyle = '--', linewidth = 2, zorder = 4)
    if temperature >= 240:
        ax.plot(emission_spectrum[0], emission_spectrum[4], color = colors_plot[4], label = '3. vib.', linestyle = '--', linewidth = 2, zorder = 5)
    if temperature >= 340:
        ax.plot(emission_spectrum[0], emission_spectrum[5], color = colors_plot[5], label = '4. vib.', linestyle = '--', linewidth = 2, zorder = 6)
    if temperature >= 400:
        ax.plot(emission_spectrum[0], emission_spectrum[6], color = colors_plot[6], label = '5. vib.', linestyle = '--', linewidth = 2, zorder = 7)
    ax.plot(emission_spectrum[0], emission_spectrum[7], color = colors_plot[0], label = 'full', linestyle = '-', linewidth = 3, zorder = 1)
    ax.legend(title = f'T = {temperature} K', loc = 'upper left')
    plt.show()
