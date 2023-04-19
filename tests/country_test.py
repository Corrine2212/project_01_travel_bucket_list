import unittest
from models.country import Country

class TestCountry(unittest.TestCase):

    def setUp(self) -> None:
        self.country = Country("Japan", False)

    def test_country_has_a_name(self):
        self.assertEqual("Japan", self.country.country_name)

    def test_can_mark_visited(self):
        self.country.mark_visited()
        self.assertEqual(True, self.country.visited)

    def test_city_has_been_visited(self):
        self.assertEqual(False, self.country.visited)