# Best book
# Write a function named highest_rated() that returns the book with the highest rating.

# The function should take in a list of dictionaries named books as a parameter. Each dictionary represents data associated with a book, including its title, author, and rating. The function should return the dictionary for the book with the highest rating.

def highest_rated(books):
    
    highest_rated_book = books[0]
    highest_rating = highest_rated_book["rating"]
    for book in books:
        if book["rating"] > highest_rating:
            highest_rated_book = book
            highest_rating = book["rating"]

    return highest_rated_book


books = [
    {"title": "Tomorrow, and Tomorrow, and Tomorrow",
     "author": "Gabrielle Zevin",
     "rating": 4.18
    },
    {"title": "A Fortune For Your Disaster",
     "author": "Hanif Abdurraqib",
     "rating": 4.47
    },
    {"title": "The Seven Husbands of Evenlyn Hugo",
     "author": "Taylor Jenkins Reid",
     "rating": 4.40
    }
]

print(highest_rated(books))
