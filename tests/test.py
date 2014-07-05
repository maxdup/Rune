#python3 -m unittest test/Rune_tests.py
import unittest
from rune.database import database 
import os.path


class Rune_tests(unittest.TestCase):

    def testMethod(self):
        self.assertEqual(3, 1+2)
    def testMethod2(self):
        self.assertEqual(3, 2+1)
    def testMethod3(self):
        self.assertEqual(3, 2+1)

    def test_db_init(self):
        filename = 'test.rune'
        db = database(filename)
        self.assertTrue(os.path.isfile(filename))

if __name__ == '__main__':
    unittest.main()
