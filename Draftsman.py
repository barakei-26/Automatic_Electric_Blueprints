import comtypes.client
import Objects.circle 
import array
import numpy as np

class Draftsman:

    def __init__(self) -> None:
        pass

    def draw_line(self, line, model):
        line = model.AddLine(line.start_point, line.final_point)
        return line

    def draw_rectangle(self, rectangle, model):
        points = rectangle.get_points_array()
        rectangle = model.AddLightweightPolyline(points)
        return rectangle

    def draw_circle(self, circle, model):
        center = circle.center
        radius = np.float64(circle.radius)
        circle_array = array.array('d', [center.x, center.y,0])
        model.AddCircle(circle_array, radius)

    def draw_terminal(self, terminal, model):
        draftsman = self
        draftsman.draw_circle(terminal.circle, model)
        draftsman.draw_line(terminal.line, model)
        
    def draw_component(self, component, model):
        draftsman = self
        draftsman.draw_rectangle(component.box, model)
        terminals = component.terminals

        for terminal in terminals:
            draftsman.draw_terminal(terminal, model)
           
            

    
        
