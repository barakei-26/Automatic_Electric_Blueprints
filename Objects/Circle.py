from Objects.coord import Coord
import array
import numpy as np

class Circle:

    def __init__(self, center, radius):
        if not isinstance(center, Coord):
           raise ValueError("center must be a coordinate")

        else:
            self.center = center
            self.radius = radius

    


    


