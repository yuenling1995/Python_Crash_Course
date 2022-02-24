def make_sandwich(*toppings):
	"""Lists what a person wants on their sandwiches"""
	print("\nHere's the summary of toppings:")
	for topping in toppings:
		print("- " + topping)


make_sandwich('beef')
make_sandwich('onion', 'peppers', 'beef', 'sausage')
