import random
class Map:

    def __init__(self):
        self.map_width = 40
        self.map_height = 10

        self.empty_block_char = "~"
        self.fruit_block_char = "@"
        self.snake_head_char = "0"
        self.snake_body_char = "°"

        self.grid = [[self.empty_block_char for x in range(self.map_width)] for y in range(self.map_height)]

    def test(self):
        test_x = 1
        test_y = 5
        self.grid[test_x][test_y] = "T"

    def get_empty_blocks(self):
        row_index = 0
        list_empty_blocks = []
        for row in self.grid:
            column_index = 0
            for block in row:
                column_index += 1
                if block == self.empty_block_char:
                    current_index = [row_index, column_index]
                    list_empty_blocks.append(current_index)
            row_index += 1
        return list_empty_blocks

    def get_map_dimentions(self):
        return [self.map_width, self.map_height]

    def drawm_entity(self, entity_type, entity_position):
        match entity_type:
            case "snake":
                for snake_body_part_position in entity_position:
                    body_part_char = self.snake_head_char if snake_body_part_position == entity_position[0] else self.snake_body_char
                    body_part_position_x = snake_body_part_position[0]
                    body_part_position_y = snake_body_part_position[1]
                    self.grid[body_part_position_x][body_part_position_y] = body_part_char
            case "fruit":
                postion_x = entity_position[0] 
                position_y = entity_position[1]
                self.grid[postion_x][position_y] = self.fruit_block_char
            case _:
                print(f"ERROR: entity '{entity_type}' is unkown.")
                exit

    def drawm_snake(self, snake_position, snake_head_char, snake_body_char):
        for snake_body_part_position in snake_position:
            body_part_char = snake_head_char if snake_body_part_position == snake_position[0] else snake_body_char
            print(f"Body part drawn:{body_part_char}")
            print(f"Body part position:{snake_body_part_position}")
            body_part_position_x = snake_body_part_position[0]
            body_part_position_y = snake_body_part_position[1]
            self.grid[body_part_position_x][body_part_position_y] = body_part_char

from game_interface_class import GameInterface
i = GameInterface
game_map = Map()
i.show_map(game_map.grid)