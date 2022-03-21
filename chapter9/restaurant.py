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


#new_restaurant = Restaurant('hong kong street', 'asian')
#new_restaurant.describe_restaurant()
#new_restaurant.open_restaurant()
#print(new_restaurant.restaurant_name)
#print(new_restaurant.cuisine_type)

#old_restaurant = Restaurant('taco bell', 'mexican')
#old_restaurant.describe_restaurant()
#old_restaurant.open_restaurant()
#print(old_restaurant.restaurant_name)
#print(old_restaurant.cuisine_type)

#restaurant = Restaurant('mcdonalds', 'fast')
#print(restaurant.number_served)
#restaurant.number_served = 8
#print(restaurant.number_served)
#restaurant.set_number_served(10)
#print(restaurant.number_served)
#restaurant.increment_number_served(12)
#print(restaurant.number_served)



