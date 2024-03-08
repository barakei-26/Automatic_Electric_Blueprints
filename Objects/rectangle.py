from Objects.coord import Coord
import comtypes
import array

class Rectangle:
    def __init__(self, corner_1, corner_2):
        if not(isinstance(corner_1,Coord)&isinstance(corner_2,Coord)):
            raise ValueError("TypeError: Arguments must be coordinates")
        else:
            delta_x, delta_y = corner_1.delta("x",corner_2), corner_1.delta("y",corner_2)
            corner_3 = Coord(corner_1.x, corner_1.y + delta_y)
            corner_4 = Coord(corner_1.x + delta_x, corner_1.y)
            self.corners = [corner_1, corner_2, corner_3, corner_4]
            self.order()

    def order(self):
        
        corners = self.corners
        corners[0:] = sorted(corners[0:], key=lambda c:c.y)
        corners[0:2] = sorted(corners [0:2], key=lambda c:c.x)
        corners[2:] = sorted(corners[2:], key=lambda c: c.x, reverse=True)
        corners.append(corners[0])
        self.corners = corners
     

    def get_points_array(self):
        corners =  self.corners
        points = []

        for corner in corners:
            points.append(corner.x)
            points.append(corner.y) 
        
        points = array.array('d', points)

        return points


