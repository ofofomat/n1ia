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
    book_recomender.BookRecommender.recommend_books(preferred_author, preferred_genre, preferred_length, book.Book.all_books, new_reader.name)

    # Feedback time
    print("How would you rate these recommendations?")
    print("1 - Boombastic")
    print("2 - Pretty good actually")
    print("3 - I've seen better")
    print("4 - Missed quite remarkably")
    print("5 - Thou hast sorely missed the mark in thy counsel, and my patience doth wane as the error deepens.")
    
    # Get feedback
    print()
    feedback = int(input("Please be honest - unless you're about to type 5, then you should reconsider: "))

    if feedback not in [5,4,3]:
        print()
        print(f'Well, I\'m happy to be of help for you, {new_reader.name}!')
    else:
        print()
        print("A wise man once said that everyone has the right to be wrong. You're lucky we all still believe in that!")
    book_recomender.BookRecommender.recommend_books(books, new_reader)


if __name__ == "__main__":
    main()