from tinydb import TinyDB, Query
import utils

def add(name):
    user_uuid = utils.generate_uuid()
    utils.store_event({'type': 'add_user', 'name': name, 'user': user_uuid})
    return user_uuid

def fetch(u_id):
    return utils.find_events('add_user', ('user', u_id))[0]

def as_str(u_id):
    if u_id == None:
        return 'BYE'
    else:
        u = fetch(u_id)
        return f"Name: {u['name']}"

