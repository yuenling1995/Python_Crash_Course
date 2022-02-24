favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
}

print("Sarah's favorite language is " + 
		favorite_languages['sarah'].title() +
		".")

#loop through all the keys in a dictionary
for name in favorite_languages.keys():
	print(name.title())


friends = ['phil', 'sarah']
for name in favorite_languages.keys():
	print(name.title())

	if name in friends:
		print("Hi " + name.title() +
			", I see your fav language is " +
			favorite_languages[name].title() + "!")



#loop through keys in order:
for name in sorted(favorite_languages.keys()):
	print(name.title() + ", thank you for taking the poll!")



#loop through all values in dictionary:
print("\nThe following languages have been mentioned: ")
for language in favorite_languages.values():
	print(language.title())



#loop in nested lists:
favorite_languages = {
	'jen': ['python', 'ruby'],
	'sarah': ['c'],
	'edward': ['ruby', 'go'],
	'phil': ['python', 'haskell'],
}


for name, languages in favorite_languages.items():
	if len(languages) > 1:
		print("\n" + name.title() + "'s favorite languages are:")
		for language in languages:
			print("\t" + language.title())
	else:
		print("\n" + name.title() + "'s favorite language is: " + str(languages))




