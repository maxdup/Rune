import struct


class schema:

    '''schemas are capped to 32 fields for now'''

    def __init__(self, schema):
        self.schema = schema
        self.schemaID = 0  # todo autoincrement
        self.rune_length = len(self.schema)
        self.offset = 0  # todo, offset of this type in the file
        self.flag1 = 0  # these flags account for 32 fields
        self.flag2 = 0
        self.flag_factory()

    def write(self, db_file):
        db_file.seek(16 * (self.schemaID + 1))
        db_file.write(struct.pack('i', self.offset))
        db_file.write(struct.pack('i', self.rune_length))
        db_file.write(struct.pack('i', self.flag1))
        db_file.write(struct.pack('i', self.flag2))

    def read(self, db_file):
        self.offset = struct.unpack('i', db_file.read(4))[0]
        self.rune_length = struct.unpack('i', db_file.read(4))[0]
        self.flag1 = struct.unpack('i', db_file.read(4))[0]
        self.flag2 = struct.unpack('i', db_file.read(4))[0]


    def flag_factory(self):
        for x, fields in enumerate(self.schema):
            value = 2 ** x
            if fields == 'uint':
                self.flag2 += value
            elif fields == 'ref':
                self.flag1 += value
            elif fields == 'str':
                self.flag1 += value
                self.flag2 += value

    def typeOf(self, index):
        position = 2 ** index
        flag1 = self.flag1 / position >= 1
        flag2 = self.flag2 / position >= 1
        if flag1:
            if flag2:
                return 'str'
            else:
                return 'ref'
        elif flag2:
            return 'uint'
        return 'int'

    def getSchema(self):
        schm = []
        for i in range(0, self.rune_length):
           schm.append(self.typeOf(i))
        return schm

    def __str__(self):
        output = "schema id: " + str(self.schemaID)
        output += "\n\toffset: " + str(self.offset)
        output += "\n\tlength: " + str(self.rune_length)
        output += "\n\tschema: " + str(self.getSchema())
        return output
