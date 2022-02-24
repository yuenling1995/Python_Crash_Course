def build_profile(first, last, **user_info):
	"""This function displays a dictionary of user info"""
	profile = {}
	profile['first_name'] = first.title()
	profile['last_name'] = last.title()
	for key, value in user_info.items():
		profile[key] = value
	return profile 

profile = build_profile('yuen', 'cheng',
						age = 26,
						height = '5 foot 7',
						education = 'master degree')

print(profile)