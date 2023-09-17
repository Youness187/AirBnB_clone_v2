#!/usr/bin/python3
"""A unit test module for the console."""
import unittest
import os
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage


class TestHBNBCommand(unittest.TestCase):
    """Represents the test class for the HBNBCommand class."""

    def setUp(self):
        """Create an instance of HBNBCommand before each test"""
        self.console = HBNBCommand()

    def tearDown(self):
        """clean up after each test"""
        pass

    def test_fs_create(self):
        """Test case for the create command"""

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('create City name="Marrakech"')
            obj_id = f.getvalue().strip()
            # self.assertIsNotNone(obj_id)
            self.assertIn('City.{}'.format(obj_id), storage.all().keys())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show City {}".format(obj_id))
            self.assertIn("'name': 'Marrakech'", f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd('create User name="Anas" age=23 height=183')
            obj_id = f.getvalue().strip()
            self.assertIn('User.{}'.format(obj_id), storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd('show User {}'.format(obj_id))
            self.assertIn("'name': 'Anas'", f.getvalue().strip())
            self.assertIn("'age': 23", f.getvalue().strip())
            self.assertIn("'height': 183", f.getvalue().strip())


if __name__ == '__main__':
    unittest.main()
