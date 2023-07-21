#!/usr/bin/python

import inkscapeMadeEasy.inkscapeMadeEasy_Base as inkBase
import inkscapeMadeEasy.inkscapeMadeEasy_Draw as inkDraw
import inkscapeMadeEasy.inkscapeMadeEasy_Plot as inkPlot

class quantumCircuits(inkBase.inkscapeMadeEasy):
    def __init__(self) -> None:
        inkBase.inkscapeMadeEasy.__init__(self)
    
    def effect(self) -> None:
        pass

if __name__ == '__main__':
    circuit = quantumCircuits()
    circuit.run()
