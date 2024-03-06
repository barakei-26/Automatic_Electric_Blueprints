from Objects.coord import Coord
import comtypes
import array

class Rectangle:
    def __init__(self, corner_1, corner_2):
        if not(isinstance(corner_1,Coord)&isinstance(corner_2,Coord)):
            raise ValueError("TypeError: Arguments must be coordinates")
        else:
            delta_x, delta_y = corner_1.delta("x",corner_2), corner_1.delta("y",corner_2)
            corner_3 = Coord(self.corner_1.x, corner_1.y + delta_y)
            corner_4 = Coord(self.corner_1.x + delta_x, corner_1.y)
            self.corners = [corner_1, corner_2, corner_3, corner_4]

    def draw(self, model):

        points = []
        corner_1 = self.corner_1
        corner_2 = self.corner_2
        corner_3 = self.corner_3
        corner_4 = self.corner_4


        #This is the right way to do a polyline
        points = [2, 4, 4, 2, 6, 4]
        points = array.array('d',points)

        model.AddLightweightPolyline(points)

