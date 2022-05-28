# xDimers

Pyhton package for simulating multi-molecular emission spectra dominated by a single effective intermolecular vibrational mode. This package accompanies the publication in ...

## Table of contents
1. [Installation](#1-installation)
2. [Basic introduction](#2-basic-introduction)
3. [API reference guide](#3-api-reference-guide)
4. [License and citation](#4-license-and-citation)

## 1. Installation

The latest development version is available on GitHub. To install use:
```
python -m pip install git+https://github.com/HammerSeb/xDimer.git
```

***PyPi and Conda version missing***

## 2. Basic introduction

This package enables the quick simulation of emission spectra from Franck-Condon vibronic transitions between the vibrational levels of two harmonic oscillators with different potential strength at different temperatures. For this purpose, it provides two ways to simulate the emission, a semi-classical one for which the final state harmonic oscillator is treated as a continous function and a full quantum-mechanical approach, for which the individual Franck-Condon factors are calculated numerically. For further details on the underlying model please refer to ***add publication reference here***.

### 2.1 Basic functionality

The package consists of three main parts contained in the [`xdimer`](#31-xdimer) module which can be loaded by

```python
import xdimer
```

This module contains the class [`dimer_system`](#dimersystem) which stores the key parameters fully defining a dimer system. The functions [`semiclassical_emission`](#semiclassicalemission) and [`quantummechanical_emission`](#quantummechanicalemission) take instances of the [`dimer_system`](#dimersystem) class as an input and return the respective emission spectra. 

#### Set up a dimer system

To create a dimer system use
```python
dimer = xdimer.dimer_system(mass, gs, xs, q_xs, e_offset)
```
In the default `setup_mode` the parameters `gs` and `xs` define the ground state (gs) and excited state (xs) vibrational energy quantum (in eV). The parameters `q_xs` and `e_offset` are the spatial (in Angstrom) and energetic (in eV) displacement of the excited state harmonic pontential in realtion to the ground state potential's vertex. The `mass` parameter is the reduced mass of the dimer system in atomic units. Hence, 
```python
dimer = xdimer.dimer_system(423, 0.02, 0.025, 0.1, 1.5)
```
defines a dimer system with reduced mass **423 u**, ground and excited state vibrational energy quantums of **20 meV** and **25 meV**, respecitvely, an excited state spatial displacement of **0.1 Angstrom** and an energetic offset of **1.5 eV**. 

#### Calculating emission spectra

Emission spectra can be calculated in semi-classical or quantummechanical manner. To calculate semiclassical emission spectra use
```python
spectra = xdimer.semiclassical_emission(E, temp, dimer)
```
where `E` is of `ndarray`-type and defines the energy-axis over which the energy is calculated. The temperatures for which the spectra are calcualted are given by `temp` either as a `list` of several temperatures or a single temperature value as a `float`. The `dimer` is an instance of `dimer_system` (`dimer` can also be a `list`, see [API reference](#semiclassicalemission)). The function [`semiclassical_emission`](#semiclassicalemission) returns either a `dictonary` if the temperature input was given as a list of several values, or a `ndarray` if only one temperature value was provided. The return variable is compased as follows

>**For a single temperature value:**
>`emission` is an array of the form
>
>`emission[0]` input variable `E` as energy axis
>
>`emission[i]` from i = 1,...,6. The emission spectrum of the i-th vibrational level of the excited state
>
>`emission[7]` total emission spectrum as sum over all emissions from the first 6 vibrational levels of the excited state
>
>**For a list temperature values `temp=\[T1, T2, T3, ...\]`** 
>`emission` is a dictionary with keys T1, T2, T3, ... . Each entry contains an array for a single temperature value as described above. 

The quantummechanical emission is calculated by 
```python
[spectra_full, spectra_stick]  = xdimer.xdimer.quantummechanical_emission(E, temp, dimer)
```
### 2.2 Examples

Two examples are provided showing how to simulate spectra and use the provided functions to fit a set of temperature dependent luminescence data. 

They can be called by

```
python -m xdimer.examples.simulating_emission
```

and 

```
python -m xdimer.examples.fitting_emission_data
```

**simulating_emission** simulates a semiclassical and quantum-mechanical emission spectrum for a temperature specified by console input when running the module. The individual vibrational contributions from the excited state are unraveled and depicted colorcoded with the main emission spectrum. 

**fitting_emission_spectra** simulates a data set of emission data using `xdimer.quantummechanical_emission` for four different temperatures. It then performs a fit to the whole data set, including all temperatures. The fit does take a while (approx 90 seconds).    
## 3. API reference guide

### 3.1 xdimer 

#### dimer_system

#### semiclassical_emission

#### quantummechanical_emission


## 4. License and citation

### License

### Citation