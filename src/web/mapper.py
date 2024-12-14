import copy
from domain.model import Game
from web.model import GameModel


def game_to_model(game: Game):
    model = GameModel()
    model.uuid = game.uuid
    model.field = copy.deepcopy(game.field)
    model.current_player = game.current_player
    model.enemy = game.enemy
    return model


def model_to_game(model: GameModel):
    game = Game()
    game.uuid = model.uuid
    game.field = copy.deepcopy(model.field)
    game.current_player = model.current_player
    game.enemy = model.enemy
    return game