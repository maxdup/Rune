# -*- coding: utf-8 -*-
from header import header
import os


class database:

    def __init__(self):
        self.schemas = []
        if os.path.isfile('db.rune'):
            with open('db.rune', mode='rb') as db_file:
                self.header = header(db_file)
                self.header.read()
                print (str(self.header))
                self.header.print_schemas()
        else:
            self.file = open('db.rune', 'wb')
            self.header = header(self.file)
            self.header.write()

    def add_schema(self, schema):
        self.schemas.append(schema)
        self.header.add_schema(schema)
        schema.write(self.file)
