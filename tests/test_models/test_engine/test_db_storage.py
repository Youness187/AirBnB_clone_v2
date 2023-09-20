#!/usr/bin/python3
"""Database storage Testing"""
from models.engine.db_storage import DBStorage
import os
import unittest
import pep8


@unittest.skipIf(
    os.getenv("HBNB_TYPE_STORAGE") != "db",
    "Test is not relevant for DBStorage")
class test_DB_Storage(unittest.TestCase):
    """Database storage unittest"""

    def test_pep8_conformance_db_storage(self):
        """Test that models/engine/db_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(["models/engine/db_storage.py"])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings)."
        )
