from Objects.coord import Coord
from Objects.circle import Circle
from Objects.rectangle import Rectangle
from connector import Connector
from draftsman import Draftsman



#start connection to Autocad
connection = Connector().connection

# get active document
doc = connection.ActiveDocument

# get model space from active document
model_space = doc.ModelSpace

#instantiate draftsman
draftsman = Draftsman(1)

#define object
object = Circle(Coord(0,0), 15)

#draw object
draftsman.draw(model_space, object)






