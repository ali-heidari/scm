
import unittest
import subprocess
import sys
sys.path.insert(1, './src')
from component import *
from setup import Setup


class MySQLTest(unittest.TestCase):
    def test_create_database(self):
        mysql_instance = mysql.MySQL(" ")
        self.assertTrue(mysql_instance.create_database("ali", "123", "test_db"))



if __name__ == "__main__":
    unittest.main()
