import array

class Line:
    
    def __init__(self, start_point, final_point):
        self.start_point = start_point
        self.final_point = final_point
        
    def draw(self, model):

        start_point = array.array('d', self.start_point)

        final_point = array.array('d', self.final_point)

        line = model.AddLine(start_point, final_point)

        return line


class Rectangle:
    def __init__(self, corner_1, corner_2):
        
        self.corner_1 = corner_1

        self.corner_2 = corner_2

    def draw(self, model):

        

        point_1 = array.array("d", self.corner_1)

        point_3 = array.array("d", self.corner_2)

        


