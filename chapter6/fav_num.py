fav_numbers = {
	'yuen': [12, 6, 10],
	'amy': [8],
	'david': [6, 18, 16],
	'sam': [10],
	'hannah': [26],
	}

for name, num in fav_numbers.items():
	print(name.title() + "'s fav numbers are: ")
	for number in num:
		print("\t" + str(number))
