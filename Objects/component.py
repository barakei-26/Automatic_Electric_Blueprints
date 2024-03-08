from Objects.coord import Coord
from draftsman import Draftsman
from Objects.rectangle import Rectangle
from Objects.terminal import Terminal

class Component:
    
    def __init__(self,number_of_terminals):

        self.number_of_terminals = number_of_terminals
        self.box = self.create_box()
        self.terminals = self.create_terminals()


    def create_box(self):
        box_hihgt = 2*5*(1.5*self.number_of_terminals)
        box = Rectangle(Coord(0,0), Coord(120,box_hihgt))
        return box

    def create_terminals(self):
        radius = 5
        terminals = []
        box_corners = self.box.corners
        upper_right_corner = box_corners[2]
        first_center = Coord(upper_right_corner.x - 2*radius, upper_right_corner.y-2*radius)
        center = first_center

        for n in range(1, self.number_of_terminals+1):
            center = Coord(first_center.x,first_center.y - 2.5*radius*(n-1))
            terminal = Terminal(center, n)
            terminals.append(terminal)

        return terminals
    
    

            