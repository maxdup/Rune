# -*- coding: utf-8 -*-
from rune.header import header
from rune.schema import schema
import os


class database:

    def __init__(self, filename):
        self.schemas = []
        if os.path.isfile(filename):
            self.file = open(filename, mode='rb')
            self.header = header(self.file)
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

    def read_schema(self, index):
        schema = schema(index)
        self.seek(16 * (index + 1))
        schema.offset = struct.unpack('i', db_file.read(4))[0]
        schema.rune_length = struct.unpack('i',db.file.read(4))[0]
        schema.flag1 = struct.unpack('i', db_file.read(4))[0]
        schema.flag2 = struct.unpack('i', db_file.read(4))[0]
