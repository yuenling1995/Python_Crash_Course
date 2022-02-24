sandwich_orders = ['beef', 'turkey', 'pastrami', 'chicken', 'tuna']
finished_sandwiches = []

while sandwich_orders:
	sandwich = sandwich_orders.pop()
	print("I made your " + sandwich + " sandwich.")
	finished_sandwiches.append(sandwich)

print("\nHere's a list of sandwiches that were made: ")
for sandwich in finished_sandwiches:
	print(sandwich)

