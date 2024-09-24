# Book Recommender

Welcome to the Book Recommender application! This application helps users find book recommendations based on their preferences for genre, author, and book length.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Classes](#classes)
    - [Book](#book)
    - [Reader](#reader)
    - [BookRecommender](#bookrecommender)
- [Example](#example)
- [License](#license)

## Installation

1. Clone the repository:
        ```sh
        git clone https://github.com/yourusername/book-recommender.git
        ```
2. Navigate to the project directory:
        ```sh
        cd book-recommender
        ```
3. Ensure you have Python installed. This project requires Python 3.6+.

## Usage

To run the application, execute the following command:
```sh
python app.py
```

The application will prompt you to enter your name, preferred genre, preferred author, and preferred book length. Based on your inputs, it will recommend books and enhance the recommendations based on your feedback.

## Classes

### Book

The Book class represents a book with attributes such as title, genre, author, and length.

### Reader

The Reader class represents a user with preferences for genre, author, and book length. It also collects feedback on recommended books.

#### Methods

- `__init__(self, name, preferred_genre, preferred_author, preferred_length)`: Initializes a new reader with the given preferences.
- `__str__(self)`: Returns a string representation of the reader.
- `give_feedback(self, books)`: Collects feedback on the recommended books.

### BookRecommender

The BookRecommender class provides methods to recommend books and enhance recommendations based on user feedback.

#### Methods

- `recommend_books(cls, books, reader)`: Recommends books based on the reader's preferences.
- `enhance_recommendation(cls, feedback, name)`: Enhances recommendations based on the feedback provided by the reader.

## Example

Here is an example of how the application works:

1. The application prompts the user for their name, preferred genre, preferred author, and preferred book length.
2. Based on the inputs, it recommends books.
3. The user provides feedback on the recommended books.
4. The application enhances the recommendations based on the feedback.

## License

This project is unlicensed, feel free to use and upgrade as you wish!