from Objects.coord import Coord
from Objects.circle import Circle
from Objects.rectangle import Rectangle
from Objects.terminal import Terminal
from Objects.component import Component
from connector import Connector
from draftsman import Draftsman



#start connection to Autocad
connection = Connector().connection

# get active document
doc = connection.ActiveDocument

# get model space from active document
model_space = doc.ModelSpace

#instantiate draftsman
draftsman = Draftsman()

#define object
object = Component(3)

#draw object
draftsman.draw_component(object, model_space)






