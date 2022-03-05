"""
xdimer package
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
    def __init__(self, mass = None, gs_parameter = None, xs_parameter = None, displ = None, e_offset = None):
        self.mass = mass 
        self.gs_parameter = gs_parameter
        self.xs_parameter = xs_parameter
        self.displ = displ 
        self.e_offset = e_offset

    @property
    def xs_vib_energy(self):
        """returns vibrational energy of excited state from xs parameter"""
        pass

    @property
    def gs_vib_energy(self):
        """returns vibrational energy of ground state from xs parameter"""
        pass


if __name__ == '__main__':
    print('xdimer module called')
