#!/usr/bin/python3
"""Test module for place class"""
import unittest
import models.place
from models.place import Place
import pep8
from models import storage
from models.engine.file_storage import FileStorage


class TestAmenityDoc(unittest.TestCase):
    """Tests for documentation in place class"""

    def test_module_doc(self):
        """Checks for module doc"""
        self.assertGreaterEqual(len(models.place.__doc__), 1)

    def test_class_doc(self):
        """Checks for class doc"""
        self.assertGreaterEqual(len(Place.__doc__), 1)


class TestPlacepep8(unittest.TestCase):
    """Tests Place Class for pep8 compliance"""

    def test_pep8_compliance(self):
        """Tests to ensure models/place.py is pep8 compliant"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/place.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_compliance(self):
        """Tests to ensure tests/test_models/test_place.py is pep8 compliant"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["tests/test_models/test_place.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class testPlaceClass(unittest.TestCase):
    """Tests Place Class"""

    def setUp(self):
        """Setup test Place instances for unittesting"""
        self.Place_1 = Place()
        self.Place_2 = Place()
        Place_3_dict = self.Place_1.to_dict()
        self.Place_3 = Place(**Place_3_dict)

    def tearDown(self):
        """Deletes Place instances that were created for unittesting"""
        del self.Place_1
        del self.Place_2
        del self.Place_3
        storage.save()

    def test_init(self):
        """Tests proper initiation of Place"""
        self.assertEqual(self.Place_1.city_id, "")
        self.assertEqual(self.Place_1.user_id, "")
        self.assertEqual(self.Place_1.name, "")
        self.assertEqual(self.Place_1.description, "")
        self.assertEqual(self.Place_2.number_bathrooms, 0)
        self.assertEqual(self.Place_2.max_guest, 0)
        self.assertEqual(self.Place_2.price_by_night, 0)
        self.assertEqual(self.Place_2.latitude, 0)
        self.assertEqual(self.Place_2.longitude, 0)
        self.assertEqual(self.Place_2.number_rooms, 0)
        self.assertEqual(self.Place_2.amenity_ids, [])

    def test_update_place(self):
        """Tests proper update of attribute values"""
        self.Place_1.city_id = "Tulsa"
        self.Place_2.user_id = "Johnny"
        self.Place_1.name = "Home"
        self.Place_2.number_rooms = 4
        self.Place_1.number_bathrooms = 3
        self.assertEqual(self.Place_1.city_id, "Tulsa")
        self.assertEqual(self.Place_2.user_id, "Johnny")
        self.assertEqual(self.Place_1.name, "Home")
        self.assertEqual(self.Place_2.number_rooms, 4)
        self.assertEqual(self.Place_1.number_bathrooms, 3)
