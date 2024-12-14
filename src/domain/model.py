import uuid


class Symbols:
    EMPTY = 0
    CROSS = 'X'
    NOUGHT = 'O'
    
    
class Field:
    def __init__(self):
        self.table = [[0] * 3 for _ in range(3)]
        
        
    def get_cell(self, cell: int):
        return self.table[cell // 3][cell % 3]
    
    
    def set_cell(self, cell: int, symbol):
        self.table[cell // 3][cell % 3] = symbol
        
        
    def is_full(self):
        return all(elem != 0 for row in self.table for elem in row)
    
    
    def check_winner(self):
        winner = None
        if self.table[0][0] == self.table[1][1] and self.table[0][0] == self.table[2][2]:
            winner = self.table[0][0]
        elif self.table[0][2] == self.table[1][1] and self.table[0][2] == self.table[2][0]:
            winner = self.table[0][2]
        else:
            for i in range(3):
                if self.table[i][0] == self.table[i][1] and self.table[i][0] == self.table[i][2]:
                    winner = self.table[i][0]
                elif self.table[0][i] == self.table[1][i] and self.table[0][i] == self.table[2][i]:
                    winner = self.table[0][i]
        return winner 
    
    
    def reset(self):
        for row in self.table:
            for elem in row:
                elem = 0

    
class Game:
    def __init__(self):
        self.field = Field()
        self.uuid = uuid.uuid4()
        self.current_player = Symbols.CROSS
        self.enemy = Symbols.NOUGHT
        

    def switch_player(self):
        if self.current_player == Symbols.CROSS:
            self.current_player = Symbols.NOUGHT
            self.enemy = Symbols.CROSS
        else:
            self.current_player = Symbols.CROSS
            self.enemy = Symbols.NOUGHT
            

    def print_field(self):
        for i in range(3):
            for j in range(3):
                print(self.field.table[i][j], end=" ")
            print()

