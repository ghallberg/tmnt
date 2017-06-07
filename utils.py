from tinydb import TinyDB, where
import uuid

def db():
    return TinyDB('panik.db')

def store_event(input):
    db().insert(input)

def find_events(type, query_params):
    key, value = query_params

    return db().search((where('type') == type) & (where(key) == value))

def first_event(type, query_params):
    return find_events(type, query_params)[0]


def generate_uuid():
    return str(uuid.uuid4())
