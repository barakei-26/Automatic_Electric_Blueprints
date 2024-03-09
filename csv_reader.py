import pandas as pd
from Objects.component import Component


doc = pd.read_csv("terminals.csv")

terminals = doc['number of terminals']

print(terminals)



class Csv_reader:
   
   def __init__(self, path):
        self.doc = pd.read_csv(path)
   
   def get_component_list(self):
        
        list_of_terminals_numbers = self.doc['number of terminals']
        components = []

        for number_of_terminals in list_of_terminals_numbers:
            components.append(Component(number_of_terminals))

        return components

    