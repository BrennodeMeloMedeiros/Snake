
import random
class Snake:
    def __init__(self):
        
        self.snake_head = "0"
        self.snake_body = "°"
        self.snake_corpse = [self.snake_head, self.snake_body]
        self.snake_position = []
        
    def move_snake(self, direction):
        new_snake_position = []
        for body_part_position in self.snake_position:
            # move head
            if body_part_position == self.snake_position[0]:
                match direction.lower:
                    case "up":
                        body_part_position[1] += 1
                    case "down":
                        body_part_position[1] -= 1
                    case "right":
                        body_part_position[0] += 1
                    case "right":
                        body_part_position[0] -= 1
            old_body_part_position = body_part_position
        return
    def get_snake_position(self, map_width, map_height):
        
        if len(self.snake_position) == 0:
            # generate random initial position
            self.snake_position = [[random.randrange(0, map_width), random.randrange(0, map_height)]]
        
        return self.snake_position 

