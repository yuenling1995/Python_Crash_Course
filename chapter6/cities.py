cities = {
	'Paris': {
		'country': 'France',
		'population': 300000,
		'fact': 'This city is so pretty!',
		},
	'Athens': {
		'country': 'Greece',
		'population': 680000,
		'fact': 'This city is very historical.',
		},
	'Tokyo': {
		'country': 'Japan',
		'population': 620000,
		'fact': 'The cherry blossoms every year is amazing!',
		},
}


for name, info in cities.items():
	print("Here's " + name + "'s info: ")
	for key, values in info.items():
		print(" \t" + str(key) + ": " + str(values))











