from Objects.circle import Circle
from Objects.coord import Coord
from Objects.line import Line
from draftsman import Draftsman
import numpy as np

class Terminal:
    def __init__(self, center, number):
        angle = np.radians(45)
        radius = 5 
        self.name = number
        self.circle = Circle(center, radius)
        self.line = self.define_line(radius, angle)

    def define_line(self, radius, angle):
        circle = self.circle
        delta_x = radius*np.cos(angle)
        delta_y = radius*np.sin(angle)
        start_point = Coord(circle.center.x - delta_x, circle.center.y - delta_y)
        final_point = Coord(circle.center.x + delta_x, circle.center.y + delta_y)
        line = Line(start_point, final_point)
        return line
    
  


 

         