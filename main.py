from game_interface_class import GameInterface
from map_class import Map
from snake_class import Snake
from fruit_class import Fruit

class Main:
    def __init__(self):
        self.interface = GameInterface()
        self.game_map = Map()
        self.snake = Snake()
        self.fruit = Fruit()
    
    def loop(self):
        print("Loop iniciated")
        
        
        snake_position = self.snake.get_snake_position(self.game_map.get_map_dimentions())
        self.game_map.drawm_snake(snake_position, self.snake.snake_head_char, self.snake.snake_body_char)
        
        self.fruit.spawn_fruit()
        self.interface.show_map(self.game_map.grid)
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