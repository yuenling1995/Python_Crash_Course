class Employee():
	"""Collect employee info and give raise."""
	def __init__(self, first, last , salary, amount=5000):
		self.first = first
		self.last = last
		self.salary = salary
		self.amount = amount

	def employee_info(self):
		full_name = self.first.title() + " " + self.last.title()
		print("For employee " + full_name)

	def give_raise(self):
		if self.amount:
			self.salary += self.amount
		else:
			self.salary += 5000
		return self.salary

