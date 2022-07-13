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
    
    #currently set up for ants to explore while no food signals have been found
    def local_search(self, ant_location, has_food):
        
        low_val = 100000
        high_val = 0
        move_choices = []
        move_choice = []
        
        
        #check the squares surrounding the ant location
        surrounding_squares = f.surrounding_squares(ant_location)
        
        adjacent_squares = f.adjacent_squares(ant_location)
        
        #IF THE DOESN'T HAVE FOOD:
        if (has_food == False):
            #print("looking for food")
            for s in surrounding_squares:
                if (food_pheremone_map[s[0]][s[1]] > 0):
                    #high_val = food_pheremone_map[s[0]][s[1]]
                    move_choices.append(s)

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
                move_choice = self.move_towards_choice(ant_location, move_choice)
                return move_choice
            else:    
                rand = random.randint(0,len(adjacent_squares) - 1)
                return adjacent_squares[rand]
            
        elif (has_food == True):

            for s in surrounding_squares:
                if (home_pheremone_map[s[0]][s[1]] > 0):
                    #high_val = food_pheremone_map[s[0]][s[1]]
                    move_choices.append(s)
                    
            if (len(move_choices) != 0):
                
                hive_loc = HIVE_LOCATIONS[0]
                hive_x = hive_loc[0]
                hive_y = hive_loc[1]
                #print(len(move_choices))
                for m in move_choices:
                    if(f.distance_squared(m[0],m[1],hive_x,hive_y) < low_val):
                        move_choice = m
                #print(home_pheremone_map[move_choice[0]][move_choice[1]])        
                #choose a random move from all options that have been determined to be equally as good
                #rand = random.randint(0,len(move_choices) - 1)
                
                move_choice = self.move_towards_choice(ant_location, move_choice)
                return move_choice
            else:

                rand = random.randint(0,len(adjacent_squares) - 1)
                return adjacent_squares[rand]    

    
    
        
    def move_towards_choice(self, ant_location, move): #this method will choose the adjacent square which moves the ant closer to its optimal choice, decided in local_search
            
            low_val = 100000
            move_choice = []
            move_choices = []
            adjacent_squares = f.adjacent_squares(ant_location)
            
            for a in adjacent_squares:
                if(f.distance_squared(a[0],a[1],move[0],move[1]) < low_val):
                        low_val = f.distance_squared(a[0],a[1],move[0],move[1])
            
            for b in adjacent_squares:
                if(f.distance_squared(b[0],b[1],move[0],move[1]) == low_val):
                    move_choices.append(b)
            
            rand = random.randint(0,len(move_choices) - 1)
            move_choice = move_choices[rand]
            return move_choice
        
    #def simulated_annealing(self, ant_location, has_food): 
#     def go_home
#         
#         
#         
        
#             for x in surrounding_squares:
#                 food_pheremone_map[s[0]][s[1]] == high_val
#                 move_choices.append(x)
            
#             if (len(move_choices) == 0):
                 #print("no scent")
#                 for s in surrounding_squares:
#                     if(home_pheremone_map[s[0]][s[1]] < low_val):
#                         low_val = home_pheremone_map[s[0]][s[1]]
#                 
#                 for x in surrounding_squares:
#                     home_pheremone_map[s[0]][s[1]] == low_val
#                     move_choices.append(x)
                    
                    

#             for m in move_choices:
#                 if(f.distance_squared(s[0],s[1],hive_x,hive_y) < low_val):
#                     low_val = f.distance_squared(s[0],s[1],hive_x,hive_y)
#                     
#             for x in surrounding_squares:
#                 if(f.distance_squared(x[0],x[1],hive_x,hive_y) == low_val):
#                     move_choices.append(x)    
#              #choose a random move from all options that have been determined to be equally as good
#             rand = random.randint(0,len(move_choices) - 1)
    
    
                #print("found food")
#             for s in surrounding_squares:
#                 if(home_pheremone_map[s[0]][s[1]] > high_val):
#                     high_val = home_pheremone_map[s[0]][s[1]]
#             
#             for x in surrounding_squares:
#                 if(home_pheremone_map[x[0]][x[1]] >= high_val):
#                     move_choices.append(x)