import math
import copy
from domain.model import Game, Symbols


class TURN:
    COMP = True
    USER = False


class GameInterface:
    def __init__(self, game: Game):
        self.game = game


    def insert_input(self, cell):
        is_insert = False
        if cell != None and self.game.field.get_cell(cell) == Symbols.EMPTY:
            self.game.field.set_cell(cell, self.game.current_player)
            self.game.switch_player()
            is_insert = True
        return is_insert


    def is_finish(self):
        is_finish = True if self.game.field.is_full() or self.game.field.check_winner() else False
        winner = self.game.field.check_winner()
        return is_finish, winner
    
    
    def computer_step(self):
        best_score = -math.inf
        field = copy.deepcopy(self.game.field)
        best_move = None
        for i in range(3):
            for j in range(3):
                if field.table[i][j] == Symbols.EMPTY:
                    field.table[i][j] = self.game.current_player
                    score = self.minimax(field, 0, TURN.USER)
                    field.table[i][j] = Symbols.EMPTY
                    if score > best_score:
                        best_score = score
                        best_move = i * 3 + j
        return best_move


    def minimax(self, field, depth, is_comp_turn):
        winner = field.check_winner()
        if winner == self.game.current_player:
            return 1
        elif winner == self.game.enemy:
            return -1
        elif field.is_full():
            return 0
        if is_comp_turn:
            best_score = - math.inf
            for i in range(3):
                for j in range(3):
                    if field.table[i][j] == Symbols.EMPTY:
                        field.table[i][j] = self.game.current_player
                        score = self.minimax(field, depth + 1, TURN.USER)
                        field.table[i][j] = Symbols.EMPTY
                        if score > best_score:
                            best_score = score
        else:
            best_score = math.inf
            for i in range(3):
                for j in range(3):
                    if field.table[i][j] == Symbols.EMPTY:
                        field.table[i][j] = self.game.enemy
                        score = self.minimax(field, depth + 1, TURN.COMP)
                        field.table[i][j] = Symbols.EMPTY
                        if score < best_score:
                            best_score = score
        return best_score

