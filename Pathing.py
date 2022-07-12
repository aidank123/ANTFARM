import Globals as gl
import Pheremone_Map as pm
import random
import Functions
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

f = Functions.Functions()

class Pathing:
    
    def __init__(self):
        
        self.move_choice = 0
        
    def surrounding_squares(self, ant_location):
        x = ant_location[0]
        y = ant_location[1]
        
        surrounding_squares = [[x-1,y-1],[x,y-1],[x+1,y-1],[x+1,y],[x+1,y+1],[x,y+1],[x-1,y+1],[x-1,y]]
        
        return surrounding_squares
    
    #currently set up for ants to explore while no food signals have been found
    def local_search(self, ant_location, has_food):
        
        low_val = 10000
        high_val = 0
        move_choices = []
        move_choice = []
        #check the 8 squares surrounding the ant location
        surrounding_squares = self.surrounding_squares(ant_location)
        
        if (has_food == False):
            #print("looking for food")
            for s in surrounding_squares:
                if (food_pheremone_map[s[0]][s[1]] > 0):
                    #high_val = food_pheremone_map[s[0]][s[1]]
                    move_choices.append(s)
#             for x in surrounding_squares:
#                 food_pheremone_map[s[0]][s[1]] == high_val
#                 move_choices.append(x)
            
#             if (len(move_choices) == 0):
#                 #print("no scent")
#                 for s in surrounding_squares:
#                     if(home_pheremone_map[s[0]][s[1]] < low_val):
#                         low_val = home_pheremone_map[s[0]][s[1]]
#                 
#                 for x in surrounding_squares:
#                     home_pheremone_map[s[0]][s[1]] == low_val
#                     move_choices.append(x)
                    
                    
            ###########################################################
            #move on pheremone trail towards food

            if (len(move_choices) != 0):
                
                food_loc = FOOD_LOCATIONS[0]
                food_x = food_loc[0]
                food_y = food_loc[1]
                

                for m in move_choices:
                    if(f.distance_squared(m[0],m[1],food_x,food_y) < low_val):
                        #low_val = f.distance_squared(m[0],m[1],food_x,food_y)
                        move_choice = m
                        
                #choose a random move from all options that have been determined to be equally as good
                #rand = random.randint(0,len(move_choices) - 1)
                return move_choice
            else:    
                rand = random.randint(0,len(surrounding_squares) - 1)
                return surrounding_squares[rand]
            
        elif (has_food == True):
            
            #print("found food")
#             for s in surrounding_squares:
#                 if(home_pheremone_map[s[0]][s[1]] > high_val):
#                     high_val = home_pheremone_map[s[0]][s[1]]
#             
#             for x in surrounding_squares:
#                 home_pheremone_map[s[0]][s[1]] == high_val
#                 move_choices.append(x)    
#             #choose a random move from all options that have been determined to be equally as good
#             rand = random.randint(0,len(move_choices) - 1)
                
                
            # CHEATING A BIT BY USING THE DIST SQUARED
            hive_loc = HIVE_LOCATIONS[0]
            hive_x = hive_loc[0]
            hive_y = hive_loc[1]
            
            for s in surrounding_squares:
                if(f.distance_squared(s[0],s[1],hive_x,hive_y) < low_val):
                    low_val = f.distance_squared(s[0],s[1],hive_x,hive_y)
                    
            for x in surrounding_squares:
                if(f.distance_squared(x[0],x[1],hive_x,hive_y) == low_val):
                    move_choices.append(x)    
             #choose a random move from all options that have been determined to be equally as good
            rand = random.randint(0,len(move_choices) - 1)
            
            return move_choices[rand]
    

#     def go_home
#         
#         
#         
        
    