
filename = '/Users/Jessicaboomboom/Desktop/python_work/chapter10/text_files/pi_digits.txt'


with open(filename) as file_object:
	lines = file_object.readlines()

for line in lines:
	print(line.rstrip())


