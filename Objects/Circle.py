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

    def draw(self, model):
        center = self.center

        radius = np.float64(self.radius)

        circle_array = array.array('d', [center.x, center.y,0])

        model.AddCircle(circle_array, radius)
        


    


