#!/usr/bin/python3
"""Place Model Unit tests"""
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """Test Plase Model"""

    def __init__(self, *args, **kwargs):
        """init method"""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """city_id test"""
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """user_id test"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """name test"""
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """description test"""
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """rooms numbers"""
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """bathrooms number test"""
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """max guest test"""
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """price_by_night test"""
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """latitude test"""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """longitude test"""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """amenity_ids test"""
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
