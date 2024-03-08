class Terminal:
    def __init__(self):
        self._name = input("ingrese el nombre de la terminal")
    
    @property
    def name(self):
        return self._name
    
    @name.setter 
    def name(self, new_name):
        if new_name.strip():
            self._name = new_name