from flask import Blueprint, render_template, request, redirect, url_for
from domain.model import Game
from domain.service import GameInterface
from datasource.mapper import game_to_storage_model, storage_model_to_game
from web.mapper import game_to_model, model_to_game
from di.container import Container


main_blueprint = Blueprint('main', __name__)
conteiner = Container()


@main_blueprint.route('/')
def go_to_start():
    return redirect(url_for('main.start'))


@main_blueprint.route('/start', methods=['GET', 'POST'])
def start():
    if request.method == 'POST':
        game = Game()
        storage_model = game_to_storage_model(game)
        conteiner.save(storage_model)
        return redirect(url_for('main.play_game', game_id=game.uuid))
    return render_template("index.html")


@main_blueprint.route('/game/<uuid:game_id>', methods=['GET', 'POST'])
def play_game(game_id):
    winner = None
    storage_model = conteiner.get(game_id)
    game = storage_model_to_game(storage_model)
    game_interface = GameInterface(game)
    is_finish, winner = game_interface.is_finish()
    if request.method == 'POST' and not is_finish:
        cell = int(request.form['cell'])
        is_insert = game_interface.insert_input(cell)
        is_finish, winner = game_interface.is_finish()
        if not is_finish and is_insert:
            cell = game_interface.computer_step()
            game_interface.insert_input(cell)
            is_finish, winner = game_interface.is_finish()
        storage_model = game_to_storage_model(game)
        conteiner.save(storage_model)
    web_model = game_to_model(game)
    return render_template("index.html", board=web_model.field.table, game_id=game_id, is_finish=is_finish, winner=winner)
     
     