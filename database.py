# -*- coding: utf-8 -*-
from header import header


class database:

    def __init__(self):

        self.schemas = []
        self.file = open('db.rune', 'wb')
        self.header = header(self.file)
        self.header.write(self.file)

    def add_schema(self, schema):
        self.schemas.append(schema)
        self.header.add_schema(schema)
        schema.write(self.file)