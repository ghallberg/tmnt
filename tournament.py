import itertools
import utils
import tournament_round
import user


def add(name):
    tournament_uuid = utils.generate_uuid()
    utils.store_event({'type': 'add_tournament', 'name': name, 'tournament': tournament_uuid})
    return tournament_uuid

def fetch(t_id):
    creation = utils.find_events('add_tournament', ('tournament', t_id))[0]

    return {'name': creation['name'],
            'uuid': creation['tournament'],
            'players': players(t_id),
            'rounds': rounds(t_id)}

def players(t_id):
    result = utils.find_events('joined_tournament', ('tournament', t_id))
    return [player['user'] for player in result]

def rounds(t_id):
    result = utils.find_events('round_added', ('tournament', t_id))
    return [t_round['round'] for t_round in result]

def add_user_to_tournament(u_id, t_id):
    utils.store_event({'type': 'joined_tournament', 'tournament': t_id, 'user': u_id})

def seed_round(t_id):
    round_id = tournament_round.seed(players(t_id))
    utils.store_event({'type': 'round_added', 'tournament': t_id, 'round': round_id})

def as_str(t_id):
    t = fetch(t_id)
    u_str= "\n    ".join([user.as_str(p) for p in t['players']])
    r_str= "\n    ".join([tournament_round.as_str(r) for r in t['rounds']])
    return f"""Name: {t['name']}
UUID: {t['uuid']}
Participants:
    {u_str}
Rounds:
    {r_str}"""
