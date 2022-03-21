class Restaurant():
	"""print brief info about a restaurant."""

	def __init__(self, restaurant_name, cuisine_type):
		"""Initialize name and type attributes."""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		print("The restaurant name: " + self.restaurant_name.title())
		print("They serve " + self.cuisine_type.title() + " food.")

	def open_restaurant(self):
		print("This restaurant is open!\n")

	def set_number_served(self, num):
		"""set the number of served customers."""
		self.number_served = num

	def increment_number_served(self, number):
		"""increment the num of served customers."""
		self.number_served += number



class IceCreamStand(Restaurant):
	"""a simple attempt to introduce the ice cream stand."""

	def __init__(self, restaurant_name, cuisine_type):
		super().__init__(restaurant_name, cuisine_type)
		self.flavors = ['chocolate', 'rasberry', 'vanilla', 'peanut butter', 'caramel']

	def display_flavors(self):
		print("Here's a list of available flavors:")
		for flavor in self.flavors:
			print(flavor)


ice_cream = IceCreamStand("yuen's stand", 'fro-yo')
ice_cream.describe_restaurant()
ice_cream.open_restaurant()
ice_cream.set_number_served(8)
print(ice_cream.number_served)

ice_cream.display_flavors()











