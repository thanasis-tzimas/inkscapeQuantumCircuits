#!/usr/bin/python

import inkscapeMadeEasy.inkscapeMadeEasy_Base as inkBase

class QuantumCircuits(inkBase.inkscapeMadeEasy):
    """
    The base class of the extension.

    This class inherits methods from inkBase that itself inherits from inkex.
    Therefore, this class has access to all the member functions and methods of 
    both inkBase and inkex.
    """

    def __init__(self) -> None:
        """__init__() -> None
        Initialization of the class.

        In here, the argument parsing happens (plus some rudimentary initialization).
        """
        inkBase.inkscapeMadeEasy.__init__(self)
        pass

    def effect(self) -> None:
        """effect() -> None:
        Effect function that Inkscape directly calls.

        As per documentation, this is the only function that Inkscape directly calls.
        This means that it has to be implemented to render with Inkscape. This function 
        can also be refered as the 'main' function of the extension.
        """
        pass

if __name__ == "__main__":
    # This extension can also run independently (?)
    circuit = QuantumCircuits()
    circuit.run()
