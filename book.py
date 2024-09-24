class Book:
    """
    A class used to represent a Book.
    Attributes
    ----------
    title : str
        The title of the book.
    __pages : int
        The number of pages in the book (private attribute).
    genre : str
        The genre of the book.
    author : str
        The author of the book.
    Methods
    -------
    __str__():
        Returns a string representation of the book.
    length():
        Determines the length category of the book based on the number of pages.
    """

    def __init__(self, title, pages, genre, author):
        self.title = title
        self.__pages = pages
        self.genre = genre
        self.author = author

    def __str__(self):
        return f"Book: {self.title}, Pages: {self.__pages}, Gender: {self.genre}, Author: {self.author}"

    def length(self):
        if self.__pages < 350:
            return "small"
        elif 350 <= self.__pages <= 700:
            return "medium"
        else:
            return "extense"

books = [
    Book("To Kill a Mockingbird", 281, "Fiction", "Harper Lee"),
    Book("1984", 328, "Dystopian", "George Orwell"),
    Book("The Great Gatsby", 180, "Fiction", "F. Scott Fitzgerald"),
    Book("The Catcher in the Rye", 214, "Fiction", "J.D. Salinger"),
    Book("The Hobbit", 310, "Fantasy", "J.R.R. Tolkien"),
    Book("Fahrenheit 451", 194, "Dystopian", "Ray Bradbury"),
    Book("Moby Dick", 635, "Adventure", "Herman Melville"),
    Book("War and Peace", 1225, "Historical", "Leo Tolstoy"),
    Book("Pride and Prejudice", 279, "Romance", "Jane Austen"),
    Book("The Lord of the Rings", 1178, "Fantasy", "J.R.R. Tolkien"),
    Book("Jane Eyre", 500, "Romance", "Charlotte Brontë"),
    Book("The Chronicles of Narnia", 767, "Fantasy", "C.S. Lewis"),
    Book("Animal Farm", 112, "Dystopian", "George Orwell"),
    Book("Brave New World", 311, "Dystopian", "Aldous Huxley"),
    Book("Wuthering Heights", 416, "Romance", "Emily Brontë"),
    Book("The Odyssey", 541, "Epic", "Homer"),
    Book("Crime and Punishment", 671, "Psychological", "Fyodor Dostoevsky"),
    Book("The Brothers Karamazov", 796, "Philosophical", "Fyodor Dostoevsky"),
    Book("Les Misérables", 1463, "Historical", "Victor Hugo"),
    Book("The Iliad", 683, "Epic", "Homer"),
    Book("Don Quixote", 1072, "Adventure", "Miguel de Cervantes"),
    Book("The Divine Comedy", 798, "Epic", "Dante Alighieri"),
    Book("The Picture of Dorian Gray", 254, "Philosophical", "Oscar Wilde"),
    Book("Dracula", 418, "Horror", "Bram Stoker"),
    Book("Frankenstein", 280, "Horror", "Mary Shelley"),
    Book("The Count of Monte Cristo", 1276, "Adventure", "Alexandre Dumas"),
    Book("A Tale of Two Cities", 489, "Historical", "Charles Dickens"),
    Book("Great Expectations", 505, "Fiction", "Charles Dickens"),
    Book("The Grapes of Wrath", 464, "Fiction", "John Steinbeck"),
    Book("The Old Man and the Sea", 127, "Fiction", "Ernest Hemingway"),
    Book("Catch-22", 453, "Satire", "Joseph Heller"),
    Book("The Sun Also Rises", 251, "Fiction", "Ernest Hemingway"),
    Book("Slaughterhouse-Five", 275, "Science Fiction", "Kurt Vonnegut"),
    Book("One Hundred Years of Solitude", 417, "Magic Realism", "Gabriel Garcia Marquez"),
    Book("Love in the Time of Cholera", 348, "Romance", "Gabriel Garcia Marquez"),
    Book("Beloved", 324, "Historical", "Toni Morrison"),
    Book("Invisible Man", 581, "Fiction", "Ralph Ellison"),
    Book("Gone with the Wind", 1037, "Historical", "Margaret Mitchell"),
    Book("The Catcher in the Rye", 214, "Fiction", "J.D. Salinger"),
    Book("The Sound and the Fury", 326, "Fiction", "William Faulkner"),
    Book("Lolita", 336, "Fiction", "Vladimir Nabokov"),
    Book("The Stranger", 123, "Philosophical", "Albert Camus"),
    Book("The Trial", 255, "Philosophical", "Franz Kafka"),
    Book("The Metamorphosis", 201, "Fiction", "Franz Kafka"),
    Book("Heart of Darkness", 164, "Fiction", "Joseph Conrad"),
    Book("The Master and Margarita", 384, "Fantasy", "Mikhail Bulgakov"),
    Book("The Wind-Up Bird Chronicle", 607, "Fiction", "Haruki Murakami"),
    Book("Norwegian Wood", 296, "Romance", "Haruki Murakami"),
    Book("Kafka on the Shore", 505, "Fiction", "Haruki Murakami"),
    Book("The Kite Runner", 371, "Fiction", "Khaled Hosseini"),
    Book("A Thousand Splendid Suns", 384, "Fiction", "Khaled Hosseini"),
    Book("Life of Pi", 319, "Adventure", "Yann Martel"),
    Book("The Road", 287, "Post-Apocalyptic", "Cormac McCarthy"),
    Book("Blood Meridian", 337, "Western", "Cormac McCarthy"),
    Book("All the Pretty Horses", 302, "Western", "Cormac McCarthy"),
    Book("No Country for Old Men", 309, "Thriller", "Cormac McCarthy"),
    Book("The Handmaid's Tale", 311, "Dystopian", "Margaret Atwood"),
    Book("Oryx and Crake", 376, "Dystopian", "Margaret Atwood"),
    Book("The Blind Assassin", 521, "Fiction", "Margaret Atwood"),
    Book("The Book Thief", 552, "Historical", "Markus Zusak"),
    Book("The Fault in Our Stars", 313, "Romance", "John Green"),
    Book("Looking for Alaska", 221, "Fiction", "John Green"),
    Book("Paper Towns", 305, "Fiction", "John Green"),
    Book("An Abundance of Katherines", 227, "Fiction", "John Green"),
    Book("The Hunger Games", 374, "Dystopian", "Suzanne Collins"),
    Book("Catching Fire", 391, "Dystopian", "Suzanne Collins"),
    Book("Mockingjay", 390, "Dystopian", "Suzanne Collins"),
    Book("Divergent", 487, "Dystopian", "Veronica Roth"),
    Book("Insurgent", 525, "Dystopian", "Veronica Roth"),
    Book("Allegiant", 526, "Dystopian", "Veronica Roth"),
    Book("The Maze Runner", 375, "Dystopian", "James Dashner"),
    Book("The Scorch Trials", 361, "Dystopian", "James Dashner"),
    Book("The Death Cure", 325, "Dystopian", "James Dashner"),
    Book("The Giver", 240, "Dystopian", "Lois Lowry"),
    Book("Gathering Blue", 241, "Dystopian", "Lois Lowry"),
    Book("Messenger", 169, "Dystopian", "Lois Lowry"),
    Book("Son", 393, "Dystopian", "Lois Lowry"),
    Book("Ender's Game", 324, "Science Fiction", "Orson Scott Card"),
    Book("Speaker for the Dead", 415, "Science Fiction", "Orson Scott Card"),
    Book("Xenocide", 592, "Science Fiction", "Orson Scott Card"),
    Book("Children of the Mind", 370, "Science Fiction", "Orson Scott Card"),
    Book("Dune", 412, "Science Fiction", "Frank Herbert"),
    Book("Dune Messiah", 256, "Science Fiction", "Frank Herbert"),
    Book("Children of Dune", 444, "Science Fiction", "Frank Herbert"),
    Book("God Emperor of Dune", 496, "Science Fiction", "Frank Herbert"),
    Book("Heretics of Dune", 480, "Science Fiction", "Frank Herbert"),
    Book("Chapterhouse: Dune", 464, "Science Fiction", "Frank Herbert"),
    Book("The Hitchhiker's Guide to the Galaxy", 193, "Science Fiction", "Douglas Adams"),
    Book("The Restaurant at the End of the Universe", 208, "Science Fiction", "Douglas Adams"),
    Book("Life, the Universe and Everything", 240, "Science Fiction", "Douglas Adams"),
    Book("So Long, and Thanks for All the Fish", 191, "Science Fiction", "Douglas Adams"),
    Book("Mostly Harmless", 230, "Science Fiction", "Douglas Adams"),
    Book("The Girl with the Dragon Tattoo", 465, "Thriller", "Stieg Larsson"),
    Book("The Girl Who Played with Fire", 503, "Thriller", "Stieg Larsson"),
    Book("The Girl Who Kicked the Hornet's Nest", 563, "Thriller", "Stieg Larsson"),
    Book("The Da Vinci Code", 489, "Thriller", "Dan Brown"),
    Book("Angels & Demons", 616, "Thriller", "Dan Brown"),
    Book("Inferno", 480, "Thriller", "Dan Brown"),
    Book("The Lost Symbol", 509, "Thriller", "Dan Brown")
] 