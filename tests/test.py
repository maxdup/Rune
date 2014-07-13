#python3 -m unittest test/Rune_tests.py
import unittest
from rune.database import database 
import os.path
from rune.schema import schema


class Rune_tests(unittest.TestCase):
    def setUp(self):
        self.filename = 'test.rune'
        db = database(self.filename)
    def tearDown(self):
        if os.path.isfile(self.filename):
            os.remove(self.filename)
    def testMethod(self):
        self.assertEqual(3, 1+2)
    def testMethod2(self):
        self.assertEqual(3, 2+1)
    def testMethod3(self):
        self.assertEqual(3, 2+1)
    def test_db_init(self):
        self.assertTrue(os.path.isfile(self.filename))
if __name__ == '__main__':
    unittest.main()