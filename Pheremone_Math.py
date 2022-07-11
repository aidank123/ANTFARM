#this class will be used to build the math which will update the pheremone map
import numpy as np
import Globals as gl


#IMPORT GLOBALS INTO EVERY CLASS

#creating globals object and calling each method
g = gl.Globals()
NUMBER_OF_ANTS = g.get_number_of_ants()
MAP_HEIGHT = g.get_height()
MAP_WIDTH = g.get_width()
HIVE_LOCATIONS = g.get_hive_locations()
FOOD_LOCATIONS = g.get_food_locations()


class Pheremone_Math:
    
    def __init__(self):
        self.pheremone_decay_rate = .25 #placeholder values
        self.pheremone_amount = .1
        
    def pheremone_decay(self):
        
        
    def add_pheremone(self):
        
        
    
        
    