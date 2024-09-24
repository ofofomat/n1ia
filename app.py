import book_recomender
import book
import reader

def main():
    """
    Main function to run the Book Recommender application.
    This function performs the following tasks:
    1. Initializes sets to keep track of unique genres, authors, and lengths.
    2. Retrieves the list of books.
    3. Prompts the user for their name.
    4. Displays unique genres from the list of books and prompts the user to select their preferred genre.
    5. Displays unique authors from the list of books and prompts the user to select their preferred author.
    6. Displays unique lengths from the list of books and prompts the user to select their preferred length.
    7. Creates a new reader object with the user's preferences.
    8. Recommends books to the user based on their preferences.
    Note:
        This function assumes the existence of `book.books`, `reader.Reader`, and `book_recomender.BookRecommender.recommend_books`.
    """
    # Set variables
    print_genres = set()
    print_authors = set()
    print_lengths = set()

    # Get the books
    books = book.books

    # Get reader preferences
    print("Welcome to Book Recommender!")
    print("Please, tell us a little bit about yourself:")
    print()
    name = input("What's your name? ")
    print()
    for a_book in books:
        if a_book.genre not in print_genres:
            print(a_book.genre)
            print_genres.add(a_book.genre)
    preferred_genre = input("What's your preferred genre from the list above? ")
    print()
    for a_book in books:
        if a_book.author not in print_authors:
            print(a_book.author)
            print_authors.add(a_book.author)
    preferred_author = input("What's your preferred author from the list above? ")
    print()
    for a_book in books:
        if a_book.length() not in print_lengths:
            print(a_book.length())
            print_lengths.add(a_book.length())
    preferred_length = input("What's your preferred length from the list above? ")

    # Create the user
    new_reader = reader.Reader(name, preferred_genre, preferred_author, preferred_length)

    # Recommend books
    book_recomender.BookRecommender.recommend_books(books, new_reader)


if __name__ == "__main__":
    main()