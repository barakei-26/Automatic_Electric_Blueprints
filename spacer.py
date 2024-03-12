from Objects.coord import Coord

class Spacer:

    def __init__(self) -> None:
      
        self.is_first_component = True
        pass

    def assign_available_place(self, number_of_terminals):
        if self.is_first_component == True:

            left_down_corner = Coord(0,0)
            self.last_left_down_corner = left_down_corner
            self.last_box_height = 2*5*1.5*number_of_terminals
            self.is_first_component = False

        else:

            left_down_corner = Coord(0, self.last_left_down_corner.y + self.last_box_height + 5) 
            self.last_left_down_corner = left_down_corner
            self.last_box_height = 2*5*1.5*number_of_terminals


        return left_down_corner


