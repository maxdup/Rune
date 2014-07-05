# -*- coding: utf-8 -*-
from rune.header import header
import os


class database:

    def __init__(self, filename):
        self.schemas = []
        if os.path.isfile(filename):
            with open('db.rune', mode='rb') as db_file:
                self.header = header(db_file)
                self.header.read()
                self.header.print_schemas()
        else:
            self.file = open(filename, 'wb')
            self.header = header(self.file)
            self.header.write()

    def add_schema(self, schema):
        self.schemas.append(schema)
        self.header.add_schema(schema)
        schema.write(self.file)
