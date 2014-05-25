from schema import schema
from database import database


schema1 = schema(['int', 'uint', 'str', 'ref'])
schema2 = schema(['int', 'ref'])
schema3 = schema(['str', 'ref', 'ref'])
schema4 = schema(['int', 'uint', 'str', 'ref', ' int', 'ref', 'str', 'ref'])

db = database()
db.add_schema(schema1)
db.add_schema(schema2)
db.add_schema(schema3)
db.add_schema(schema4)


