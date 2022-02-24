#check if an item is in a list
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping == "green peppers":
		print("We're out of green peppers!")
	else:
		print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")


#check if a list is empty
requested_toppings = []
if requested_toppings:
	for requested_topping in requested_toppings:
		print("Adding " + requested_topping + ".")
	print("\nFinished making your pizza!")
else:
	print("\nAre you sure you want a plain pizza?\n")


#use multiple lists
available_toppings = ['mushrooms', 'olives', 'green peppers', 
					  'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print("Adding " + requested_topping + ".")
	else:
		print("Sorry we don't have " + requested_topping + ".")
print("\nFinished making your pizza!")

















