from user import User
from admin import Admin, Privileges

new_admin = Admin('yuen', 'cheng', 26, '5 foot 7', 12)
new_admin.privileges.show_privileges()

