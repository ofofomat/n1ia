class Reader:
    """
    A class to represent a reader with specific preferences.
    Attributes:
    -----------
    name : str
        The name of the reader.
    preferred_genre : str
        The preferred genre of the reader.
    preferred_author : str
        The preferred author of the reader.
    preferred_length : str
        The preferred length of books for the reader.
    feedback : list
        A list to store feedback on books.
    Methods:
    --------
    __str__():
        Returns a string representation of the Reader object.
    give_feedback(books):
        Rates a list of books based on the reader's preferences and stores the feedback.
        Parameters:
            books (list): A list of book objects to be rated.
        Returns:
            list: A list of tuples containing the book and its likeliness rating.
    """

    def __init__(self, name, preferred_genre, preferred_author, preferred_length):
        self.name = name
        self.preferred_genre = preferred_genre.lower()
        self.preferred_author = preferred_author.lower()
        self.preferred_length = preferred_length.lower()
        self.feedback = []

    def __str__(self):
        return (f"Reader(name={self.name}, preferred_gender={self.preferred_genre}, "
                f"preferred_author={self.preferred_author}, preferred_length={self.preferred_length})")

    def give_feedback(self, books):
        for book in books:
            likeliness = 0
            if book.author.lower() == self.preferred_author:
                likeliness += 1
            if book.genre.lower() == self.preferred_genre:
                likeliness += 1
            if book.length() == self.preferred_length:
                likeliness += 1
            self.feedback.append((book, likeliness))
        print()
        print(f'{self.name}: I\'d rate these books as (from 0 to 3 stars):')
        for book, likeliness in self.feedback:
            print(f"{book.title} - {likeliness} star(s)")
        return self.feedback