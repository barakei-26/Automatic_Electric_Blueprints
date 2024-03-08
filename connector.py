import comtypes.client  

class Connector:
    def __init__(self):

        self._connection = comtypes.client.GetActiveObject("AutoCAD.Application")

    @property
    def connection(self):
        return self._connection


