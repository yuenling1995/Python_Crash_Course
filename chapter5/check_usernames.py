current_users = ['yuen', 'amy', 'david', 'tom', 'ashley']
new_users = ['amy', 'sara', 'David', 'katherine', 'laura']

for user in new_users:
	user = user.lower()
	if user in current_users:
		print("You need to enter a new username.")
	else:
		print("This username is available.")