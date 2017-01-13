from tinydb import TinyDB, Query
import tournament
import tournament_round
import user
import match

if __name__ == '__main__':
    t_id = tournament.add('granament')


    user_names = ['gran granman', 'gran grankvinna','gran granbarn', 'gran granhen', 'gran granhund']
    user_ids = [user.add(user_name) for user_name in user_names]

    [tournament.add_user_to_tournament(u_id, t_id) for u_id in user_ids]

    tournament.seed_round(t_id)

    print("RAW TOURNAMENT")
    print( tournament.fetch(t_id) )
    print("\nTOURNAMENT")
    print( tournament.as_str(t_id) )
    print("\nMATCHES")

    r_id = tournament.rounds(t_id)[0]
    matches = tournament_round.matches(r_id)
    print("\n\n".join([match.as_str(m_id) for m_id in matches]))



