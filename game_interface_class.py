from map_class import Map

class GameInterface:

    def ShowMap(self):
        print()
        print()
        print()
        game_map = Map()

        for line in game_map.grid:
            line_drawing = ""
            for block in line:
                line_drawing += block
            print(line_drawing)

ifc = GameInterface()
ifc.ShowMap()