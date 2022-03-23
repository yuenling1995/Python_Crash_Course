import json

def get_stored_username():
	"""store the username in a file."""
	filename = 'username.json'
	try:
		with open(filename) as file_obj:
			username = json.load(file_obj)
	except FileNotFoundError:
		return None 
	else:
		return username 


def get_new_username():
	"""Prompt for a new name."""
	username = input("What is your name? ")
	filename = 'username.json'
	with open(filename, 'w') as file_obj:
		json.dump(username, file_obj)
	return username


def greet_user():
	"""Greet the user by name."""
	username = get_stored_username()
	if username:
		confirm = input("Is " + username + " the correct username? Enter 'y' or 'n': ")
		if confirm.lower() == 'y':
			print("Welcome back, " + username + "!")
		else:
			username = get_new_username()
			print("We will remember you when you come back, " + username + "!")
	else:
		username = get_new_username()
		print("We will remember you when you come back, " + username + "!")


greet_user()