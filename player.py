from tinydb import TinyDB, Query
import utils

def add(name):
    player_uuid = utils.generate_uuid()
    utils.store_event({'type': 'add_player', 'name': name, 'player': player_uuid})
    return player_uuid

def fetch(p_id):
    return utils.first_event('add_player', ('player', p_id))

def as_str(p_id):
    if p_id == None:
        return 'BYE'
    else:
        u = fetch(p_id)
        return f"Name: {u['name']}"

