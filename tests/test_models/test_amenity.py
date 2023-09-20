#!/usr/bin/python3
"""amenity test case"""
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """Test Amenity Model"""

    def __init__(self, *args, **kwargs):
        """init method"""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """Test Amenity Model"""
        new = self.value()
        self.assertEqual(type(new.name), str)
