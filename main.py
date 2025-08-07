from game_interface import GameInterface
from map import Map
from snake import Snake
from fruit import Fruit
import random
class Main:
    def __init__(self):
        self.interface = GameInterface()
        self.map = Map()
        self.snake = Snake()
        self.fruit = Fruit()
    
    def loop(self):
        print("Loop iniciated")
        print("________________________________________________________")
        self.map.reset_map()

        if self.fruit.dead():
            empty_blocks = self.map.get_empty_blocks()
            fruit_new_position = random.choice(empty_blocks)
            self.fruit.update_position(fruit_new_position)
        
        if self.snake.dead():
            empty_blocks = self.map.get_empty_blocks()
            snake_new_position = [random.choice(empty_blocks)]
            self.snake.update_position(snake_new_position)
            print(f"test: {snake_new_position}")

        self.map.drawm_entity("fruit", self.fruit.get_position())
        self.map.drawm_entity("snake", self.snake.get_position())

        print(f"Snake Position: {self.snake.get_position()}")
        print(f"Fruit Position: {self.fruit.get_position()}")

        self.interface.show_map(self.map.grid)

        player_input = self.interface.get_player_input()
        while not player_input:
            player_input = self.interface.get_player_input()

        self.snake.move_snake(player_input)

main = Main()
run = True
turn = 0
while run:
    turn += 1
    main.loop()
    # if turn == 10:
    #     run = False