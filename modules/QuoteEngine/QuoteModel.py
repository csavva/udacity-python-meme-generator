class QuoteModel:

    def __init__(self, body, author):
        """ Initialize new QuoteModel. """
        self.body = body
        self.author = author

    def __repr__(self):
        """ String representation of the QuoteModel. """
        print(f"\"{self.body}\" - {self.author}")
