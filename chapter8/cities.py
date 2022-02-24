def describe_city(city, country = 'France'):
	"""info about the city and country"""
	print(city.title() + " is in " + country.title() + ".")


describe_city('paris')
describe_city('tokyo', 'japan')
describe_city(city = 'hong kong', country = 'china')