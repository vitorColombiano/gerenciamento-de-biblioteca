class Book:
    def __init__(self, id, title, author, category, year):
        self.id = id
        self.title = title
        self.author = author
        self.category = category
        self.year = year
        self.available = True  # Assume que o livro está inicialmente disponível
        self.is_borrowed = False  # Novo atributo para verificar se o livro está emprestado

    def borrow(self):
        if not self.available:
            return False  # Livro já está emprestado
        self.available = False
        self.is_borrowed = True  # Marca o livro como emprestado
        return True

    def return_book(self):
        self.available = True
        self.is_borrowed = False  # Marca o livro como não emprestado ao ser devolvido
