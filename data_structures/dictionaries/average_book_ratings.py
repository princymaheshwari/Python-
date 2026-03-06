# Average Book Ratings
# Write a function average_book_ratings(), that calculates the average rating for each book in a collection. The function takes one parameter: a dictionary book_ratings where each key-value pair represents a book title and a list of its ratings, respectively. Ratings are represented as floating-point numbers. The function should return a new dictionary with book titles as keys and their average rating.

def average_book_ratings(book_ratings):

    return {book_title: (sum(ratings)/len(ratings)) for book_title, ratings in book_ratings.items()}

book_ratings = {
    "The Great Gatsby": [4.5, 3.0, 5.0],
    "To Kill a Mockingbird": [4.8, 5.0, 4.0, 4.9]
}
print(average_book_ratings(book_ratings))