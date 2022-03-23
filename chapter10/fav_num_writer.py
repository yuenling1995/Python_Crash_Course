import json


def get_stored_num():
	"""fetch the stored num in file."""
	filename = "fav_num.json"
	try:
		with open(filename) as file_obj:
			num = json.load(file_obj)
	except FileNotFoundError:
		return None 
	else:
		return num 


def get_new_num():
	"""ask for user's fav num."""
	filename = "fav_num.json"
	num = input("What's your favorite number? ")
	with open(filename, 'w') as file_obj:
		json.dump(num, file_obj)


def show_num():
	filename = 'fav_num.json'
	num = get_stored_num()
	if num:
		print("I know your favorite number, it is " + str(num))
	else:
		num = get_new_num()
		print("We will remember this number when you come back!")


show_num()










