import struct


class rune:

    def __init__(self, schema, id=0):
        self.schema = schema['id']  # to associate runes to their schema
        self.runeID = id  # the index of that rune. todo: autoincrement
        self.values = []  # the rune values, according to the schema

    def write(self, db_file):
        db_file.seek(self.length * id)
        for value in self.values:
            db_file.write(struct.pack('i', value))