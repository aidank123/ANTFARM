import Globals as gl
import math

#IMPORT GLOBALS INTO EVERY CLASS

#creating globals object and calling each method
g = gl.Globals()
NUMBER_OF_ANTS = g.get_number_of_ants()
MAP_HEIGHT = g.get_height()
MAP_WIDTH = g.get_width()
HIVE_LOCATIONS = g.get_hive_locations()
FOOD_LOCATIONS = g.get_food_locations()

class Functions:
    
    def distance_squared(self, curr_x, curr_y, dest_x, dest_y):
        
        distance = 0
        distance = math.sqrt((abs(curr_x - dest_x) ** 2) + (abs(curr_y - dest_y) ** 2))
        return distance
        
    