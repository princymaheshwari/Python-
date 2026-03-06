# Best Movie Genre
# Imagine you're contributing to a move recommendation engine, and you're tasked with writing a function named most_popular_genre() that returns the genre with the highest average rating across all movies.

# The function takes in a list of dictionaries named movies as a parameter. Each dictionary represents data associated with a movie, including its title, genre, and rating. The function calculates the average rating for each genre and returns the genre with the highest average rating.

def most_popular_genre(movies):
    genres = {}

    for movie in movies:
        if movie["genre"] not in genres:
            genres[movie["genre"]] = []

        genres[movie["genre"]].append(movie["rating"])

    avg_rating = {genre: (sum(ratings))/len(ratings) for genre, ratings in genres.items()}
    return max(avg_rating, key=avg_rating.get)


movies = [
    {"title": "Inception",
     "genre": "Science Fiction",
     "rating": 8.8
    },
    {"title": "The Matrix", 
     "genre": "Science Fiction",
     "rating": 8.7
    },
    {"title": "Pride and Prejudice", 
     "genre": "Romance",
     "rating": 7.8
    },
    {"title": "Sense and Sensibility", 
     "genre": "Romance",
     "rating": 7.7
    }
]

print(most_popular_genre(movies))
