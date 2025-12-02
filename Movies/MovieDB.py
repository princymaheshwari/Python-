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
    
    # Making the movies dictionary
    with open(f"{dname}/movies.dat") as f:
        lines = f.read().splitlines()

        for line in lines:
            mid, title, country, year = line.split(":")
            m = Movie(mid, title, country, year)
            movies[mid] = m 

    # Making the theaters dictionary
    with open(f"{dname}/theaters.dat") as f:
        lines = f.read().splitlines()

        for line in lines:
            tid, theater_name, theater_city = line.split(":")
            t = Theater(tid, theater_name, theater_city)
            if tid not in theaters:
                theaters[tid] = t
    
    # Making the screens connections
    with open(f"{dname}/screens.dat") as f:
        lines = f.read().splitlines()

        for line in lines:
            theater_id, sid, screen_name = line.split(":")
            theater = theaters[theater_id]
            s = Screen(sid, screen_name, theater)
            theater.add_screen(s)

    # Making the shows connections
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
                if each_screen.get_sid() == screen_id:
                    screen = each_screen
                    break

            show.set_screen(screen)
            screen.add_show(show)


    return movies, theaters

# returns the length of the longest theater name
# useful in formatting output
def longest_theater_name_len(theaters):

    len_of_longest_theater_name = 0

    for t in theaters.values():
        name_len = len(t.get_tname())
        if name_len > len_of_longest_theater_name:
            len_of_longest_theater_name = name_len

    return len_of_longest_theater_name


# returns the length of the longest screen name
# useful in formatting output
def longest_screen_name_len(theaters):

    len_of_longest_screen_name = 0

    for t in theaters.values():
        for screen in t.screens:
            len_screen_name = len(screen.get_sname())
            if len_screen_name > len_of_longest_screen_name:
                len_of_longest_screen_name = len_screen_name
    
    return len_of_longest_screen_name
    

# finds statistics for movie mid and returns number of matinee visitors
# and number of evening visitors for the movie.
def process_movie_statistics(movies, mid):
    
    no_of_matinee_visitors, no_of_evening_visitors = movies[mid].visitors()

    revenue_earned_from_matinee_visitors = no_of_matinee_visitors*5
    revenue_earned_from_evening_visitors = no_of_evening_visitors*8

    total_revenue = revenue_earned_from_matinee_visitors + revenue_earned_from_evening_visitors

    return no_of_matinee_visitors, no_of_evening_visitors, revenue_earned_from_matinee_visitors, revenue_earned_from_evening_visitors, total_revenue


# finds show listings for a movie with mid in a given city
# the result should be sorted by date and time of show.
# the result should be a list of tuples - see sample output for what should
# go into the tuple.
def process_show_listings(shows, mid, city):
    
    shows_for_this_movie_and_city = []

    for show in shows:
        movie = show.get_movie()
        screen = show.get_screen()
        theater = screen.get_theater()
        show_city = theater.get_city()
        date_time = show.get_sdatetime()
        no_of_visitors = show.get_nvisitors()

        if movie.get_mid() == mid:
            if show_city == city:
                shows_for_this_movie_and_city.append((theater.get_tname(), screen.get_sname(), date_time, no_of_visitors ))

    shows_for_this_movie_and_city.sort(key = lambda item: item[2])
    return shows_for_this_movie_and_city

def menu():
    print("\nMenu Options\n")
    print("  Theater Cities (c)")
    print("  Movie IDs (d)")
    print("  Theater IDs (h)")
    print("  Movies Screened in Theater (t tid)")
    print("  Movie Statistics (m mid)")
    print("  Show Listings for Movie in City (s mid city)")
    print("  Quit (q)\n")
    return input("Enter your option: ").strip()

def main():

    movies, theaters = load_data(sys.argv[1])

    while True:
        option = menu()

        if option == "q":
            break

        elif option == "c":
            cities = sorted({theaters[t].get_city() for t in theaters})
            print("\nCities: " + ", ".join(cities))

        elif option == "d":
            mids = sorted(movies.keys())
            print("\nmids: " + ", ".join(mids))

        elif option == "h":
            tids = sorted(theaters.keys())
            print("\ntids: " + ", ".join(tids))

        elif option.startswith("t "):
            _, tid = option.split()
            if tid in theaters:
                theater = theaters[tid]
                movie_titles = theater.movies_screened()
                print("\nMovies screened in " + theater.get_tname() + "\n")
                for title in movie_titles:
                    print(title)
            else:
                print("\nPlease input a Valid theater ID")

        elif option.startswith("m "):
            _, mid = option.split()
            if mid in movies:
                no_matinee, no_evening, rev_matinee, rev_evening, total_rev = process_movie_statistics(movies, mid)
                movie = movies[mid]
                print("\nStatistics for " + movie.get_title() + "\n")
                print(f"Matinee Visitors: {no_matinee:4d} @$5 each = ${rev_matinee:6d}")
                print(f"Evening Visitors: {no_evening:4d} @$8 each = ${rev_evening:6d}\n")
                print(f"TOTAL Revenue: ${total_rev}")
            else:
                print("\nPlease input a Valid Movie ID")

        elif option.startswith("s "):
            parts = option.split()
            if len(parts) == 3:
                _, mid, city = parts
                shows = []
                for m in movies.values():
                    shows.extend(m.shows)
                result = process_show_listings(shows, mid, city)
                if result:

                    theater_width = longest_theater_name_len(theaters)
                    screen_width = longest_screen_name_len(theaters)

                    print("\nScreenings for " + movies[mid].get_title() + " in " + city)
                    print("------------------------------------------------------")
                    print("Theater".ljust(theater_width+2),
                          "Screen".ljust(screen_width+2),
                          "Date".ljust(12),
                          "Time".ljust(7),
                          "#Visitors", sep="")
                    print("------------------------------------------------------")
                    for tname, sname, dt, nvis in result:
                        date_str = dt.strftime("%m/%d/%Y")
                        time_str = dt.strftime("%I %p").lstrip("0")
                        print(f"{tname:<{theater_width+2}}{sname:<{screen_width+2}}{date_str:<12}{time_str:<7}{nvis:>8}")
                    print("------------------------------------------------------")
            
            else:
                print("\nPlease input a valid movie ID and city")
        
        else:
            print("\nPlease input a Valid Command")

main()
