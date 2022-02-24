#string tests
string_1 = 'hello'
string_2 = 'Hello'
print(string_1 == string_2)
print(string_1 == string_2.lower())

#numerical tests
num_1 = 12
num_2 = 8

print(num_1 == num_2)
print(num_2+8 > num_1)
print(num_2*3 <= num_1*2)
print(num_1 != num_2)


#test using the and/or
if string_1 == string_2.lower() and 2+3 == 5:
	print("You're right!")
else:
	print("You're wrong!")


if string_1 == string_2 or num_1 > num_2:
	print("Yes man")
else:
	print("Nah!")


#whether item is in a list
fruits = ['apple', 'banana', 'carrot']
animals = ['cats', 'dogs', 'rabbits', 'horses', 'deer']

#whether item is not in a list
test_item = 'apple'
if test_item in fruits:
	print("Yes!")
else:
	print("Nah!")

test_item_2 = 'hello'
if test_item_2 not in animals:
	print("It's not in the 'animals' list!!")

for animal in animals:
	if animal == 'cats':
		print("Yes cats are my favorite animals!")
	else:
		print("No you guess wrong!")






