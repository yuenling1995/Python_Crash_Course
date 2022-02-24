#store information about a pizza being ordered
pizzas = {
	'crust': 'thick',
	'toppings': ['mushroom', 'extra cheease', 'sausage'],
}

#summarize the order
print("You ordered a " + pizzas['crust'] + "-crust pizza" +
	  "with the following toppings:")

for topping in pizzas['toppings']:
	print("\t" + topping)