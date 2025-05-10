from book import Book
from author import Author
from contract import Contract

# Example Usage
author1 = Author("Jane Austen")
book1 = Book("Pride and Prejudice")
contract1 = author1.sign_contract(book1, "2025-05-10", 5000)

print(f"{author1.name} has written '{book1.title}' and earns {contract1.royalties} in royalties.")