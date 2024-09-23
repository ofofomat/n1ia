# Book Recommender System

## Overview

The Book Recommender System is a Python application designed to recommend books to users based on their preferences for genre, author, and book length. The system uses a set of predefined genres, authors, and books to generate personalized recommendations.

## Features

- **User Preferences**: Users can input their preferred genre, author, and book length.
- **Book Correlations**: The system calculates a likeliness score for each book based on the user's preferences.
- **Recommendations**: Books are recommended to the user based on the calculated likeliness scores.

## Components

### 1. Author

Represents an author with a name attribute.

```python
class Author:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
```

### 2. Genre

Represents a genre with a name attribute.

```python
class Genre:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
```

### 3. Book

Represents a book with a title, number of pages, genre, and author.

```python
class Book:
    all_books = []

    def __init__(self, title, pages, genre, author):
        self.title = title
        self.__pages = pages
        self.genre = genre
        self.author = author
        Book.all_books.append(self)

    def __str__(self):
        return f"Book: {self.title}, Pages: {self.__pages}, Genre: {self.genre}, Author: {self.author}"

    def length(self):
        if self.__pages < 500:
            return "Small"
        elif 500 <= self.__pages <= 1000:
            return "Medium"
        else:
            return "Extense"
```

### 4. Reader

Represents a reader with specific preferences for genre, author, and book length.

```python
class Reader:
    GENRE_MAP = {1: "Romance", 2: "Fiction", 3: "Fantasy"}
    AUTHOR_MAP = {1: "J.K. Rowling", 2: "Jane Austen", 3: "George Orwell", 4: "Stephen King", 5: "Agatha Christie"}
    LENGTH_MAP = {1: "Small", 2: "Medium", 3: "Extense"}

    def __init__(self, name, preferred_genre_num, preferred_author_num, preferred_length_num):
        self.name = name
        self.preferred_genre = self.GENRE_MAP.get(preferred_genre_num, "Unknown")
        self.preferred_author = self.AUTHOR_MAP.get(preferred_author_num, "Unknown")
        self.preferred_length = self.LENGTH_MAP.get(preferred_length_num, "Unknown")
        self.book_correlations = []

    def __str__(self):
        return (f"Reader(name={self.name}, preferred_genre={self.preferred_genre}, "
                f"preferred_author={self.preferred_author}, preferred_length={self.preferred_length})")

    def add_book_correlations(self, books):
        for book in books:
            likeliness = 0
            if book.author.name == self.preferred_author:
                likeliness += 1
            if book.genre.name == self.preferred_genre:
                likeliness += 1
            if book.length() == self.preferred_length:
                likeliness += 1
            self.book_correlations.append((book, likeliness))

    def get_book_correlations(self):
        return self.book_correlations
```

### 5. BookRecommender

Provides methods to determine user preferences based on book correlations and recommend books accordingly.

```python
class BookRecommender:
    @classmethod
    def get_preferences(cls, correlations):
        author_count = {}
        genre_count = {}
        length_count = {}

        for book, likeliness in correlations:
            if book.author in author_count:
                author_count[book.author] += likeliness
            else:
                author_count[book.author] = likeliness

            if book.genre in genre_count:
                genre_count[book.genre] += likeliness
            else:
                genre_count[book.genre] = likeliness

            if book.length() in length_count:
                length_count[book.length()] += likeliness
            else:
                length_count[book.length()] = likeliness

        preferred_author = max(author_count, key=author_count.get)
        preferred_genre = max(genre_count, key=genre_count.get)
        preferred_length = max(length_count, key=length_count.get)

        return preferred_author, preferred_genre, preferred_length

    @classmethod
    def recommend_books(cls, author, genre, length, books, name):
        love = []
        like = []
        print(f'Your preferred author seems to be {author}')
        print(f'Your preferred genre seems to be {genre}')
        print(f'And your preferred length seems to be {length}')
        print()
        for book in books:
            match_count = 0
            if book.author == author:
                match_count += 1
            if book.genre == genre:
                match_count += 1
            if book.length() == length:
                match_count += 1

            if match_count == 3:
                love.append(book)
            elif match_count == 2:
                like.append(book)

        if not love and not like:
            print(f'Oops, your taste for books is too unique {name}. We couldn\'t find any books that match your preferences')
            print()
        else:
            if love:
                print(f'Books you\'ll love {name}')
                for book in love:
                    print(book)
                print()
            if like:
                print(f'Books you might like {name}')
                for book in like:
                    print(book)
                print()
```

### 6. Main Application app.py

The main script that runs the application, collects user input, and provides book recommendations.

```python
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
    book.Book("Pride and Prejudice", 300, fantasy, jane_austen)
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

if __name__ == "__main__":
    main()
```

## How to Run

1. **Clone the repository**:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Run the application**:
    ```sh
    python app.py
    ```

3. **Follow the prompts** to input your preferences and receive book recommendations.

## Dependencies

- Python 3.x

## License

This project is not licensed.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.