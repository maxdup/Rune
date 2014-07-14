# -*- coding: utf-8 -*-
from rune.header import header
from rune.schema import schema
import struct
import os


class database:

    def __init__(self, filename):
        self.schemas = []
        if os.path.isfile(filename):
            self.file = open(filename, mode='rb')
            self.header = header(self.file)
            self.header.read()

            for x in range(0, self.header.nb_schemas):
                self.schemas.append(self.read_schema(x))
        else:
            self.file = open(filename, 'wb')
            self.header = header(self.file)
            self.header.write()

    def add_schema(self, schema):
        self.schemas.append(schema)
        self.header.add_schema(schema)
        self.header.write()
        self.write_schema(schema)

    def read_schema(self, index):
        schema = schema(index)
        self.file.seek(16 * (index + 1))
        schema.offset = struct.unpack('i', self.file.read(4))[0]
        schema.length = struct.unpack('i', self.file.read(4))[0]
        schema.flag1 = struct.unpack('i', self.file.read(4))[0]
        schema.flag2 = struct.unpack('i', self.file.read(4))[0]
        return schema

    def write_schema(self, schema):
        self.file.seek(16 * (schema.schemaID + 1))
        self.file.write(struct.pack('i', schema.offset))
        self.file.write(struct.pack('i', schema.length))
        self.file.write(struct.pack('i', schema.flag1))
        self.file.write(struct.pack('i', schema.flag2))
