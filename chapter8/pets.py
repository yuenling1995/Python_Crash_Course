def describe_pet(animal_type, pet_name = 'lyon'):
	"""Display information about a pet."""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name + ".")

#describe_pet('hamster', 'harry')
#describe_pet('cat', 'lyon')
#describe_pet(animal_type = 'cat', pet_name = 'bubbles')
describe_pet('cat')