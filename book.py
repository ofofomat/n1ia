class Book:
    """
    A class to represent a book.
    Attributes:
    -----------
    all_books : list
        Class attribute to store all instances of Book.
    title : str
        The title of the book.
    __pages : int
        The number of pages in the book (private attribute).
    genre : str
        The genre of the book.
    author : str
        The author of the book.
    Methods:
    --------
    __str__():
        Returns a string representation of the book.
    length():
        Returns a string indicating the length of the book based on the number of pages.
    """
    all_books = [] 

    def __init__(self, title, pages, genre, author):
        self.title = title
        self.__pages = pages
        self.genre = genre
        self.author = author
        Book.all_books.append(self)

    def __str__(self):
        return f"Book: {self.title}, Pages: {self.__pages}, Gender: {self.genre}, Author: {self.author}"

    def length(self):
        if self.__pages < 500:
            return "Small"
        elif 500 <= self.__pages <= 1000:
            return "Medium"
        else:
            return "Extense"