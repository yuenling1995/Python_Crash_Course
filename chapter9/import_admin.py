#rom admin import User, Privileges, Admin
import admin

new_admin = admin.Admin('yuen', 'cheng', 26, '5 foot 7', 10)
new_admin.describe_user()
new_admin.greet_user()
new_admin.increment_login_attempts()
print(new_admin.login_attempts)
new_admin.privileges.show_privileges()