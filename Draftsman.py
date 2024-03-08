import comtypes.client
import Objects.circle 

class Draftsman:

    def __init__(self,id):
        self.id = id

    def draw(self, model, object):
        object.draw(model)
