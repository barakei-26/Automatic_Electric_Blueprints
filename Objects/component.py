from Objects.coord import Coord
from draftsman import Draftsman
from Objects.rectangle import Rectangle
from Objects.terminal import Terminal
from spacer import Spacer

class Component:

    def __init__(self,number_of_terminals,spacer):

        self.number_of_terminals = number_of_terminals
        
        left_down_corner = spacer.assign_available_place(number_of_terminals)
        self.box = self.create_box(left_down_corner)
        self.terminals = self.create_terminals()

    def create_box(self, left_down_corner):
        box_heihgt = 2*5*1.5*self.number_of_terminals

        print(left_down_corner.y)
        box = Rectangle(left_down_corner, Coord(120,left_down_corner.y + box_heihgt))
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

        
    
    
    

            