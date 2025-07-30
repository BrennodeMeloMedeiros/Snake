import sys
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

    def get_player_input(self):
        direction_choosen = ""
        print("Select one of the following directions:")
        player_input = input("[Up | Down | Right | Left]: ")
        player_input = player_input.lower()
        directions = ["up", "down", "right", "left"]

        for d in directions:
            match_score = len(set(d).intersection(set(player_input)))
            if match_score > 1:
                direction_choosen = d
                print(f"Direction choosen: {direction_choosen} with {match_score} points")
                return direction_choosen
        if direction_choosen == "":
            print("wtf did you type? That's not a direction.")
            sys.exit

ifc = GameInterface()
ifc.get_player_input()