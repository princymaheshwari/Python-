class Movie:

	# constructor
	def __init__(self,id,t,c,y):
		self.mid = id
		self.title = t
		self.country = c
		self.year = y
		self.shows = []

	# getter
	def get_mid(self):
		return self.mid
	
	# getter
	def get_title(self):
		return self.title
	
	# adds show s to self.shows
	def add_show(self,s):
		self.shows.append(s)

	# returns number of matinee visitors and number of evening visitors for this movie
	def visitors(self):
		no_of_matinee_visitors = 0
		no_of_evening_visitors = 0

		for show in self.shows:
			hour = show.get_sdatetime().hour

			if hour < 17:
				no_of_matinee_visitors += show.get_nvisitors()
			elif hour >= 17:
				no_of_evening_visitors += show.get_nvisitors()

		return no_of_matinee_visitors, no_of_evening_visitors

	def __str__(self):
		return "[" + ",".join([self.mid,self.title,self.country,str(self.year)]) + "]"
