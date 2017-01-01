import unittest

from powerball_python.models import PowerBallEntrant, InvalidChoiceException


class EntrantTestCase(unittest.TestCase):

    def setUp(self):
        self.entrant = self._entrant_factory()

    @staticmethod
    def _entrant_factory():
        return PowerBallEntrant(first_name="Jeff", last_name="Palladino")

    def test_create_entrant(self):
        """Test entrant was created with given first and last name"""
        self.assertEqual(self.entrant.first_name, "Jeff")
        self.assertEqual(self.entrant.last_name, "Palladino")

    def test_set_favorite_number(self):
        """Test setting favorite number"""
        self.entrant.set_favorite_number(4)
        self.assertListEqual([4], self.entrant.favorite_numbers)

        self.entrant.set_favorite_number(5)
        self.assertListEqual([4, 5], self.entrant.favorite_numbers)

    def test_set_invalid_favorite_number(self):
        """Test setting a invalid choice raises a InvalidChoiceException or a ValueError"""

        with self.assertRaises(ValueError):
            # Test non numeric characters raise
            self.entrant.set_favorite_number("Hello")

        with self.assertRaises(InvalidChoiceException):
            # Test numbers not in acceptable pool raise
            self.entrant.set_favorite_number(100)

    def test_set_powerball_number(self):
        """Test setting powerball number"""
        self.entrant.set_powerball(10)
        self.assertEqual(10, self.entrant.powerball_number)

        self.entrant.set_powerball(12)
        self.assertEqual(12, self.entrant.powerball_number)

    def test_set_invalid_powerball(self):
        """Test setting a invalid choice raises a InvalidChoiceException or a ValueError"""
        with self.assertRaises(ValueError):
            # Test non numeric characters raise
            self.entrant.set_powerball("Hello")

        with self.assertRaises(InvalidChoiceException):
            # Test numbers not in acceptable pool raise
            self.entrant.set_powerball(100)

    def test_number_pool(self):
        """Test number pool for each entrant is unique"""

        # test numbers are removed from the pool as they are selected
        self.assertTrue(1 in self.entrant.number_pool)
        self.entrant.set_favorite_number(1)
        self.assertFalse(1 in self.entrant.number_pool)

        # given a new entrant, test their number pool contains 1
        new_entrant = PowerBallEntrant(first_name="test", last_name="test")
        self.assertTrue(1 in new_entrant.number_pool)