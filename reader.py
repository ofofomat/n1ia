class Reader:
    """
    A class to represent a reader with specific preferences for genre, author, and book length.
    Attributes:
    -----------
    GENRE_MAP : dict
        A dictionary mapping genre numbers to genre names.
    AUTHOR_MAP : dict
        A dictionary mapping author numbers to author names.
    LENGTH_MAP : dict
        A dictionary mapping length numbers to length descriptions.
    Methods:
    --------
    __init__(name, preferred_genre_num, preferred_author_num, preferred_length_num):
        Initializes the Reader with a name and preferred genre, author, and length.
    __str__():
        Returns a string representation of the Reader.
    add_book_correlations(books):
        Adds book correlations based on the reader's preferences.
    get_book_correlations():
        Returns the list of book correlations.
    """
    # Dictionaries to map the user input to the actual values
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
        return (f"Reader(name={self.name}, preferred_gender={self.preferred_genre}, "
                f"preferred_author={self.preferred_author}, preferred_length={self.preferred_length})")

    def add_book_correlations(self, books):
        """
        Adds book correlations based on the user's preferences.

        This method iterates over a list of books and calculates a likeliness score
        for each book based on the user's preferred author, genre, and length. The
        likeliness score is incremented by 1 for each matching preference. The book
        and its corresponding likeliness score are then appended to the 
        `book_correlations` list.

        Args:
            books (list): A list of book objects to be evaluated.

        Attributes:
            book_correlations (list): A list of tuples where each tuple contains a 
                                      book object and its likeliness score.
        """
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