class User():
	"""provide simple info about the users."""
	def __init__(self, first_name, last_name, age, height, login_attempts):
		"""Initialzie name and other attributes."""
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.height = height
		self.login_attempts = login_attempts

	def describe_user(self):
		"""print a summary of user profile."""
		full_name = self.first_name + " " + self.last_name
		print("The user's full name: " + full_name.title())
		print("Age: " + str(self.age))
		print("Height: " + str(self.height))

	def greet_user(self):
		print("Welcome " + self.first_name.title() + "!")

	def increment_login_attempts(self):
		self.login_attempts += 1

	def reset_login_attempts(self):
		self.login_attempts = 0

#new_user = User('yuen', 'cheng', 26, '5 foot 7')
#print(new_user.first_name)
#print(new_user.age)
#new_user.describe_user()
#new_user.greet_user()
#user = User('yuen', 'cheng', 26, '5 foot 7', 6)
#user.increment_login_attempts()
#print(user.login_attempts)
#user.reset_login_attempts()
#print(user.login_attempts)
