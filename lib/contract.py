from author import Author  # Import Author to resolve NameError
from book import Book  # Import Book for completeness

class Contract:
    all = []  # Class attribute to store all contracts

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise ValueError("Author must be an instance of Author class")
        if not isinstance(book, Book):
            raise ValueError("Book must be an instance of Book class")
        if not isinstance(date, str):
            raise ValueError("Date must be a string")
        if not isinstance(royalties, int):
            raise ValueError("Royalties must be an integer")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]