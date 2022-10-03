#!/usr/bin/python3
"""Test module for city class"""
import unittest
import models.city
from models.city import City
import pep8
from models import storage
from models.engine.file_storage import FileStorage


class TestAmenityDoc(unittest.TestCase):
    """Tests for documentation in city class"""

    def test_module_doc(self):
        """Checks for module doc"""
        self.assertGreaterEqual(len(models.city.__doc__), 1)

    def test_class_doc(self):
        """Checks for class doc"""
        self.assertGreaterEqual(len(City.__doc__), 1)


class TestCityClass(unittest.TestCase):
    """Tests City Class"""

    def setUp(self):
        """Setup test City instances for unittesting"""
        self.City_1 = City()
        self.City_2 = City()
        City_3_dict = self.City_1.to_dict()
        self.City_3 = City(**City_3_dict)

    def tearDown(self):
        """Deletes City instances that were created"""
        del self.City_1
        del self.City_2
        del self.City_3
        storage.save()

    def test_init(self):
        """Tests proper initiation of Amenity"""
        self.assertEqual(self.City_1.name, "")
        self.assertEqual(self.City_2.state_id, "")
        self.City_1.name = "Tulsa"
        self.assertEqual(self.City_1.name, "Tulsa")
        self.City_2.state_id = "Oklahoma"
        self.assertEqual(self.City_2.state_id, "Oklahoma")


class TestCityPep8(unittest.TestCase):
    """Tests Amenity Class for pep8 compliance"""

    def test_pep8_compliance(self):
        """Tests to ensure models/amenity.py is pep8 compliant"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/city.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_compliance(self):
        """Tests to ensure tests/test_models/amenity.py is pep8 compliant"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["tests/test_models/test_city.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
