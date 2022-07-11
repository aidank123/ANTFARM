#this class will store all global variables and be imported by each class
#COLORS

WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

class Globals:
    def __init__(self):
        self.NUMOFANTS = 100
        self.WIDTH = 1100
        self.HEIGHT = 800
        self.HIVE_LOCATIONS = [[300,300]] #must be formatted in this way so the x and y values can be indexed
        self.FOOD_LOCATIONS = [[50,50]]
        self.ANT_COLOR = BLACK
        self.MAP_COLOR = WHITE
        self.FOOD_COLOR = BLUE
        self.HIVE_COLOR = GREEN
        
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
    