from entity import Entity
class Snake(Entity):
    def __init__(self):
        self.position = []

    def update_position(self, new_position):
        self.position = new_position

    def move_snake(self, direction):
        new_snake_position = []
        for body_part_position in self.position:
            # move head
            if body_part_position == self.position[0]:
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

        self.update_position(new_snake_position)
