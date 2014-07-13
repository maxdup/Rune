from rune.database import Database
from rune.schema import Schema

db = Database('db.rune')

schema = Schema(1, ['int', 'uint', 'obj', 'str'])

db.add_schema(Schema)
