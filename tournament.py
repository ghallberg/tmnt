import itertools
import utils
import tournament_round
import player


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
    events = utils.find_events('joined_tournament', ('tournament', t_id))
    return [event['player'] for event in events]

def rounds(t_id):
    events = utils.find_events('round_added', ('tournament', t_id))
    return [event['round'] for event in events]

def add_player_to_tournament(p_id, t_id):
    utils.store_event({'type': 'joined_tournament', 'tournament': t_id, 'player': p_id})

def seed_round(t_id):
    round_id = tournament_round.seed(players(t_id))
    utils.store_event({'type': 'round_added', 'tournament': t_id, 'round': round_id})

def as_str(t_id):
    t = fetch(t_id)
    u_str= "\n    ".join([player.as_str(p) for p in t['players']])
    r_str= "\n    ".join([tournament_round.as_str(r) for r in t['rounds']])
    return f"""Name: {t['name']}
UUID: {t['uuid']}
Participants:
    {u_str}
Rounds:
    {r_str}"""
