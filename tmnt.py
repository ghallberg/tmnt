from tinydb import TinyDB, Query
import tournament
import tournament_round
import player
import match

if __name__ == '__main__':
    t_id = tournament.add('granament')


    player_names = ['gran grankvinna', 'gran granbarn', 'gran granhund']
    player_ids = [player.add(player_name) for player_name in player_names]

    [tournament.add_player_to_tournament(p_id, t_id) for p_id in player_ids]

    tournament.seed_round(t_id)

    print("RAW TOURNAMENT")
    print( tournament.fetch(t_id) )
    print("\nTOURNAMENT")
    print( tournament.as_str(t_id) )
    print("\nMATCHES")

    r_id = tournament.rounds(t_id)[0]
    matches = tournament_round.matches(r_id)

    m_id = matches[0]
    p_id = match.fetch(m_id)['players'][0]
    match.register_point(m_id, p_id)
    match.register_point(m_id, p_id)
    print("\n\n".join([match.as_str(m_id) for m_id in matches]))



