class Show:

    # constructor
    def __init__(self,dt,n):
        self.sdatetime = dt
        self.nvisitors = n
        self.movie = None
        self.screen = None

    # getter
    def get_sdatetime(self):
        return self.sdatetime
    
    # getter
    def get_nvisitors(self):
        return self.nvisitors
    
    # getter
    def get_movie(self):
        return self.movie
    
    # getter
    def get_screen(self):
        return self.screen
    
    # setter
    def set_movie(self,m):
        self.movie = m
    
    # setter
    def set_screen(self,s):
        self.screen = s

    def __str__(self):
        return "[" + self.movie.get_mid() + "," + self.screen.get_sid() + "," + str(self.sdatetime) + "," + str(self.nvisitors) +"]" 