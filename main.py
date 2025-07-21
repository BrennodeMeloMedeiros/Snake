from game_interface_class import GameInterface
from map_class import Map

class Main:
    def __init__(self):
        self.game_map = Map()
        self.ifc = GameInterface()
    
    def loop(self):
        print("Loop iniciated")
        self.game_map.spawn_fruit()
        self.ifc.show_map(self.game_map.grid)

main = Main()
main.loop()


# run = True
# c = 0
# while run:
#     c += 1
#     main.loop
#     if c == 10:
#         run = False