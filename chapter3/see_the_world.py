places = ['Paris', 'Barcelona', 'Greece', 'Thailand', 'Germany']
#print in order without changing the actual list
print(sorted(places))
print(places)
#print in reverse order without changing the list
print(sorted(places, reverse = True))
print(places)
#use reverse() method to change the order of list 
places.reverse()
print(places)
#use reverse() again to go back to original order
places.reverse()
print(places)
#use sort() method to change the order of actual list
places.sort()
print(places)
#use sort() method again to reverse the order
places.sort(reverse=True)
print(places)




