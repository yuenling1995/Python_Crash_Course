from random import randint

class Die():
	def __init__(self, sides=6):
		self.sides = sides

	def roll_die(self):
		x= randint(1, self.sides)
		print(x)



roll = Die()

for n in range(1,11):
	print("Roll die round " + str(n) + ":")
	roll.roll_die()



new_roll = Die(10)
for n in range(1,11):
	print("Roll die round " + str(n) + ":")
	new_roll.roll_die()


final_roll = Die(20)
for n in range(1,11):
	print("Roll die round " + str(n) + ":")
	final_roll.roll_die()	








