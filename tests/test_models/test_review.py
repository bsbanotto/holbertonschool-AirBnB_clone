#!/usr/bin/python3
"""Test module for review class"""
import unittest
import models.review
from models.review import Review
import pep8
from models import storage
from models.engine.file_storage import FileStorage


class TestAmenityDoc(unittest.TestCase):
    """Tests for documentation in review class"""

    def test_module_doc(self):
        """Checks for module doc"""
        self.assertGreaterEqual(len(models.review.__doc__), 1)

    def test_class_doc(self):
        """Checks for class doc"""
        self.assertGreaterEqual(len(Review.__doc__), 1)


class TestReviewPep8(unittest.TestCase):
    """Tests Review Class for pep8 compliance"""

    def test_pep8_compliance(self):
        """Tests to ensure models/review.py is pep8 compliant"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/review.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_compliance(self):
        """Test to ensure tests/test_models/test_review.py is pep8 compliant"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["tests/test_models/test_review.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class TestReviewClass(unittest.TestCase):
    """Tests Review Class"""

    def setUp(self):
        """Setup test Review instances for unittesting"""
        self.Review_1 = Review()
        self.Review_2 = Review()
        Review_3_dict = self.Review_1.to_dict()
        self.Review_3 = Review(**Review_3_dict)

    def tearDown(self):
        """Deletes Amenigy instances that were created for testing"""
        del self.Review_1
        del self.Review_2
        del self.Review_3
        storage.save()

    def test_init(self):
        """Tests proper initiation and update of Review"""
        self.assertEqual(self.Review_1.place_id, "")
        self.assertEqual(self.Review_2.user_id, "")
        self.assertEqual(self.Review_3.text, "")

    def test_review_update(self):
        self.Review_1.place_id = "Review 1 ID"
        self.Review_2.user_id = "Johnny"
        self.Review_3.text = "Review 3 text"
        self.assertEqual(self.Review_1.place_id, "Review 1 ID")
        self.assertEqual(self.Review_2.user_id, "Johnny")
        self.assertEqual(self.Review_3.text, "Review 3 text")
