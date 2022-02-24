sandwich_orders = ['beef', 'turkey', 'pastrami', 'chicken', 'tuna', 'pastrami', 'pastrami']
finished_sandwiches = []

print("The shop has run out of pastrami today.\n")

while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')



while sandwich_orders:
	sandwich = sandwich_orders.pop()
	print("I made your " + sandwich + " sandwich.")
	finished_sandwiches.append(sandwich)

print("\nHere's a list of sandwiches that were made: ")
for sandwich in finished_sandwiches:
	print(sandwich)