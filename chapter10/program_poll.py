message = "Why do you like programming? "
message += "Enter 'q' to quit:\n"
filename = "program_poll.txt"

while True:
	reason = input(message)
	if reason.lower() == 'q':
		break
	else:
		with open(filename, 'a') as file_object:
			file_object.write(reason + "\n")

