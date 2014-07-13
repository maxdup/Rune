# -*- coding: utf-8 -*-
from rune.header import header
from rune.schema import schema
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
            schema1 = schema(1)
            schema2 = schema(2)
            schema3 = schema(3)
            schema4 = schema(4)

            schema1.setSchema(['int', 'uint', 'str', 'ref'])
            schema2.setSchema(['int', 'ref'])
            schema3.setSchema(['str', 'ref', 'ref'])
            schema4.setSchema(['int', 'uint', 'str', 'ref', ' int', 'ref', 'str', 'ref'])

            self.file = open(filename, 'wb')

            self.header = header(self.file)
            self.header.write()

            schema1.write(self.file)
            schema2.write(self.file)
            schema3.write(self.file)
            schema4.write(self.file)

    def add_schema(self, schema):
        self.schemas.append(schema)
        self.header.add_schema(schema)
        schema.write(self.file)

    def read_schema(self, index):
        schema = schema(index)
        self.seek(16 * (index + 1))
        schema.offset = struct.unpack('i', db_file.read(4))[0]
        schema.rune_length = struct.unpack('i',db.file.read(4))[0]
        schema.flag1 = struct.unpack('i', db_file.read(4))[0]
        schema.flag2 = struct.unpack('i', db_file.read(4))[0]
