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
RANDMIN = g.get_rand_min()
RANDMAX = g.get_rand_max()
#importing the food and home pheromone maps
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
        
        
        #check the squares surrounding the ant location that it can smell
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
                        low_val = f.distance_squared(m[0],m[1],food_x,food_y)
                        move_choice = m
                        

#TRYING TO MAKE CHOICES ONLY INVOLVING PHEROMONES WHILE SEARCHING FOR FOOD
#                 for s in surrounding_squares:
#                     if(food_pheremone_map[s[0]][s[1]] > high_val):
#                         high_val = food_pheremone_map[s[0]][s[1]]
#                 
#                 for x in surrounding_squares:
#                     if(food_pheremone_map[x[0]][x[1]] == high_val):
#                         move_choices.append(x)
#                         
#                 #choose a random move from all options that have been determined to be equally as good
#                 rand = random.randint(0,len(move_choices) - 1)
#                 move_choice = move_choices[rand]
                
                
                
                
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

                for m in move_choices:
                    if(f.distance_squared(m[0],m[1],hive_x,hive_y) < low_val):
                        low_val = f.distance_squared(m[0],m[1],hive_x,hive_y)
                        move_choice = m

#TRYING TO MAKE CHOICES ONLY INVOLVING PHEROMONES WHILE SEARCHING FOR HOME
#                 for s in surrounding_squares:
#                     if(home_pheremone_map[s[0]][s[1]] > high_val):
#                         high_val = home_pheremone_map[s[0]][s[1]]
#                 
#                 for x in surrounding_squares:
#                     if(home_pheremone_map[x[0]][x[1]] == high_val):
#                         move_choices.append(x)
#                         
#                 #choose a random move from all options that have been determined to be equally as good
#                 rand = random.randint(0,len(move_choices) - 1)
#                 move_choice = move_choices[rand]
                
                
                
                
                move_choice = self.move_towards_choice(ant_location, move_choice)
                return move_choice
            else:

                rand = random.randint(0,len(adjacent_squares) - 1)
                return adjacent_squares[rand]    

    def local_search_2(self, ant_location, has_food):
        
        low_val = 100000
        high_val = 0
        
        #these vals will be used as part of randint(randmin, randmax) in order to generate random vals to multiply the attractiveness level of the square by
        randmin = RANDMIN
        randmax = RANDMAX
        move_choices = []
        #the indices of these arrays need to correspond with the move_choices array indices properly
        move_choices_pheremone_levels = []
        move_choices_after_randomizing = []
        
        #the final array that will hold the possible move choices
        final_move_choices = []
        
        #check the squares surrounding the ant location
        surrounding_squares = f.surrounding_squares(ant_location)
        adjacent_squares = f.adjacent_squares(ant_location)
        
        #adding the surrounding squares as possible move choices
        for s in surrounding_squares:
            move_choices.append(s)
        
#         for s in adjacent_squares:
#              move_choices.append(s)
         
        #IF THE ANT DOESN'T HAVE FOOD, IT SHOULD SEARCH FOR FOOD
        if (has_food == False):
            
            #lets add some scores to the move_choices_pheremone_levels array
            for m in move_choices:
                move_choices_pheremone_levels.append(food_pheremone_map[m[0]][m[1]])
            
            for c in move_choices_pheremone_levels:
                move_choices_after_randomizing.append((1 + c) * random.randint(randmin,randmax))
                
            
            for s in move_choices_after_randomizing:
                if (s >= high_val):
                    high_val = s
            
            for i in range(len(move_choices_after_randomizing)):
                if(move_choices_after_randomizing[i] == high_val):
                    #append a move choice from the original array to the final move choices array
                    final_move_choices.append(move_choices[i])
            
            
            move_choice = final_move_choices[random.randint(0,len(final_move_choices) - 1)]
            move_choice = self.move_towards_choice(ant_location, move_choice)
            return move_choice
        #IF THE ANT HAS FOOD, IT SHOULD SEARCH FOR HOME TO DROP IT OFF
        elif(has_food == True):
            
            for m in move_choices:
                move_choices_pheremone_levels.append(home_pheremone_map[m[0]][m[1]])
                
            for c in move_choices_pheremone_levels:
                move_choices_after_randomizing.append((1 + c) * random.randint(randmin,randmax))
            
            for s in move_choices_after_randomizing:
                if (s >= high_val):
                    high_val = s
            
            for i in range(len(move_choices_after_randomizing)):
                if(move_choices_after_randomizing[i] == high_val):
                    #append a move choice from the original array to the final move choices array
                    final_move_choices.append(move_choices[i])
            
            move_choice = final_move_choices[random.randint(0,len(final_move_choices) - 1)]
            move_choice = self.move_towards_choice(ant_location, move_choice)
            return move_choice
            
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
    
    #this method will take in the pheremones surrounding the ant and randomly decide, based on how attractive each choice is, which direction to move.
    #the thresholds for the decision will need to be fine-tuned.
        
    def pheremone_calculator(self): 
        print('hi')
        
        
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