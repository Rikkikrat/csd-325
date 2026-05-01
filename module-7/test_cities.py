# Rikki Kratochvil
# Assignment: 7.2 Test Cases
# Date: 05/01/2026


import unittest
from city_functions import city_country


class CitiesTestCase(unittest.TestCase):
    """Tests for city_functions.py."""

    def test_city_country(self):
        formatted_city = city_country("santiago", "chile")
        self.assertEqual(formatted_city, "Santiago, Chile")


if __name__ == "__main__":
    unittest.main()