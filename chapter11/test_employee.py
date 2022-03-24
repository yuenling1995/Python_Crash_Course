import unittest
from employee import Employee

class TestEmployeeRaise(unittest.TestCase):
	"""Tests for the class Employee."""
	def setUp(self):
		"""
		create employee instance and test for default and custom raise methods.
		"""
		self.emp_yuen = Employee('yuen', 'cheng', 75000)
		self.emp_hannah = Employee('hannah', 'park', 65000, 7000)

	def test_give_default_rasie(self):
		"""test if the default raise is given properly."""
		new_salary = self.emp_yuen.give_raise()
		self.emp_yuen.employee_info()
		print("New salary is " + str(new_salary))
		self.assertEqual(new_salary, 80000)

	def test_give_custom_raise(self):
		"""test if the custom raise is given properly."""
		new_salary = self.emp_hannah.give_raise()
		self.emp_hannah.employee_info()
		print("New salary is " + str(new_salary))
		self.assertEqual(new_salary, 72000)

unittest.main()



