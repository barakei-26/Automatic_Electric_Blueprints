from Objects.coord import Coord
from Objects.Rectangle import Rectangle
from Connector import Connector
import sys

connection = Connector().connection

doc = connection.ActiveDocument

model_space = doc.ModelSpace

rectangle = Rectangle(Coord(0,0), Coord(6,10))

rectangle.draw(model_space)






