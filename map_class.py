import random
class Map:

    def __init__(self):
        self.map_width = 40
        self.map_height = 10
        self.empty_block_char = "~"
        self.fruit_block_char = "@"

        self.grid = [[self.empty_block_char for x in range(self.map_width)] for y in range(self.map_height)]

    def test(self):
        return "test"

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

    def spawn_fruit(self):
        # Choose one empty block to became a fruit
        fruit_block = random.choice(self.get_empty_blocks())
        fruit_block_x = fruit_block[0] 
        fruit_block_y = fruit_block[1]
        self.grid[fruit_block_x][fruit_block_y] = self.fruit_block_char
        print(f"Fruit spawned at {fruit_block}")


# game_map = Map()
# print(game_map.spawn_fruit())