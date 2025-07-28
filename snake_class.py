import random
class Snake:
    def __init__(self):
        self.snake_position = []

    def get_snake_position(self, map_dimentions):
        map_height = map_dimentions[0] - 1
        map_width = map_dimentions[1] - 1
        if len(self.snake_position) == 0:
            # generate random initial position
            self.snake_position = [[random.randrange(0, map_height), random.randrange(0, map_width)]]
        
        return self.snake_position if len(self.snake_position) > 0 else False

    def update_position(self, new_position):
        self.snake_position = new_position

    def move_snake(self, direction):
        new_snake_position = []
        for body_part_position in self.snake_position:
            # move head
            if body_part_position == self.snake_position[0]:
                match direction:
                    case "up":
                        body_part_position[0] += 1
                    case "down":
                        body_part_position[0] -= 1
                    case "right":
                        body_part_position[1] += 1
                    case "left":
                        body_part_position[1] -= 1
                    case _:
                        print("Input key incorrect")
            # move body 
            else:
                body_part_position = old_body_part_position

            old_body_part_position = body_part_position
            new_snake_position.append(body_part_position)

        self.snake_position = new_snake_position
