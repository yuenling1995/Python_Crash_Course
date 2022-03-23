message = "What's your name? "
message += "Enter 'q' to quit.\n"
filename = "guest_book.txt"

while True:
	name = input(message)
	if name.lower() == 'q':
		break
	else:
		print("Welcome " + name.title())
		with open(filename, 'a') as file_object:
			file_object.write(name.title() + "\n")