# -*- coding: utf-8 -*-
import struct
from schema import schema


class header:

    def __init__(self, file):
        self.file = file
        self.nb_schemas = 0
        self.offset = 16 * (self.nb_schemas + 1)
        self.version = 1
        self.anwser = 42
        self.schemas = []

    def write(self):
        self.file.seek(0)
        self.file.write(struct.pack('i', self.offset))
        self.file.write(struct.pack('i', self.nb_schemas))
        self.file.write(struct.pack('i', self.version))
        self.file.write(struct.pack('i', self.anwser))

    def read(self):
        self.file.seek(0)
        self.offset = struct.unpack('i', self.file.read(4))[0]
        self.nb_schemas = struct.unpack('i', self.file.read(4))[0]
        self.version = struct.unpack('i', self.file.read(4))[0]
        self.anwser = struct.unpack('i', self.file.read(4))[0]

        for x in range(0, self.nb_schemas):
            schm = schema([])
            schm.read(db_file)
            self.schemas.append(schm)

    def add_schema(self, schema):
        schema.schemaID = self.nb_schemas
        self.nb_schemas += 1
        self.file.seek(4)
        self.file.write(struct.pack('i', self.nb_schemas))

    def print_schemas(self):
        for schema in self.schemas:
            print(str(schema))
        return
 
    def __str__(self):
        output = 'schema count: ' + str(self.nb_schemas)
        output += '\nfile offset: ' + str(self.offset)
        output += '\ndb version: ' + str(self.version)
        output += '\nanwser: ' + str(self.anwser)
        return output
