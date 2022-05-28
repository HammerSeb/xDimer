# xDimers

Pyhton package for simulating multi-molecular emission spectra dominated by a single effective intermolecular vibrational mode. This package accompanies the publication in ...

## Table of contents
1. [Installation](#1-installation)
2. [Basic introduction](#2-basic-introduction)
3. [API reference guide](#3-api-reference-guide)
4. [License and citation](#4-license-and-citation)

## 1. Installation

The latest development version is available on GitHub. To install use:

`python -m pip install git+https://github.com/HammerSeb/xDimer.git`

***PyPi and Conda version missing***

## 2. Basic introduction

This package enables the quick simulation of emission spectra from Franck-Condon vibronic transitions between the vibrational levels of two harmonic oscillators with different potential strength at different temperatures. For this purpose, it provides two ways to simulate the emission, a semi-classical one for which the final state harmonic oscillator is treated as a continous function and a full quantum-mechanical approach, for which the individual Franck-Condon factors are calculated numerically. For further details on the underlying model please refer to ***add publication reference here***.

### Basic functionality

The package should be imported 

### Examples

Two examples are provided showing how to simulate spectra and use the provided functions to fit a set of temperature dependent luminescence data. 

They can be called by

`python -m xdimer.examples.simulating_emission`

and 

`python -m xdimer.examples.fitting_emission_data`

**simulating_emission** simulates a semiclassical and quantum-mechanical emission spectrum for a temperature specified by console input when running the module. The individual vibrational contributions from the excited state are unraveled and depicted colorcoded with the main emission spectrum. 

**fitting_emission_spectra** ...
## 3. API reference guide

## 4. License and citation

### License

### Citation