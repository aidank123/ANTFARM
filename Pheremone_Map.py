import numpy as np

pheremone_map = []

class Pheremone_Map:
    def __init__(self):
        self.map = map
        
    def add_location(self,location):
        pheremone_map.append(location)
        
    def get_map(self):
        return pheremone_map