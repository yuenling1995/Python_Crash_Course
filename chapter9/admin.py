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


class Privileges():
	"""A simple attempt to show admin's privileges."""
	def __init__(self):
		self.privileges = ['can add post', 'can delete post', 'can ban user']

	def show_privileges(self):
		print("Here's a list of admin's privileges: ")
		for privilege in self.privileges:
			print(privilege)


class Admin(User):
	"""A simple attempt to show admin's privileges."""
	def __init__(self, first_name, last_name, age, height, login_attempts):
		super().__init__(first_name, last_name, age, height, login_attempts)
		self.privileges = Privileges()




#new_admin = Admin('yuen', 'cheng', 26, '5 foot 7', 10)
#new_admin.describe_user()
#new_admin.greet_user()
#new_admin.increment_login_attempts()
#print(new_admin.login_attempts)

#new_admin.privileges.show_privileges()
