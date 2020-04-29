from flask import Blueprint, jsonify, request
from . import db
from .models import Player
main = Blueprint('main', __name__)

@main.route('/add_player', methods=['POST'])
def add_player():
    player_data = request.get_json()
    
    new_player = Player(name=player_data['name'], rating=player_data['rating'])
    db.session.add(new_player)
    db.session.commit()

    return 'Done', 201

@main.route('/players', methods=['GET'])
def players():
    players_list = Player.query.all()
    players = []

    for player in players_list:
        players.append({'name':player.name, 'rating': player.rating})
    
    return jsonify({"players":players})

