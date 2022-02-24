


while True:
	age = input("What's your age? ")
	age = int(age)
	prompt = input("Enter 'quit' to exit the program: ")	

	if prompt == 'quit':
		break

	if age < 3:
		print("Your ticket is free!")
	elif age < 12:
		print("Your ticket is $10.")
	else:
		print("Your ticket is $15.")



