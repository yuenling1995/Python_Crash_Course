pizzas = ['sausage', 'pepperoni', 'cheese', 'plain', 'meat lover', 'hawaiian', 'artichoke']
for pizza in pizzas:
	print("One of my fav pizzas is " + pizza.title() + ".\n")
print("I really love pizza!")



print("\nThe first three items in the list are:")
print(pizzas[:3])

print("\nThree items from the middle of the list are:")
num = int(round(len(pizzas)/2,0)-2)
print(num)
print(pizzas[num:num+3])


print("\nThe last three items in the list are:")
print(pizzas[-3:])


