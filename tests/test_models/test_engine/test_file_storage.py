#!/usr/bin/python3
import models
from models import storage
from models.base_model import BaseModel
from models.engine import file_storage
from models.engine.file_storage import FileStorage
import unittest
import json
import pep8
import os


class TestFileStorageDoc(unittest.TestCase):
    """Contains tests for documentation in base_model"""
    def test_module_doc(self):
        """Checks for documentation in file_storage module"""
        self.assertGreaterEqual(len(file_storage.__doc__), 1)

    def test_class_doc(self):
        """Checks for documentation in FileStorage"""
        self.assertGreaterEqual(len(FileStorage.__doc__), 1)

    def test_all(self):
        """Checks for documentation of the all method"""
        self.assertGreaterEqual(len(FileStorage.all.__doc__), 1)

    def test_new(self):
        """Checks for documentation of the new method"""
        self.assertGreaterEqual(len(FileStorage.new.__doc__), 1)

    def test_save(self):
        """Checks for documentation of the all method"""
        self.assertGreaterEqual(len(FileStorage.save.__doc__), 1)

    def test_reload(self):
        """Checks for documentation of the all method"""
        self.assertGreaterEqual(len(FileStorage.reload.__doc__), 1)


class TestBaseModelPep8(unittest.TestCase):
    """Tests BaseModel Class for pep8 compliance"""

    def test_pep8_compliance(self):
        """Tests to ensure models/amenity.py is pep8 compliant"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/engine/file_storage.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_compliance(self):
        """Tests to ensure tests/test_models/base_model.py is pep8 compliant"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files([("tests/test_models/"
                                        "test_engine/test_file_storage.py")])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class TestFileStorage(unittest.TestCase):
    """Tests FilesStorage"""
    def setUp(self):
        self.obj1 = BaseModel()
        self.storage = FileStorage()
        self.storage.save()

    def tearDown(self):
        """tearDown method"""
        del self.obj1
        del self.storage
        os.remove("file.json")

    def test_all(self):
        my_dict = self.storage.all()
        self.assertIsInstance(my_dict, dict)
        self.assertIn(self.obj1, my_dict.values())

    def test_new(self):
        new_obj = BaseModel()
        self.storage.new(new_obj)
        my_dict = self.storage.all()
        self.assertIn(new_obj, my_dict.values())

    def test_save(self):
        self.assertTrue(os.path.exists("file.json"))
        with open("file.json", 'r') as file:
            file_contents = file.read()
        self.assertTrue(len(file_contents) > 0)
        self.assertIn(f"{self.obj1.__class__.__name__}.{self.obj1.id}",
                      file_contents)

    def test_reload(self):
        self.storage.destroy_all()
        self.assertEqual(self.storage.all(), {})
        self.assertTrue(len(self.storage.all()) == 0)
        self.storage.reload()
        self.assertIn(f"{self.obj1.__class__.__name__}.{self.obj1.id}",
                      self.storage.all().keys())


if __name__ == '__main__':
    unittest.main()
