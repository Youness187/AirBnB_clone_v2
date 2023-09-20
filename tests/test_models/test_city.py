#!/usr/bin/python3
"""City Model Unittests"""
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """Test City Model"""

    def __init__(self, *args, **kwargs):
        """init method"""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """state id test"""
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """name test"""
        new = self.value()
        self.assertEqual(type(new.name), str)
