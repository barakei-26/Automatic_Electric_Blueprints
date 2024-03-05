import comtypes.client
import objects

class Draftsman:

    def __init__(self,id):
        self.id = id

    def draw(model, object):
        object.draw(model)
