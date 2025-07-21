from game_interface_class import GameInterface
from map_class import Map
from snake_class import Snake

class Main:
    def __init__(self):
        self.game_map = Map()
        self.ifc = GameInterface()
        self.snake = Snake()
    
    def loop(self):
        print("Loop iniciated")
        
        
        snake_position = self.snake.get_snake_position(self.game_map.get_map_dimentions())
        print(snake_position)
        self.game_map.drawm_snake(snake_position, self.snake.snake_head_char, self.snake.snake_body_char)
        
        
        self.game_map.spawn_fruit()
        self.ifc.show_map(self.game_map.grid)
        #player_input = input("Up/Down/Right/Left")

main = Main()
main.loop()


# run = True
# c = 0
# while run:
#     c += 1
#     main.loop
#     if c == 10:
#         run = False