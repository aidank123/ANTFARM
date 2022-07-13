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
ANT_SMELL_RADIUS = g.get_ant_smell_radius()

class Functions:
    
    def distance_squared(self, curr_x, curr_y, dest_x, dest_y):
        
        distance = 0
        distance = math.sqrt((abs(curr_x - dest_x) ** 2) + (abs(curr_y - dest_y) ** 2))
        return distance
        
    
    def surrounding_squares(self, ant_location): #all squares within the ants smelling distance
        x = ant_location[0]
        y = ant_location[1]
        
        
        surrounding_squares = [[x-1,y-1],[x,y-1],[x+1,y-1],[x+1,y],[x+1,y+1],[x,y+1],[x-1,y+1],[x-1,y]]
        
#         for a in range(ANT_SMELL_RADIUS): 
#             for b in range(ANT_SMELL_RADIUS):
#             surrounding_squares.add(([x-a,y-a],[x,y-a],[x+a,y-a],[x+a,y],[x+a,y+a],[x,y+a],[x-a,y+a],[x-a,y]))
            
            
            
        return surrounding_squares