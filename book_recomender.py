class BookRecommender:
    """
    BookRecommender class provides methods to determine user preferences based on book correlations and recommend books accordingly.
    Methods:
        get_preferences(cls, correlations):
            Analyzes the given correlations to determine the preferred author, genre, and length of books.
            Parameters:
                correlations (list of tuples): A list where each tuple contains a book object and a likeliness score.
            Returns:
                tuple: A tuple containing the preferred author, genre, and length.
        recommend_books(cls, author, genre, length, books, name):
            Recommends books based on the user's preferred author, genre, and length.
            Parameters:
                author (str): The preferred author.
                genre (str): The preferred genre.
                length (str): The preferred length.
                books (list): A list of book objects to recommend from.
                name (str): The name of the user for personalized messages.
            Returns:
                None: Prints the recommended books categorized into 'love' and 'like'.
    """
    
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