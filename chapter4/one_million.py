list = [value for value in range(1,1000001)]
print(list)

#another way
list = []
for value in range(1,1000001):
	list.append(value)
print(list)


print(min(list))
print(max(list))
print(sum(list))