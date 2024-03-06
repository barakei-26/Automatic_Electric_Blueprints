import array
class Coord:
    def __init__(self, x, y):
        if not (isinstance(x,(float,int)) and isinstance(y, (float, int))):
            raise ValueError("Los argumentos de esta función deben ser ")
        else:
            self.x = x
            self.y = y 

    def delta(self, x_or_y, second_coord):

        if x_or_y == "x":
            delta = second_coord.x-self.x
        elif x_or_y == "y":
            delta = second_coord.y-self.y

        return delta
        
    def acad_point(self):
        acad_point = array.array('d',[self.x, self.y])
        return acad_point
    