#this class will store all global variables and be imported by each class
#COLORS

WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

class Globals:
    def __init__(self):
        self.NUMOFANTS = 1
        self.WIDTH = 200
        self.HEIGHT = 200
        self.HIVE_LOCATIONS = [[50,50]] #must be formatted in this way so the x and y values can be indexed
        self.FOOD_LOCATIONS = [[100,100]]
        self.ANT_COLOR = BLACK
        self.MAP_COLOR = WHITE
        self.FOOD_COLOR = BLUE
        self.HIVE_COLOR = GREEN
        self.PHEREMONE_DECAY_RATE = .01 #rate of pheromone decay
        self.PHEREMONE_DEPOSIT_RATE = .05 #rate of pheromone deposit
        self.ANT_SMELL_RADIUS = 1 #how many squares away can an ant smell
        
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
    
    