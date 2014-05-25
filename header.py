# -*- coding: utf-8 -*-
import struct
class header:

    def __init__(self, file):
        self.file = file
        self.nb_schemas = 0
        self.offset = 16 * (self.nb_schemas + 1)
        self.version = 1
        self.anwser = 42

    def write(self, db_file):
        db_file.seek(0)
        db_file.write(struct.pack('i', self.offset))
        db_file.write(struct.pack('i', self.nb_schemas))
        db_file.write(struct.pack('i', self.version))
        db_file.write(struct.pack('i', self.anwser))

    def add_schema(self, schema):
        schema.schemaID = self.nb_schemas
        self.nb_schemas += 1
        self.file.seek(4)
        self.file.write(struct.pack('i', self.nb_schemas))