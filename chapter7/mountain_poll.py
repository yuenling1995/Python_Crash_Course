responses = {}

#set a flag to indicate that polling is active.
polling_active = True

while polling_active:
	#prompt for the person's anme and response.
	name = input("\nWhat's your name? ")
	response = input("Which mountain would you like to climb someday? ")

	#store the response in the dictionary:
	responses[name] = response

	#find out if anyone else is going to take the poll.
	repeat = input("Would you like to let another person respond? (yes/no) ")
	if repeat == 'no':
		polling_active = False

#polling is complete & now show the results.
print("\n--- Polling Results---")
for name, response in responses.items():
	print(name.title() + " would like to climb " + response + " someday.")