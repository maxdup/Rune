class Schema:
    types = ['int', 'uint', 'ref', 'str']

    def __init__(self, index=None, schema=[]):
        self.schema = schema
        self.schemaID = index
        self.length = len(self.schema)
        self.offset = 0  # todo, offset of this type in the file
        self.flag1 = 0  # these flags account for 32 fields
        self.flag2 = 0
        if self.schema:
            self.flag_factory()

    def addfield(self, field):
        # todo, add possibility to add arrays of field at once
        if field in self.types:
            self.schema.append(field)
            self.length += 1
            self.flag_factory()

    def flag_factory(self):
        self.flag1 = 0
        self.flag2 = 0
        for x, fields in enumerate(self.schema):
            value = 2 ** x
            if fields == 'uint':
                self.flag2 += value
            elif fields == 'ref':
                self.flag1 += value
            elif fields == 'str':
                self.flag1 += value
                self.flag2 += value

    def type_of(self, index):
        position = 2 ** index
        flag1 = ((self.flag1 % (2 ** (index + 1))) / position) >= 1
        flag2 = ((self.flag2 % (2 ** (index + 1))) / position) >= 1
        if flag1:
            if flag2:
                return 'str'
            else:
                return 'ref'
        elif flag2:
            return 'uint'
        return 'int'

    def get_schema(self):
        schema = []
        for i in range(0, self.length):
            schema.append(self.type_of(i))
        return schema

    def set_schema(self, schema):
        self.schema = schema
        self.flag_factory()
        self.length = len(self.schema)

    def __str__(self):
        output = "schema id: " + str(self.schemaID)
        output += "\n\toffset: " + str(self.offset)
        output += "\n\tlength: " + str(self.length)
        output += "\n\tschema: " + str(self.getSchema())
        output += "\n\tflag: " + str(self.flag1) + ' ' +str(self.flag2)
        return output
