alien_0 = {'color': 'green', 'points': 5}
#print(alien_0)

#add key-value pairs
alien_0['x_position'] = 0
alien_0['y_position'] = 25
#print(alien_0)

#start with an empty dictionary
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5
#print(alien_0)

#modify dictionary
alien_0 = {'color': 'green'}
#print("The alien is " + alien_0['color'] + '.')

alien_0['color'] = 'yellow'
#print("The alien is now " + alien_0['color'] + '.\n\n')


#modify dictionary - another example
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
#print("Original x-position: " + str(alien_0['x_position']) + "\n")

#move the alien to the right.
#Determine how far to move the alien based on its current speed.

#now change the speed to fast
alien_0['speed'] = 'fast'

#determine how much the speed increments the x-position
if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	#this must be a fast alien
	x_increment = 3

#the new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

#print("New x-position: " + str(alien_0['x_position']) + "\n")



#removing key-value pairs:
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)


















