print("Give me two numbers, and I will add them up: ")
print("Enter 'q' to quit: ")

while True:
	first_num = input("\nFirst number: ")
	if first_num == 'q':
		break 

	second_num = input("\nSecond number: ")
	if second_num == 'q':
		break

	try:
		answer = int(first_num) + int(second_num)
	except ValueError:
		print("\nEither input value is not a number! ")
		pass
	else:
		print("The sum is " + str(answer))

