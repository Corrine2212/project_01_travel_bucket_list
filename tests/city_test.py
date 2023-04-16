import unittest
from models.city import City

class TestCity(unittest.TestCase):

    def setUp(self):
        self.city = City("Tokyo", False)

    def test_city_has_a_name(self):
        self.assertEqual("Tokyo", self.city.city_name)

    def test_can_mark_visited(self):
        self.city.mark_visited()
        self.assertEqual(True, self.city.visited)

    def test_city_has_been_visited(self):
        self.assertEqual(False, self.city.visited)