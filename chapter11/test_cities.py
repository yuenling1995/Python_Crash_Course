import unittest
from city_functions import city_country

class TestCityFunction(unittest.TestCase):
	"""test for 'test_functions.py'."""
	def test_city_country(self):
		string = city_country('santiago', 'chile')
		self.assertEqual(string, 'Santiago, Chile')

	def test_city_country_population(self):
		string = city_country('santiago', 'chile', 5000000)
		self.assertEqual(string, 'Santiago, Chile - population 5000000')

unittest.main()