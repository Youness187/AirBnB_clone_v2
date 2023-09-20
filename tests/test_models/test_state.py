#!/usr/bin/python3
"""State Model Unit tests"""
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """Test State Model"""

    def __init__(self, *args, **kwargs):
        """init method"""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """test State"""
        new = self.value()
        self.assertEqual(type(new.name), str)
