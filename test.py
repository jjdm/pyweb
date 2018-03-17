from tinydb import TinyDB, Query
import pprint as pp

db = TinyDB('db.json')
db.purge_tables()

db.insert({'int': 1, 'char': 'a'})
db.insert({'int': 1, 'char': 'b'})

groups = db.table('groups')
groups.insert({'name': 'user', 'permissions': [{'type': 'read'}]})
groups.insert({'name': 'sudo', 'permissions': [{'type': 'read'}, {'type': 'sudo'}]})
groups.insert({'name': 'admin', 'permissions': [{'type': 'read'}, {'type': 'write'}, {'type': 'sudo'}]})

pp.pprint(db.all())