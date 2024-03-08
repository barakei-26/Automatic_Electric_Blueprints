from Objects.coord import Coord
from Objects.circle import Circle
from Objects.rectangle import Rectangle
from Objects.terminal import Terminal

class Component:

    
    def __init__(self,number_of_terminals):

        self.number_of_terminals = number_of_terminals
        self.names = self.define_terminal_names()

    def define_terminal_names(self):

        terminal_names = []

        for terminal in range(self.number_of_terminals):
            terminal = Terminal()
            terminal_names.append(terminal.name)

    def draw(self, model):
        box = Rectangle(Coord(0,0), Coord(12,5))

        for terminal in range(self.number_of_terminals):
            circle = Circle(Coord(0,0),5)

    
