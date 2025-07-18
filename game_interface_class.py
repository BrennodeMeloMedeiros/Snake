
class GameInterface:

    def show_map(self, grid):
        print()
        print()
        print()
        for line in grid:
            line_drawing = ""
            for block in line:
                line_drawing += block
            print(line_drawing)

# ifc = GameInterface()
# ifc.show_map()