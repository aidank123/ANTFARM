import Globals as gl
import Pheremone_Map as pm

#IMPORT GLOBALS INTO EVERY CLASS

#creating globals object and calling each method
g = gl.Globals()
NUMBER_OF_ANTS = g.get_number_of_ants()
MAP_HEIGHT = g.get_height()
MAP_WIDTH = g.get_width()
HIVE_LOCATIONS = g.get_hive_locations()
FOOD_LOCATIONS = g.get_food_locations()

# p = pm.Pheremone_Map()
# pheremone_map = p.get_map()

class Pathing:
    
    def __init__(self):
        
        self.move_choice = 0
        
    def surrounding_squares(self, ant_location):
        x = ant_location[0]
        y = ant_location[1]
        
        surrounding_squares = [[x-1,y-1],[x,y-1],[x+1,y-1],[x+1,y],[x+1,y+1],[x,y+1],[x-1,y+1],[x-1,y]]
        
        return surrounding_squares
    
    def local_search(self, ant_location):
        
        surrounding_squares = self.surrounding_squares(ant_location)
        
        #check the 8 squares surrounding the ant location assuming no pheremones have been released yet
        
        
    
        
        
        
        
    