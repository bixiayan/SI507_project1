
class Media:
	def __init__(self, title="No Title", author="No Author", release_year="No year", json=None):
		if json == None:
			self.title = title
			self.author = author
			self.release_year = release_year
		else:
			self.process_json(json)

	def process_json(self, json):
			self.title = json['trackCensoredName']
			self.author = json['artistName']
			self.release_year = json['releaseDate']

	def __str__(self):
		return self.title + " by " + self.author + " (" + self.release_year + ")"

	def __len__(self):
		return 0

class Song(Media):
	def __init__(self, title="No Title", author="No Author", release_year="No year", genre="No genre", track_length=0, json=None):
		if json == None:
			super().__init__(title, author, release_year)
			self.genre = genre
			self.track_length = track_length
		else:
			self.process_json(json)

	def process_json(self, json):
		self.genre = json['primaryGenreName']
		self.track_length = json['trackTimeMillis']

	def __str__(self):
		return super().__str__() + " [" + self.genre + "]"

	def __len__(self):
		return self.track_length

class Movie(Media):
	def __init__(self, title="No Title", author="No Author", release_year="No year", rating="No rating", movie_length=0, json=None):
		if json == None:
			super().__init__(title, author, release_year)
			self.rating = rating
			self.movie_length = movie_length
		else:
			self.process_json(json)

	def process_json(self, json):
		self.rating = json['contentAdvisoryRating']
		self.movie_length = json['trackTimeMillis']


	def __str__(self):
		return super().__str__() + " [" + self.rating + "]"
	
	def __len__(self):
		return self.movie_length




## Other classes, functions, etc. should go here

if __name__ == "__main__":
	# your control code for Part 4 (interactive search) should go here
	pass
