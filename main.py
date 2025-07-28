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


        if self.fruit.was_eaten():
            empty_blocks = self.map.get_empty_blocks()
            fruit_new_position = random.choice(empty_blocks)
            self.map.drawm_entity("fruit", fruit_new_position)
            self.fruit.update_position(fruit_new_position)
            print(f"Fruit spawned at {fruit_new_position}")

        if not self.snake.get_snake_position():
            empty_blocks = self.map.get_empty_blocks()
            snake_new_position = random.choice(empty_blocks)
            self.snake.update_position(snake_new_position)
            self.map.drawm_entity("snake", snake_new_position, empty_blocks)

        self.map.clear_map(snake_new_position, fruit_new_position)

        self.interface.show_map(self.map.grid)

        
        self.snake.move_snake(player_input)

main = Main()
run = True
c = 0
while run:
    c += 1
    main.loop()
    if c == 10:
        run = False