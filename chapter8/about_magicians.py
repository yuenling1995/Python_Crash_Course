# this function is used to move magicians to the new list
def make_magicians(input, output):
	while input:
		current = input.pop()
		output.append(current)

#this function is used to display the new list of magicians
def display_magicians(output):
	for name in output:
		print("Great " + name.title())



input_names = ['yuen', 'helen', 'hannah']
output_names = []
make_magicians(input_names, output_names)
display_magicians(output_names)