import genre
import author
import book_recomender
import book
import reader

def main():
    # Create genres
    romance = genre.Genre("Romance")
    fiction = genre.Genre("Fiction")
    fantasy = genre.Genre("Fantasy")

    # Create authors
    jk_rowling = author.Author("J.K. Rowling")
    jane_austen = author.Author("Jane Austen")
    george_orwell = author.Author("George Orwell")
    stephen_king = author.Author("Stephen King")
    agatha_christie = author.Author("Agatha Christie")

    # Create books
    book.Book("Harry Potter", 700, romance, jk_rowling)
    book.Book("1984", 400, fiction, george_orwell)
    book.Book("Pride and Prejudice", 278, fantasy, jane_austen)
    book.Book("Fantastic Beasts and Where to Find Them", 640, romance, jk_rowling)
    book.Book("Murder on the Orient Express", 107, fiction, agatha_christie)
    book.Book("Pride and Postjudice", 300, fantasy, jane_austen)
    book.Book("The Big Malakoi", 1245, romance, jk_rowling)
    book.Book("Murder on the Ocident Express", 250, fiction, agatha_christie)
    book.Book("1984: 1983, a prequeal", 1001, fantasy, george_orwell)
    book.Book("It", 1100, romance, stephen_king)
    book.Book("That, the stuff", 2014, fiction, stephen_king)
    book.Book("1984: 1985, a sequeal", 870, fantasy, george_orwell)

    # Get reader preferences from the terminal
    print("Welcome to your specialist book recommender!")
    print("Let's start with the basics. Shall we?")
    reader_name = input("What's your name: ")

    print()
    print("From the list bellow, which is your favorite author?")
    print(f'1 - {jk_rowling}')
    print(f'2 - {jane_austen}')
    print(f'3 - {george_orwell}')
    print(f'4 - {stephen_king}')
    print(f'5 - {agatha_christie}')
    preferred_author = int(input("Enter the number that represents your preferred author: "))

    print()
    print("And what about genre?")
    print(f'1 - {romance}')
    print(f'2 - {fiction}')
    print(f'3 - {fantasy}')
    preferred_genre = int(input("Enter the number that represents your preferred genre: "))

    print()
    print("And what's your preferred length?")
    print("1 - small")
    print("2 - medium")
    print("3 - extense")
    preferred_length = int(input("Enter the number that represents your preferred book length: "))

    print()
    print()
    print("Getting things started...")
    print(".")
    print(".")
    print(".")
    print()

    # Create a reader
    new_reader = reader.Reader(reader_name, preferred_genre, preferred_author, preferred_length)

    new_reader.add_book_correlations(book.Book.all_books)

    # Guess reader preferences
    preferred_author, preferred_genre, preferred_length = book_recomender.BookRecommender.get_preferences(new_reader.get_book_correlations())
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


if __name__ == "__main__":
    main()