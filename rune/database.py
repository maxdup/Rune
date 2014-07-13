# -*- coding: utf-8 -*-
import struct
import os

from rune.header import Header

from rune.schema import Schema


class Database:

    def __init__(self, filename):
        self.schemas = []
        if os.path.isfile(filename):
            self.file = open(filename, mode='rb')
            self.header = Header(self.file)

            for x in range(0, self.header.nb_schemas):
                self.schemas.append(self.read_schema(x))
        else:
            self.file = open(filename, 'wb')
            self.header = Header(self.file)
            self.header.write()

    def add_schema(self, insert_schema):
        self.schemas.append(insert_schema)
        self.header.add_schema(insert_schema)
        #schema.write(self.file)
        self.write_schema(insert_schema)

    def read_schema(self, index):
        found_schema = Schema(index)
        self.file.seek(16 * (index + 1))
        found_schema.offset = struct.unpack('i', self.file.read(4))[0]
        found_schema.length = struct.unpack('i', self.file.read(4))[0]
        found_schema.flag1 = struct.unpack('i', self.file.read(4))[0]
        found_schema.flag2 = struct.unpack('i', self.file.read(4))[0]
        return Schema

    def write_schema(self, schema):
        self.file.seek(16 * (schema.schemaID + 1))
        self.file.write(struct.pack('i', schema.offset))
        self.file.write(struct.pack('i', schema.length))
        self.file.write(struct.pack('i', schema.flag1))
        self.file.write(struct.pack('i', schema.flag2))
