import utils
import player
import tournament_round

from itertools import groupby


def add(players):
    match_uuid = utils.generate_uuid()

    utils.store_event({'type': 'add_match', 'players': players, 'match': match_uuid})
    return match_uuid


def parent_tournament(m_id):
    creation = utils.first_event('add_match', ('match', m_id))
    round_added = utils.first_event('round_added', ('round', r_id))
    return round_added['tournament']


def fetch(m_id):
    return {'uuid': m_id,
            'players': players(m_id),
            'scores': score(m_id)}

def players(m_id):
    creation = utils.first_event('add_match', ('match', m_id))
    return creation['players']


def is_finished(m_id):
    scores = list(score(m_id).values())
    return scores and max(scores) >= 2


def score(m_id):
    p_ids = [x for x in players(m_id) if x is not None]
    score_count = {}

    if len(p_ids) == 1:
        score_count[list(p_ids)[0]] = 2

    else:
        point_events = utils.find_events('point_scored', ('match', m_id))
        for event in point_events:
            p_id = event['player']
            if p_id in score_count:
                score_count[p_id] += 1
            else:
                score_count[p_id] = 1

    return score_count


def register_point(m_id, p_id):
    utils.store_event({'type': 'point_scored', 'player': p_id, 'match': m_id})
    return fetch(m_id)


def as_str(m_id):
    m = fetch(m_id)
    p_strings = []

    for p_id in m['players']:
        name = player.as_str(p_id)
        score = m['scores'].get(p_id, 0)
        p_strings.append(f"""{name} {score}""")

    p_str = " - ".join(p_strings)

    f_str = "Finished:"
    if is_finished(m_id):
        f_str = " ".join((f_str, "YES!"))
    else:
       f_str =  " ".join((f_str, "NO!"))

    return f"""UUID: {m['uuid']}
Matchup:
    {p_str}
    {f_str}
    """
