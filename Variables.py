#this class will be used to update and store variables taken through out, such as food collected, num of successful paths etc



class Variables:
    
    def __init__(self):
        
        self.total_food_collected = 0
        
    def update_total_food_collected(self):
        self.total_food_collected += 1
        self.set_total_food_collected(self.total_food_collected)
        print(self.total_food_collected)
        
    def set_total_food_collected(self, new_total):
        
        self.total_food_collected = new_total
        
    def get_total_food_collected(self):
        
        return self.total_food_collected
    
