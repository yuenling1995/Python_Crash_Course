def make_album(artist, album, num_tracks = ''):
	info = {'artist': artist.title(), 'album': album.title()}
	if num_tracks:
		info['num_tracks'] = num_tracks

	return info


information = make_album('yuen', 'forget me not')
print(information)
information_2 = make_album('jess', 'once upon a time')
print(information_2)