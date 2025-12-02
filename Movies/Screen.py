class Screen:

    # constructor
    def __init__(self,id,n,t):
        self.sid = id
        self.sname = n
        self.theater = t
        self.shows = []

    # getter
    def get_sid(self):
        return self.sid

    # getter
    def get_sname(self):
        return self.sname
    
    # getter
    def get_theater(self):
        return self.theater
    
    # getter
    def get_shows(self):
        return self.shows
    
    # add show s to this screen
    def add_show(self,s):
        self.shows.append(s)
        
    def __str__(self):
        return "[" + ",".join([self.theater.get_tid(),self.sid,self.sname]) +"]"