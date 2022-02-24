def make_shirt(size = "large"):
	"""print the size of the shirt"""
	print("The size of this shirt is: " + size + ".")

	if size == "large":
		print("I love Python!")
	else:
		print("The default message here.")

make_shirt("small")
make_shirt(size = "medium")
make_shirt()