#python3 -m unittest test/Rune_tests.py
import unittest
import os.path

from rune.database import database
from rune.schema import schema


class Rune_tests(unittest.TestCase):
    def setUp(self):
        self.filename = 'test.rune'
        self.db = database(self.filename)
    def tearDown(self):
        if os.path.isfile(self.filename):
            os.remove(self.filename)
    def test_db_init(self):
        self.assertTrue(os.path.isfile(self.filename))

    def test_add_schema(self):
        schema1 = schema(1)
        schema1.setSchema(['int'])
        self.db.add_schema(schema1)
        self.assertEqual(1, len(self.db.schemas))


if __name__ == '__main__':
    unittest.main()
