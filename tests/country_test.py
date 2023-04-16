import unittest
from models.country import Country

class TestCountry(unittest.TestCase):

    def setUp(self) -> None:
        self.country = Country("Japan")

    def test_country_has_a_name(self):
        self.assertEqual("Japan", self.country.country_name)