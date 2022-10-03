#!/usr/bin/python3
"""Test module for user class"""
import unittest
import models.user
from models.user import User
import pep8
from models import storage
from models.engine.file_storage import FileStorage


class TestUserDoc(unittest.TestCase):
    """Tests for documentation in user class"""

    def test_module_doc(self):
        """Checks for module doc"""
        self.assertGreaterEqual(len(models.user.__doc__), 1)

    def test_class_doc(self):
        """Checks for class doc"""
        self.assertGreaterEqual(len(User.__doc__), 1)


class TestUserPep8(unittest.TestCase):
    """Tests User Class for pep8 compliance"""
    def test_pep8_compliance(self):
        """Tests to ensure models/user.py is pep8 compliant"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/user.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_compliance(self):
        """Tests that tests/test_models/test_user.py is pep8 compliant"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["tests/test_models/test_user.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class TestUserClass(unittest.TestCase):
    """Tests User Class for proper initiation"""
    def setUp(self):
        """Setup test User instances for unittesting"""
        self.User_1 = User()
        self.User_2 = User()
        User_3_dict = self.User_1.to_dict()
        self.User_3 = User(**User_3_dict)

    def tearDown(self):
        """Deletes User instances that were created for unittesting"""
        del self.User_1
        del self.User_2
        del self.User_3
        storage.save()

    def test_init(self):
        """Tests proper initiation of User"""
        self.assertEqual(self.User_1.email, "")
        self.assertEqual(self.User_2.password, "")
        self.assertEqual(self.User_3.first_name, "")
        self.assertEqual(self.User_1.last_name, "")

    def test_user_update(self):
        self.User_1.email = "person.email@internet.com"
        self.User_2.password = "keep this private"
        self.User_3.first_name = "John"
        self.User_1.last_name = "Snow"
        self.assertEqual(self.User_1.email, "person.email@internet.com")
        self.assertEqual(self.User_2.password, "keep this private")
        self.assertEqual(self.User_3.first_name, "John")
        self.assertEqual(self.User_1.last_name, "Snow")
