#this class will store all global variables and be imported by each class
#COLORS

WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

class Globals:
    def __init__(self):
        self.NUMOFANTS = 100 #total number of ants
        self.WIDTH = 200 #width of the screen
        self.HEIGHT = 200 #height of the screen
        self.HIVE_LOCATIONS = [[50,50]] #must be formatted in this way so the x and y values can be indexed
        self.HIVE_SIZE = 4 #how large to draw the hive
        self.FOOD_LOCATIONS = [[100,100]]
        self.FOOD_SIZE = 4 #how large to draw the food
        self.ANT_COLOR = BLACK 
        self.MAP_COLOR = WHITE
        self.FOOD_COLOR = BLUE
        self.HIVE_COLOR = GREEN
        self.PHEREMONE_DECAY_RATE = .01 #rate of pheromone decay
        self.PHEREMONE_DEPOSIT_RATE = .05 #rate of pheromone deposit
        self.ANT_SMELL_RADIUS = 10 #how many squares away can an ant smells
        
        #increasing the range of these values will increasing the randomness by which an ant operates
        self.RANDMIN = 0 #min value that a pheromone value can be multiplied by when randomizing ant decisions
        self.RANDMAX = 10 #max value that a pheromone value can be multiplied by when randomizing ant decisions
        
        self.FOOD_PHEREMONE_MAX = 10 #how many units of food pheremone an ant starts with
        self.HOME_PHEREMONE_MAX = 10 #how many units of home pheremone an ant starts with
        
        
    def get_number_of_ants(self):
        return self.NUMOFANTS
    
    def get_width(self):
        return self.WIDTH
    
    def get_height(self):
        return self.HEIGHT
    
    def get_hive_locations(self):
        return self.HIVE_LOCATIONS
    
    def get_food_locations(self):
        return self.FOOD_LOCATIONS
    
    def get_ant_color(self):
        return self.ANT_COLOR
    
    def get_map_color(self):
        return self.MAP_COLOR
    
    def get_food_color(self):
        return self.FOOD_COLOR
    
    def get_hive_color(self):
        return self.HIVE_COLOR
    
    def get_pheremone_decay_rate(self):
        return self.PHEREMONE_DECAY_RATE
    
    def get_pheremone_deposit_rate(self):
        return self.PHEREMONE_DEPOSIT_RATE
    
    def get_ant_smell_radius(self):
        return self.ANT_SMELL_RADIUS
    
    def get_hive_size(self):
        return self.HIVE_SIZE
    
    def get_food_size(self):
        return self.FOOD_SIZE
        
    def get_rand_min(self):
        return self.RANDMIN
    
    def get_rand_max(self):
        return self.RANDMAX
    
    def get_food_pheremone_max(self):
        return self.FOOD_PHEREMONE_MAX
    
    def get_home_pheremone_max(self):
        return self.HOME_PHEREMONE_MAX
    
    