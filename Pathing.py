import Globals as gl
import Pheremone_Map as pm
import random
#IMPORT GLOBALS INTO EVERY CLASS

#creating globals object and calling each method
g = gl.Globals()
NUMBER_OF_ANTS = g.get_number_of_ants()
MAP_HEIGHT = g.get_height()
MAP_WIDTH = g.get_width()
HIVE_LOCATIONS = g.get_hive_locations()
FOOD_LOCATIONS = g.get_food_locations()

p = pm.Pheremone_Map()
food_pheremone_map = p.get_food_pheremone_map()
home_pheremone_map = p.get_home_pheremone_map()

class Pathing:
    
    def __init__(self):
        
        self.move_choice = 0
        
    def surrounding_squares(self, ant_location):
        x = ant_location[0]
        y = ant_location[1]
        
        surrounding_squares = [[x-1,y-1],[x,y-1],[x+1,y-1],[x+1,y],[x+1,y+1],[x,y+1],[x-1,y+1],[x-1,y]]
        
        return surrounding_squares
    
    #currently set up for ants to explore while no food signals have been found
    def local_search(self, ant_location):
        
        low_val = 10
        move_choices = []
        
        #check the 8 squares surrounding the ant location
        surrounding_squares = self.surrounding_squares(ant_location)
        
        for s in surrounding_squares:
            if(home_pheremone_map[s[0]][s[1]] <= low_val):
                low_val = home_pheremone_map[s[0]][s[1]]
                move_choices.append(s)
        
        #choose a random move from all options that have been determined to be equally as good
        rand = random.randint(0,len(move_choices) - 1)
        
        return move_choices[rand]
    
    
#     def go_home
#         
#         
#         
        
    