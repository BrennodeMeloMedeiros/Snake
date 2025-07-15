

class Game:
    def __init__(self):
        self.map_width = 10
        self.map_height = 10
        self.game_map = [["~" for x in range(self.map_width)] for y in range(self.map_height)] 

    def ShowMap(self, map):
        print()
        print()
        print()
        for line in map:
            line_drawing = ""
            for column in line:
                line_drawing += column
            print(line_drawing)

game = Game()
new_map = game.game_map
print(new_map)

game.ShowMap(new_map)
