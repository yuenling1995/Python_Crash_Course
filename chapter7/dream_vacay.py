prompt = "If you could visit one place in the world, where would you go? "
prompt += "Enter 'quit' to exit the program and see the results: "
place = []
active = True

while active:
	message = input(prompt)

	if message == "quit":
		active = False
	else:
		place.append(message)


#now print the results
print("Here's a list of places you would love to go someday: ")
for location in place:
	print(location)




