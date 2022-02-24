def make_album(artist, album):
	"""return the artist name and album title"""
	info = {'artist': artist.title(), 'album': album.title()}
	return info

while True:
	print("This stores your artist's info and show them below. Pleaser type 'q' to exit and see results.")
	name = input("Please enter the artist's name here: ")
	if name == 'q':
		break

	title= input("Please enter the album title here: ")
	if title == 'q':
		break

	info = make_album(name, title)
	print(info)





