import random
class Snake:
    def __init__(self):
        self.snake_head_char = "0"
        self.snake_body_char = "°"
        self.snake_position = []

    def get_snake_position(self, map_dimentions):
        map_width = map_dimentions[0]
        map_height = map_dimentions[1]
        if len(self.snake_position) == 0:
            # generate random initial position
            self.snake_position = [[random.randrange(0, map_height), random.randrange(0, map_width)]]
        
        return self.snake_position 

    def move_snake(self, direction):
        new_snake_position = []
        for body_part_position in self.snake_position:
            # move head
            if body_part_position == self.snake_position[0]:
                match direction.lower():
                    case "up":
                        body_part_position[1] += 1
                    case "down":
                        body_part_position[1] -= 1
                    case "right":
                        body_part_position[0] += 1
                    case "left":
                        body_part_position[0] -= 1
                    case _:
                        print("Input key incorrect")
                new_snake_position = body_part_position
            
            old_body_part_position = body_part_position
        self.snake_position = new_snake_position
