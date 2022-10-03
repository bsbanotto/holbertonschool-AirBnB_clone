#!/usr/bin/python3
"""Module contains unit tests for the BaseModel class"""
from models import base_model
from models import storage
from models.base_model import BaseModel
import unittest
import os
from datetime import datetime, time
import pep8


class TestBaseModelDoc(unittest.TestCase):
    """Contains tests for documentation in base_model"""

    def test_module_doc(self):
        """Checks for documentation in base_model module"""
        self.assertGreaterEqual(len(base_model.__doc__), 1)

    def test_class_doc(self):
        """Checks for documentation in BaseClass"""
        self.assertGreaterEqual(len(BaseModel.__doc__), 1)

    def test_init_doc(self):
        """Checks for documentation of __init__ method"""
        self.assertGreaterEqual(len(BaseModel.__init__.__doc__), 1)

    def test_str_doc(self):
        """Checks for documentation of __str__ method"""
        self.assertGreaterEqual(len(BaseModel.__str__.__doc__), 1)

    def test_save_doc(self):
        """Checks for documentation of save() method"""
        self.assertGreaterEqual(len(BaseModel.save.__doc__), 1)

    def test_to_dict_doc(self):
        """Checks for documentation of to_dict() method"""
        self.assertGreaterEqual(len(BaseModel.to_dict.__doc__), 1)


class TestBaseModelPep8(unittest.TestCase):
    """Tests BaseModel Class for pep8 compliance"""

    def test_pep8_compliance(self):
        """Tests to ensure models/amenity.py is pep8 compliant"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/base-model.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_compliance(self):
        """Tests to ensure tests/test_models/base_model.py is pep8 compliant"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["tests/test_models\
                                       /test_base_model.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class TestBaseModel(unittest.TestCase):
    """Checks creating model"""

    def setUp(self):
        """setUp method"""
        self.obj1 = BaseModel()
        self.obj1.save()

    def tearDown(self):
        """tearDown method"""
        del self.obj1
        os.remove("file.json")

    def test_normal(self):
        """Checks that an object is created"""
        self.assertIsNotNone(self.obj1)


class TestBaseModelAttributes(unittest.TestCase):
    """Checks attributes in BaseModel"""

    def setUp(self):
        """setUp method"""
        self.obj1 = BaseModel()
        self.obj1.save()

    def tearDown(self):
        """tearDown method"""
        del self.obj1
        os.remove("file.json")

    def test_id(self):
        """Checks BaseModel.id"""
        self.assertIsNotNone(self.obj1.id)
        self.obj1.id = 5
        self.assertEqual(self.obj1.id, 5)

    def test_created_at_format(self):
        """Checks that created_at is ISO format"""
        self.assertTrue(self.obj1.created_at.fromisoformat(
            str(self.obj1.created_at)))

    def test_created_at_format(self):
        """Checks that updated_at is ISO format"""
        self.assertTrue(self.obj1.updated_at.fromisoformat(
            str(self.obj1.updated_at)))

    def test_new_attributes(self):
        """Checks added attributes"""
        self.obj1.name = "My First Model"
        self.obj1.my_number = 89
        self.assertEqual(self.obj1.name, "My First Model")
        self.assertEqual(self.obj1.my_number, 89)


class TestBaseModelCreateTwo(unittest.TestCase):

    def setUp(self):
        """setUp method"""
        self.bm1 = BaseModel()
        self.bm2 = BaseModel()
        self.bm1.save()
        self.bm2.save()

    def tearDown(self):
        """tearDown method"""
        del self.bm1
        del self.bm2
        os.remove("file.json")

    def test_create_two(self):
        """Checks proper function when creating two BaseModels"""
        self.assertIsInstance(self.bm1, BaseModel)
        self.assertIsInstance(self.bm1, BaseModel)
        self.assertTrue(hasattr(self.bm1, "id"))
        self.assertTrue(hasattr(self.bm1, "created_at"))
        self.assertTrue(hasattr(self.bm1, "updated_at"))
        self.assertTrue(hasattr(self.bm1, "id"))
        self.assertTrue(hasattr(self.bm1, "created_at"))
        self.assertTrue(hasattr(self.bm1, "updated_at"))
        self.assertNotEqual(self.bm1.id, self.bm2.id)
        self.assertNotEqual(self.bm1.created_at, self.bm2.created_at)
        self.assertNotEqual(self.bm1.updated_at, self.bm2.updated_at)
        self.assertIsInstance(self.bm1.id, str)
        self.assertIsInstance(self.bm1.created_at, object)
        self.assertIsInstance(self.bm1.updated_at, object)
        self.assertIsInstance(self.bm2.id, str)
        self.assertIsInstance(self.bm2.created_at, object)
        self.assertIsInstance(self.bm2.updated_at, object)


class TestBaseModelMethods(unittest.TestCase):
    """Checks methods implemented in BaseModel"""

    def setUp(self):
        """setUp method"""
        self.obj1 = BaseModel()
        self.obj1.save()

    def tearDown(self):
        """tearDown method"""
        del self.obj1
        os.remove("file.json")

    def test_save(self):
        """Checks save method"""
        self.obj1.save()
        self.assertNotEqual(self.obj1.created_at, self.obj1.updated_at)

    def test__str__(self):
        """Checks __str__() method"""
        self.assertEqual(self.obj1.__str__(), (
                            f"[{self.obj1.__class__.__name__}] "
                            f"({self.obj1.id}) {self.obj1.__dict__}"))

    def test_to_dict(self):
        """Checks to_dict() method"""
        my_dict = self.obj1.to_dict()
        self.assertIsInstance(my_dict, dict)
        self.assertIsInstance(my_dict["created_at"], str)

    def test_create(self):
        obj2 = BaseModel(hello=0)
        self.assertEqual(getattr(obj2, "hello"), 0)
        del obj2


if __name__ == '__main__':
    unittest.main()
