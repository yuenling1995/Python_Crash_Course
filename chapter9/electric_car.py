from car import Car 

class Battery():
	"""A simple attempt to model a battery for an electric car."""

	def __init__(self, battery_size=70):
		"""Initialize the battery's attributes."""
		self.battery_size = battery_size

	def describe_battery(self):
		"""Print a statement describing the battery size."""
		print("This car has a " + str(self.battery_size) + "-kwh battery.")

	def get_range(self):
		"""Print a statement about the range this battery provides."""
		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 85:
			range = 270

		message = "This car can go approximately " + str(range)
		message += " miles on a full range."
		print(message)

	def update_battery(self):
		if self.battery_size < 85:
			self.battery_size = 85


class ElectricCar(Car):
	"""Represent aspects of a car, specific to electric vehicles."""
	def __init__(self, make, model, year):
		"""Initialize atrributes of the parent class."""
		super().__init__(make, model, year)
		self.battery = Battery()




#my_tesla = ElectricCar('tesla', 'model s', 2016)
#print(my_tesla.get_descriptive_name())
#my_tesla.battery.describe_battery()
#my_tesla.battery.get_range()
#my_tesla.battery.update_battery()
#my_tesla.battery.get_range()







