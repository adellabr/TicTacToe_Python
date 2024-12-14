import copy
from domain.model import Game
from datasource.model import StorageModel


def game_to_storage_model(game: Game):
    storage_model = StorageModel()
    storage_model.uuid = game.uuid
    storage_model.field = copy.deepcopy(game.field)
    storage_model.current_player = game.current_player
    storage_model.enemy = game.enemy
    return storage_model


def storage_model_to_game(storage_model: StorageModel):
    game = Game()
    game.uuid = storage_model.uuid
    game.field = copy.deepcopy(storage_model.field)
    game.current_player = storage_model.current_player
    game.enemy = storage_model.enemy
    return game
    
    