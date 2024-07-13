class ExternalCatalogAdapter:
    def __init__(self):
        # Simula uma integração com um sistema externo de catalogação de livros.
        self.external_books = [
            {"id": "101", "title": "External Book 1", "author": "Author A", "category": "Fiction", "year": 2020},
            {"id": "102", "title": "External Book 2", "author": "Author B", "category": "Non-Fiction", "year": 2019},
        ]

    def search_books(self, criteria, value):
        results = [book for book in self.external_books if book[criteria].lower() == value.lower()]
        return results
