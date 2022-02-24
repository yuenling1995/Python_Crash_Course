def make_car(manufacturer, model_name, **info):
	"""This function shows a dictionary of car info"""
	car = {}
	car['manufacturer'] = manufacturer.title()
	car['model_name'] = model_name.title()
	for key, value in info.items():
		car[key] = value
	return car

car = make_car('subaru', 'outback', color = 'blue', tow_package = True)
print(car)