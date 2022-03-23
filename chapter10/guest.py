filename = 'guest.txt'

with open(filename, 'w') as file_object:
	name = input("What's your name?")
	file_object.write(name)