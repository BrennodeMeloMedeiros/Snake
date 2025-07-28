import random
class Fruit():
    def __init__(self):
        self.fruit_position = []

        def get_fruit_position(self):
            if not self.fruit_position:
            # Choose one empty block to became a fruit
            fruit_block = random.choice(self.get_empty_blocks())
            fruit_block_x = fruit_block[0] 
            fruit_block_y = fruit_block[1]
            self.grid[fruit_block_x][fruit_block_y] = self.fruit_block_char
            print(f"Fruit spawned at {fruit_block}")