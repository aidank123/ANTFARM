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

total_food_collected = 0

class Functions:
        
    def distance_squared(self, curr_x, curr_y, dest_x, dest_y):
        
        distance = 0
        distance = math.sqrt((abs(curr_x - dest_x) ** 2) + (abs(curr_y - dest_y) ** 2))
        return distance
    
        
    def adjacent_squares(self, ant_location): #all squares directly next to the ant
        x = ant_location[0]
        y = ant_location[1]
        
        adjacent_squares = [[x-1,y-1],[x,y-1],[x+1,y-1],[x+1,y],[x+1,y+1],[x,y+1],[x-1,y+1],[x-1,y]]
        return adjacent_squares
        
    def surrounding_squares(self, ant_location): #all squares within the ants smelling distance
        x = ant_location[0]
        y = ant_location[1]
        
        surrounding_squares = []
        
        for a in range((0 - ANT_SMELL_RADIUS),ANT_SMELL_RADIUS + 1): #plus one added to solve the issue of ants going up and left
            for b in range((0 - ANT_SMELL_RADIUS),ANT_SMELL_RADIUS + 1):
                
                
                if ((x + b) >= 0 and (x + b) < MAP_WIDTH): #error handling for indexing outside the map
                    if ((y + a) >= 0 and (y + a) < MAP_HEIGHT):
                        surrounding_squares.append([x + b,y + a])

        return surrounding_squares
    
