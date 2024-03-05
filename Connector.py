import comtypes.client  

class Connector:
    def __init__(self):

        self.connection = comtypes.client.GetActiveObject("AutoCAD.Application")

    def connec_to_open_doc(self):

        acad_connection = self.connection

        return acad_connection

