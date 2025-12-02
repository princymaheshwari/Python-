import sys
from Movie import *
from Theater import *
from Screen import *
from Show import *
from datetime import datetime

# Given a director name as input this function opens and reads
# data from files movies.dat, theaters.dat, screens.dat, and shows.dat.
# It then creates the data structure as shown in the figure and returns 
# two dictionaries: movies (key: mid and value: movie object for mid) and 
# theaters (key: tid and value: theater object). 
def load_data(dname):
    movies = {}
    theaters = {}

    with open(f"{dname}/movies.dat") as f:
        lines = f.read().splitlines()

        for line in lines:
            mid, title, country, year = line.split(":")
            m = Movie(mid, title, country, year)
            if mid not in movies:
                movies[mid] = m 

    with open(f"{dname}/theaters.dat") as f:
        lines = f.read().splitlines()

        for line in lines:
            tid, theater_name, theater_city = line.split(":")
            t = Theater(tid, theater_name, theater_city)
            if tid not in theaters:
                theaters[tid] = t

    with open(f"{dname}/screens.dat") as f:
        lines = f.read().splitlines()

        for line in lines:
            theater_id, sid, screen_name = line.split(":")
            theater = theaters[theater_id]
            s = Screen(sid, screen_name, theater)
            theater.add_screen(s)
    
    # for tid in theaters:
    #     print(theaters[tid].screens)

    with open(f"{dname}/shows.dat") as f:
        lines = f.read().splitlines()

        for line in lines:
            theater_displayed, screen_id, movie_id, date, time, no_of_visitors = line.split(":")

            # Making up the show object
            dt = datetime.strptime(date + " " + time, "%m/%d/%Y %I%p")
            show = Show(dt, int(no_of_visitors))

            #Setting up the movie relationship
            show.set_movie(movies[movie_id])
            movies[movie_id].add_show(show)

            #Setting up the Screen relationship
            screen = None
            for each_screen in theaters[theater_displayed].screens:
                if each_screen.sid == screen_id:
                    screen = each_screen
                    break

            show.set_screen(screen)
            screen.add_show(show)


            

            
        
load_data(sys.argv[1])