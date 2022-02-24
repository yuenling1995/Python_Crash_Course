countries = ['Korea', 'China', 'Japan', 'France', 'England', 'Greece']

#add or remove elements in the list based on index or value
countries.append('Thailand')
print(countries)
countries.insert(0, 'Germany')
print(countries)
del countries[-1]
print(countries)
countries.pop(0)
print(countries)
countries.remove('England')
print(countries)

#organize the list - sort them permanently or temparily
countries.sort()
print("\n")
print(countries)
print(sorted(countries, reverse = True))
countries.reverse()
print(countries)
countries.sort()
print(countries)
print(len(countries))





