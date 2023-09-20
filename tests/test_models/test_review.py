#!/usr/bin/python3
"""Review Model Unit tests"""
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """Test Review Model"""

    def __init__(self, *args, **kwargs):
        """init method"""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """place id test"""
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """user id test"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """text test"""
        new = self.value()
        self.assertEqual(type(new.text), str)
