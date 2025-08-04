class Entity:
    def __init__(self):
        self.position = []
        
    def get_position(self):
        return self.position
    
    def update_position(self, new_position):
        self.position = new_position

    def dead(self):
        return False if len(self.position) > 0 else True
