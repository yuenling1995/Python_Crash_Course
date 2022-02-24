my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print('My fav foods are:')
list = [food for food in my_foods]
print(list)

print("\nMy friend's fav foods are:")
list = [food for food in friend_foods]
print(list)