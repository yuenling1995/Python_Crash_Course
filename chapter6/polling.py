favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
}

people = ['phil', 'edward', 'amy', 'david']

for person in people:
	if person in favorite_languages:
		print("You already took the poll, thanks for responding!")
	else:
		print("Hi " + person.title() + ", Please feel free to take the poll!")


