from game_interface_class import GameInterface
from map_class import Map

class Main:
    def __init__(self):
        self.game_map = Map()
        self.ifc = GameInterface()
    
    def loop(self):
        self.game_map = self.game_map.spawn_fruit()
        self.ifc.show_map(self.game_map)


main = Main()
main.loop()
main.loop()
