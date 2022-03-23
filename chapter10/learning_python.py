filename = '/Users/Jessicaboomboom/Desktop/python_work/chapter10/text_files/learning_python.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

for line in lines:
	line = line.strip()
	print(line.replace('python', 'C'))


