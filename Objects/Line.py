from coord import Coord
class Line:
    def __init__(self, start_point, final_point):

        if not(isinstance(final_point,Coord)&isinstance(start_point,Coord)):
            raise ValueError("Los argumentos de esta función deben ser pares coordenados")
        else:
            self.start_point = start_point.acad_point()            
            self.final_point = final_point.acad_point()        
        
    def draw(self, model):
        line = model.AddLine(self.start_point, self.final_point)
        return line