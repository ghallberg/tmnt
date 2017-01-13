from tinydb import TinyDB, Query

import utils
import match

import random
from itertools import zip_longest

def seed(players):
    round_uuid = utils.generate_uuid()

    pairs = random_pairs(players)
    matches = [match.add([p1, p2]) for p1, p2 in pairs]

    utils.store_event({'type': 'create_round', 'matches': matches, 'round': round_uuid})

    return round_uuid

def fetch(r_id):
    db = TinyDB('panik.db')

    Event = Query()
    creation = db.search((Event.round == r_id) &
            (Event.type == 'create_round'))[0]


    return {'uuid': creation['round']}

def matches(r_id):
    result = utils.find_events('create_round', ('round', r_id))[0]
    return result['matches']

def as_str(r_id):
    r = fetch(r_id)
    return f"""UUID: {r['uuid']}"""

def random_pairs(iterable):
    random.shuffle(iterable)
    args = [iter(iterable)] * 2
    return zip_longest(*args, fillvalue=None)
