class BookRecommender:
    """
    BookRecommender class provides methods to recommend books to a reader based on their preferences and enhance the recommendations based on feedback.
    Methods:
        recommend_books(cls, books, reader):
            Recommends books to the reader based on their preferred author, genre, or length.
            Parameters:
                books (list): List of book objects to consider for recommendation.
                reader (object): Reader object containing preferences and feedback methods.
        enhance_recommendation(cls, feedback, name):
            Enhances the book recommendations based on the reader's feedback.
            Parameters:
                feedback (list): List of tuples containing book objects and their likeliness score (1 to 3).
                name (str): Name of the reader to personalize the recommendation messages.
    """

    @classmethod
    def recommend_books(cls, books, reader):
        books_to_recommend = []
        for book in books:
            if book.author == reader.preferred_author or book.genre == reader.preferred_genre or book.length() == reader.preferred_length:
               books_to_recommend.append(book)
        cls.enhance_recommendation(reader.give_feedback(books_to_recommend), reader.name)
    
    @classmethod
    def enhance_recommendation(cls, feedback, name):
        love = []
        like = []
        trying = []
        print()
        print("Enhancing recommendation based on your feedback...")
        print()
        for book, likeliness in feedback:
            if likeliness == 3:
                love.append(book)
            elif likeliness == 2:
                like.append(book)
            elif likeliness == 1:
                trying.append(book)
        if love:
            print(f'You will LOVE these books {name}:')
            for book in love:
                print(book)
        print()
        if like:
            print(f'You could like these books {name}:')
            for book in like:
                print(book)
        print()
        if trying:
            print(f'You might want to give these books a try {name}: ')
            for book in trying:
                print(book)
        print()