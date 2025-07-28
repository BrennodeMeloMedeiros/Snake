from game_interface_class import GameInterface
from map_class import Map
from snake_class import Snake
from fruit_class import Fruit
import random
class Main:
    def __init__(self):
        self.interface = GameInterface()
        self.map = Map()
        self.snake = Snake()
        self.fruit = Fruit()
    
    def loop(self):
        print("Loop iniciated")
        
        empty_blocks = self.map.get_empty_blocks()
        snake_position = self.snake.get_snake_position(self.map.get_map_dimentions())
        
        if self.fruit.was_eaten():
            fruit_block = random.choice(empty_blocks)
            self.map.drawm_entity("fruit", fruit_block)
            self.fruit.update_position(fruit_block)
            print(f"Fruit spawned at {fruit_block}")

        self.map.drawm_entity("snake", snake_position)
        
        self.interface.show_map(self.map.grid)
        player_input = input("Up/Down/Right/Left")
        self.snake.move_snake(player_input)

main = Main()
run = True
c = 0
while run:
    c += 1
    main.loop()
    if c == 10:
        run = False