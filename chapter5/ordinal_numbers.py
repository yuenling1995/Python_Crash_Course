numbers = list(range(1,10))
for number in numbers:
	number = str(number)
	if number == 1:
		print(number + "st")
	elif number == 2:
		print(number + "nd")
	elif number == 3:
		print(number + "rd")
	else:
		print(number + "th")
print("Finished!")