def city_country(city, country, population=""):
	"""brief info about the city and country"""
	if population:
		string = city.title() + ", " + country.title() + " - population " + str(population)
	else:
		string = city.title() + ", " + country.title()
	return string
