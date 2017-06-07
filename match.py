import utils
import player

def add(players):
    match_uuid = utils.generate_uuid()

    utils.store_event({'type': 'add_match', 'players': players, 'match': match_uuid})
    return match_uuid

def fetch(m_id):
    creation = utils.find_events('add_match', ('match', m_id))[0]
    return {'uuid': m_id,
            'players': creation['players']}


def as_str(m_id):
    m = fetch(m_id)

    players = [player.as_str(p_id) for p_id in m['players']]
    p_str = ' - '.join(players)

    return f"""UUID: {m['uuid']}
Matchup:
    {p_str}"""
