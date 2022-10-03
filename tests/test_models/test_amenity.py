#!/usr/bin/python3
"""Test module for amenity class"""
import unittest
import models.amenity
from models.amenity import Amenity
import pep8
from models import storage
from models.engine.file_storage import FileStorage


class TestAmenityDoc(unittest.TestCase):
    """Tests for documentation in amenity class"""

    def test_module_doc(self):
        """Checks for module doc"""
        self.assertGreaterEqual(len(models.amenity.__doc__), 1)

    def test_class_doc(self):
        """Checks for class doc"""
        self.assertGreaterEqual(len(Amenity.__doc__), 1)


class TestAmenityClass(unittest.TestCase):
    """Tests Amenity Class"""
    def setUp(self):
        """Setup test Amenity instances for unittesting"""
        self.Amenity_1 = Amenity()
        self.Amenity_2 = Amenity()
        Amenity_3_dict = self.Amenity_1.to_dict()
        self.Amenity_3 = Amenity(**Amenity_3_dict)

    def tearDown(self):
        """Deletes Amenity instances that were created for unittesting"""
        del self.Amenity_1
        del self.Amenity_2
        del self.Amenity_3
        storage.save()

    def test_init(self):
        """Tests proper initiation of Amenity"""
        self.assertEqual(self.Amenity_1.name, "")
        self.Amenity_1.name = "Swimming Pool"
        self.assertEqual(self.Amenity_1.name, "Swimming Pool")


class TestAmenityPep8(unittest.TestCase):
    """Tests Amenity Class for pep8 compliance"""
    def test_pep8_compliance(self):
        """Tests to ensure models/amenity.py is pep8 compliant"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/amenity.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_compliance(self):
        """Tests that tests/test_models/test_amenity.py is pep8 compliant"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["tests/test_models/test_amenity.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
