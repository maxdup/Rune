from rune.database import database
from rune.schema import schema

db = database('db.rune')

schema = schema(1,['int','uint','obj','str'])

db.add_schema(schema)
