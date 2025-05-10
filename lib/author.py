class Author:
    all = []  # Class attribute to store all authors

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        from contract import Contract  # Import inside method to avoid circular import
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        from contract import Contract  # Import inside method to avoid circular import
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        from contract import Contract  # Import inside method to avoid circular import
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        from contract import Contract  # Import inside method to avoid circular import
        return sum(contract.royalties for contract in self.contracts())