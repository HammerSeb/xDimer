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

## 2.Introduction

This package enables the quick simulation of emission spectra from Franck-Condon vibronic transitions between the vibrational levels of two harmonic oscillators with different potential strength at different temperatures. For this purpose, it provides two ways to simulate the emission, a semi-classical one for which the final state harmonic oscillator is treated as a continous function and a full quantum-mechanical approach, for which the individual Franck-Condon factors are calculated numerically. A short introduction of the underlying physical model as well as some basic defintions are given [below](#21-basic-defintions) please refere to the [related publication](#citation) for an in detail description of the physical model and the mathematical definition.

### 2.1 Model and defintions

The emission spectra are modeled as Franck-Condon transition between two displaced harmonic oscillators. They are characterized by their **reduced mass** $\mu$ and their potential curve
$\begin{equation*}
R(q) = R q^2
\end{equation*}$
with $q$ as the spatial generalized coordinate and the
> **oscillator constant** $R$.

which is related to the 

> **vibrational energy quantum** $E_{vib}$

and the 

> **oscilator parameter** $\alpha$

via the reduced mass as

$\begin{equation*}
R = \frac{\mu}{\hbar^2}E_{vib}^2 
\end{equation*}$

and 

$\begin{equation*}
\alpha = \frac{\mu}{\hbar^2}E_{vib} .
\end{equation*}$

The oscillators are displaces in energy by the
> **energetic offset** $D_e$

and along the generalized spatial coordinate by the
> **spatial displacement** $q_e$

each with respect to the vertex of the ground state parabola. 

Variable names are declare throughtout the package as follows: 

> `gs_potential` : ground state oscillator constant
>
> `xs_potential` : excited state oscillator constant
>
> `gs_vib_energy` : ground state vibrational energy quantum
>
> `xs_vib_energy` : excited state vibrational energy quantum
>
> `gs_parameter` : ground state oscillator parameter
>
> `xs_parameter` : excited state oscillator parameter
>
> `q_xs` : spatial displacement along generalized coordinate
>
> `e_offset` : energetic offset of the oscillators

For the simulation quantummechanical emission the energetic broadening of the underlying lineshape function is declared as
> `energetic_broadening`

### 2.2 Basic functionality

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
In the default `setup_mode` the parameters `gs` and `xs` define the ground state (gs) and excited state (xs) vibrational energy quantum (in eV). The parameters `q_xs` and `e_offset` are the spatial displacement $q_e$ (in Angstrom) and energetic offset $D_e$ (in eV). The `mass` parameter is the reduced mass $\mu$ of the dimer system in atomic units. Hence, 
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
>**For a list temperature values `temp=[T1, T2, T3, ...]`** 
>`emission` is a dictionary with keys T1, T2, T3, ... . Each entry contains an array for a single temperature value as described above. 

The quantummechanical emission is calculated by 
```python
emission = xdimer.xdimer.quantummechanical_emission(E, temp, dimer)
```
where `E` is of `ndarray`-type and defines the energy-axis over which the energy is calculated. The temperatures for which the spectra are calcualted are given by `temp` either as a `list` of several temperatures or a single temperature value as a `float`. The `dimer` is an instance of `dimer_system` (`dimer` can also be a `list`, see [API reference](#quantummechanicalemission)). The function [`quantummechanical_emission`](#quantummechanicalemission) returns pairs of array like return values 
```python
[spectra_full, spectra_stick] 
```
either as entrys in a dictonary keyed by multiple temperature values given in `temp`, or a single array pair if only one temperature value was given. If n vibrational levels of the excited state (0, ..., n-1) are simulated, t

**`spectra_stick`** is a list of `ndarrays` of length n. Each entry i contains the transition energies and intensities of all transitions from the i-th vibrational level of the excited state to the manifold of simulated ground state levels (default is 90). The relation between emission energy and tranisition intensity is referred to as stick spectrum of the i-th vibrational level.

> **The stick spectrum** of the i-th vibrational level is given as
>
>`spectrum_stick[i][0]` quantum number k of the vibrational level of the respective final state
>
>`spectrum_stick[i][1]` photon energy of the $\ket{i} \rightarrow \ket{k}$ transition
>
>`spectrum_stick[i][2]` Franck-Condon factor $|\braket{k|i}|^2$ transition weighted with a respective Boltzmann factor

**`spectra_full`** is a `ndarray` contains the convolution of the stick spectra with a gaussian line shape function of energetic broadening w (specified as an optional parameter when creating a [`dimer_system'](#dimersystem) instance) resulting in smooth emission spectra. 

>**The smooth emission spectra** are returned as
>
>`spectra_full[0]`: input variable `E` as energy axis
>
>`spectra_full[i]`: from i = 1 to the last simulated vibrational level n. The emission spectrum of the i-th vibrational level of the excited state as the sum of gaussian line shapes for each transition specified in `spectra_stick[i]`.
>
>`spectra_full[n+1]`: total emission spectrum as sum over all emissions from the simulated ;eve;s vibrational levels of the excited state

The **default settings** of the function simulate the **first five vibrational levels** of the excited states.

### 2.3 Fitting emission data

To use the emission functions to fit a luminescence data_set the `dimer` input can be given as a `list` containing the variables for an optimization procedure.

For `semiclassical_emission` the list needs to be of the following form:
```python
[gs_potential, xs_parameter, e_offset, q_xs, mass]
```

For `quantummechanical_emission` the list needs to be of the following form:
```python
[gs_parameter, xs_parameter, e_offset, q_xs, energetic_broadening, mass]
```

### 2.4 Examples

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