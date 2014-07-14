# -*- coding: utf-8 -*-
import struct


class Header:

    def __init__(self, file):
        self.file = file
        self.nb_schemas = 0
        self.offset = 16 * (self.nb_schemas + 1)
        self.version = 1
        self.answer = 42
        self.schemas = []

    def write(self):
        self.file.seek(0)
        self.file.write(struct.pack('i', self.offset))
        self.file.write(struct.pack('i', self.nb_schemas))
        self.file.write(struct.pack('i', self.version))
        self.file.write(struct.pack('i', self.answer))

    def read(self):
        self.file.seek(0)
        self.offset = struct.unpack('i', self.file.read(4))[0]
        self.nb_schemas = struct.unpack('i', self.file.read(4))[0]
        self.version = struct.unpack('i', self.file.read(4))[0]
        self.anwser = struct.unpack('i', self.file.read(4))[0]
    def add_schema(self, schema):
        schema.schemaID = self.nb_schemas
        self.nb_schemas += 1
        self.offset += 16
        self.file.seek(4)
        self.file.write(struct.pack('i', self.nb_schemas))
 
    def __str__(self):
        output = 'schema count: ' + str(self.nb_schemas)
        output += '\nfile offset: ' + str(self.offset)
        output += '\ndb version: ' + str(self.version)
        output += '\nanswer: ' + str(self.answer)
        return output
