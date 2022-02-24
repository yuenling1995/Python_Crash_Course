prompt = "Please tell me what kind of pizza toppings do you want: "
prompt += "\nEnter quit when you are finished. "

while True:
	message = input(prompt)

	if message == "quit":
		break
	else:
		print("I'll add " + message + " to your pizza.")


#another way
active = True

while active:
	message = input(prompt)

	if message == "quit":
		active = False
	else:
		print("I'll add " + message + " to your pizza.")


