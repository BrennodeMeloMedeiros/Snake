class GameInterface:
    def __init__(self):
        self.direction = ""
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
        print("Select one of the following directions:")
        player_input = input("[Up | Down | Right | Left]: ")
        player_input = player_input.lower()
        directions = ["up", "down", "right", "left"]

        for d in directions:
            match_score = len(set(d).intersection(set(player_input)))
            if match_score > 1:
                self.direction = d
                print(f"Direction choosen: {self.direction} with {match_score} points")
                return self.direction
        if self.direction == "":
            print("Not a valid direction.")
            return False

ifc = GameInterface()
ifc.get_player_input()

player_input = ifc.get_player_input()
while not player_input:
    player_input = ifc.get_player_input()
