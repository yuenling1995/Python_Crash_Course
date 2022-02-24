alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
	print(alien)


#use loop to create 30 aliens
aliens = []

for alien_number in range(30):
	new_alien = {'alien_number': alien_number, 'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)

#print the first 5 aliens
for alien in aliens[:5]:
	print(alien)
print("...")

print("Total number of aliens: " + str(len(aliens)))




#change parts of elements in a list of dictionaries
aliens = []

#make 30 green aliens
for alien_number in range(0,30):
	new_alien = {'alien_number': alien_number, 'color': 'green', 'points': 5,
				 'speed': 'slow'}
	aliens.append(new_alien)

for alien in aliens[0:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['points'] = 10
		alien['speed'] = 'medium'
	elif alien['color'] == 'yellow':
		alien['color'] = 'red'
		alien['points'] = 15
		alien['speed'] = fast

#show the first 5 aliens
for alien in aliens[:10]:
	print(alien)
print("...")















