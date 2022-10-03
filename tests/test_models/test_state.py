#!/usr/bin/python3
"""Test module for state class"""
import unittest
import models.state
from models.state import State
import pep8
from models import storage
from models.engine.file_storage import FileStorage


class TestStateDoc(unittest.TestCase):
    """Tests for documentation in state class"""

    def test_module_doc(self):
        """Checks for module doc"""
        self.assertGreaterEqual(len(models.state.__doc__), 1)

    def test_class_doc(self):
        """Checks for class doc"""
        self.assertGreaterEqual(len(State.__doc__), 1)


class TestStatePep8(unittest.TestCase):
    """Tests state Class for pep8 compliance"""

    def test_pep8_compliance(self):
        """Tests to ensure models/state.py is pep8 compliant"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/state.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_compliance(self):
        """Tests to ensure tests/test_models/test_state.py is pep8 compliant"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["tests/test_models/test_state.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class TestStateClass(unittest.TestCase):
    """Tests State Class"""
    def setUp(self):
        """Setup test State instances for unittesting"""
        self.State_1 = State()
        self.State_2 = State()
        State_3_dict = self.State_1.to_dict()
        self.State_3 = State(**State_3_dict)

    def tearDown(self):
        """Deletes State instances that were created for unittesting"""
        del self.State_1
        del self.State_2
        del self.State_3
        storage.save()

    def test_init(self):
        """Tests proper initiation of State"""
        self.assertEqual(self.State_1.name, "")
        self.assertEqual(self.State_2.name, "")

    def test_state_update(self):
        """Tests updates to State are correct"""
        self.State_1.name = "Oklahoma"
        self.assertEqual(self.State_1.name, "Oklahoma")
