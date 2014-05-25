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
        db_file.write(struct.pack('i', self.rune_length))
        db_file.write(struct.pack('i', self.offset))
        db_file.write(struct.pack('i', self.flag1))
        db_file.write(struct.pack('i', self.flag2))

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

