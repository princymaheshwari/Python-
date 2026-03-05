class Theater:

    # constructor
    def __init__(self,id,n,c):
        self.tid = id
        self.tname = n
        self.city = c
        self.screens = []

    # getter
    def get_tid(self):
        return self.tid

    # getter
    def get_tname(self):
        return self.tname

    # getter
    def get_city(self):
        return self.city
    
    # add screen s to this theater
    def add_screen(self,s):
        self.screens.append(s)
    
    # return a sorted list of movie titles screened in this theater
    def movies_screened(self):
        movie_titles_screened = set()

        for screen in self.screens:
            for show in screen.get_shows():
                movie = show.get_movie()
                movie_name = movie.get_title()
                movie_titles_screened.add(movie_name)

        return sorted(movie_titles_screened)

    def __str__(self):
        return "[" + ",".join([self.tid,self.tname,self.city]) + "]"
