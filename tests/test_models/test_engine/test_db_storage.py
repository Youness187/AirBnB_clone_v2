#!/usr/bin/python3
"""Database storage Testing"""
import MySQLdb
from models.engine.db_storage import DBStorage
import os
import unittest
from models.state import State
from models import storage


@unittest.skipIf(
    os.getenv("HBNB_TYPE_STORAGE") != "db",
    "Test is not relevant for DBStorage")
class test_DB_Storage(unittest.TestCase):
    """Database storage unittest"""

    def test_documentation(self):
        """documentation test"""
        self.assertIsNot(DBStorage.__doc__, None)
        
    def test_new_and_save(self):
        """Testing the new and save methods"""
        db = MySQLdb.connect(user=os.getenv('HBNB_MYSQL_USER'),
                             host=os.getenv('HBNB_MYSQL_HOST'),
                             passwd=os.getenv('HBNB_MYSQL_PWD'),
                             port=3306,
                             db=os.getenv('HBNB_MYSQL_DB'))
        new_state = State(**{'name': 'California'})
        cur = db.cursor()
        cur.execute('SELECT COUNT(*) FROM states:')
        old_count = cur.fetchall()
        cur.close()
        db.close()
        new_state.save()
        db = MySQLdb.connect(user=os.getenv('HBNB_MYSQL_USER'),
                             host=os.getenv('HBNB_MYSQL_HOST'),
                             passwd=os.getenv('HBNB_MYSQL_PWD'),
                             port=3306,
                             db=os.getenv('HBNB_MYSQL_DB'))
        cur = db.cursor()
        cur.execute('SELECT COUNT(*) FROM states;')
        new_count = cur.fetchall()
        self.assertEqual(new_count[0][0], old_count[0][0] + 1)
        cur.close()
        db.close()
        
    def test_new(self):
        """ New object is correctly added to database """
        new = State(name='California')
        self.assertFalse(new in storage.all().values())
        new.save()
        self.assertTrue(new in storage.all().values())
        dbc = MySQLdb.connect(
            host=os.getenv('HBNB_MYSQL_HOST'),
            port=3306,
            user=os.getenv('HBNB_MYSQL_USER'),
            passwd=os.getenv('HBNB_MYSQL_PWD'),
            db=os.getenv('HBNB_MYSQL_DB')
        )
        cursor = dbc.cursor()
        cursor.execute('SELECT * FROM states WHERE id="{}"'.format(new.id))
        result = cursor.fetchone()
        self.assertTrue(result is not None)
        self.assertIn('California', result)
        cursor.close()
        dbc.close()
