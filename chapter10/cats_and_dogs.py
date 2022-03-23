def read_file(filename):
	try:
		with open(filename) as file_obj:
			contents = file_obj.read()
	except FileNotFoundError:
		print("This file does not exist")
		pass
	else:
		print(contents)




file_cat = 'cats.txt'
file_dog = 'dogs.txt'
file_invalid = 'invalid.txt'
read_file(file_cat)
read_file(file_dog)
read_file(file_invalid)
