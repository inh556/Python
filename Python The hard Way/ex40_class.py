class Song(object):
	def __init__(self, lyrics):
		self.lyrics = lyrics
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line
	def length_of_lyrics(self):
		print len(self.lyrics)
song1 = ["Happy birthday to you",
		"I dont\'t want to get sued",
		"So I'll stop right there"]
song2 = ["They really around the family",
		"With pockets full of shells"]
happy_baby = Song(song1)
bulls_on_parade = Song(song2)
happy_baby.sing_me_a_song()
bulls_on_parade.sing_me_a_song()

happy_baby.length_of_lyrics()
bulls_on_parade.length_of_lyrics()
					