import random
class Fruit():
    def __init__(self):
        self.fruit_position = []

    def get_current_fruit_position(self):
        return self.fruit_position

    def get_new_fruit_position(self, map_empty_positions):
        if self.fruit_position:
            pass
        # Choose one empty block to became a fruit

    def update_position(self, new_position):
        self.fruit_position = new_position

    def was_eaten(self):
        return False if self.fruit_position else True
    
    def has_been_eaten(self):
        self.fruit_position = []
        pass