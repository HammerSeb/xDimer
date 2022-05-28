from gettext import find
from setuptools import setup, find_packages

setup(name='XDimer',
      version='0.8.2',
      description='Simulation of multi-molecular emission spectra dominated by intermolecular vibrations ',
      long_description=open('README.md').read(),
      license= 'MIT',
      author='Sebastian Hammer',
      author_email='sebastian.hammer@mail.mcgill.ca',
      url='https://github.com/HammerSeb/ITC503Control',
      packages= find_packages(),
      install_requires=['numpy', 'scipy', 'matplotlib'],
      include_package_data = True
     )
