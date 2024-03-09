from Objects.coord import Coord
from Objects.circle import Circle
from Objects.rectangle import Rectangle
from Objects.terminal import Terminal
from Objects.component import Component
from connector import Connector
from draftsman import Draftsman
from csv_reader import Csv_reader



#start connection to Autocad
connection = Connector().connection
doc = connection.ActiveDocument
model_space = doc.ModelSpace
draftsman = Draftsman()

#get the list of components from csv file
csv_reader = Csv_reader('terminals.csv')

components = csv_reader.get_component_list()

for component in components:
    draftsman.draw_component(component, model_space)







