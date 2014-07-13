# python3 -m unittest test/Rune_tests.py
import unittest
import os.path

from rune.database import Database
from rune.schema import Schema


class DatabaseTest(unittest.TestCase):
    def setUp(self):
        self.filename = 'test.rune'
        self.db = Database(self.filename)

    def tearDown(self):
        if os.path.isfile(self.filename):
            os.remove(self.filename)

    def test_db_init(self):
        self.assertTrue(os.path.isfile(self.filename))

    def test_add_schema(self):
        schema1 = Schema(1)
        schema1.set_schema(['int'])
        self.db.add_schema(schema1)

    def test_read_schema(self):
        insert_schema = Schema(1)
        insert_schema.set_schema(['int'])
        self.db.add_schema(insert_schema)
        # found_schema = self.db.read_schema(1)
        # self.assertNotEqual(None, found_schema)


if __name__ == '__main__':
    unittest.main()
