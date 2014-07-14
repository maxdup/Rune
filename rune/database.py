# -*- coding: utf-8 -*-
import struct
import os

from rune.header import Header
from rune.schema import Schema


class Database:

    def __init__(self, filename):
        self.schemas = []
        if os.path.isfile(filename):
            with open(filename, 'rb') as db_file:
                self.header = Header()
                self.header.read(db_file)

                for x in range(0, self.header.nb_schemas):
                    self.schemas.append(self.read_schema(x))

            self.file = open(filename, mode='wb')
            self.header.file = self.file

        else:
            self.file = open(filename, 'wb')
            self.header = Header()
            self.header.write(self.file)

    def add_schema(self, insert_schema):
        self.schemas.append(insert_schema)
        self.header.add_schema(insert_schema)
        self.header.write()
        self.write_schema(insert_schema)

    def read_schema(self, index):
        found_schema = Schema(index)
        self.file.seek(16 * (index + 1))
        found_schema.offset = struct.unpack('i', self.file.read(4))[0]
        found_schema.length = struct.unpack('i', self.file.read(4))[0]
        found_schema.flag1 = struct.unpack('i', self.file.read(4))[0]
        found_schema.flag2 = struct.unpack('i', self.file.read(4))[0]
        return found_schema

    def write_schema(self, schema):
        self.file.seek(16 * (schema.schemaID + 1))
        self.file.write(struct.pack('i', schema.offset))
        self.file.write(struct.pack('i', schema.length))
        self.file.write(struct.pack('i', schema.flag1))
        self.file.write(struct.pack('i', schema.flag2))
