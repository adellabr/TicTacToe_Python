class GameModel:
    def __init__(self):
        self.uuid = None
        self.field = None
        self.current_player = None
        self.enemy = None
        
    def print_field(self):
        for i in range(3):
            for j in range(3):
                print(self.field.table[i][j], end=" ")
            print()
