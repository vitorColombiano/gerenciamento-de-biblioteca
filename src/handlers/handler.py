class Handler:
    def __init__(self):
        self.next_handler = None

    def set_next(self, handler):
        self.next_handler = handler
        return handler

    def handle(self):
        if self.next_handler:
            return self.next_handler.handle()
        return True

class BookAvailabilityHandler(Handler):
    def __init__(self, book):
        super().__init__()
        self.book = book

    def handle(self):
        if not self.book.is_borrowed:  # Acessa o atributo 'available' do objeto Book
            return super().handle()
        return False

class UserEligibilityHandler(Handler):
    def __init__(self, user):
        super().__init__()
        self.user = user

    def handle(self):
        # Lógica de verificação de elegibilidade do usuário (exemplo: sempre true)
        return super().handle()

class LoanLimitHandler(Handler):
    def __init__(self, user):
        super().__init__()
        self.user = user

    def handle(self):
        if len(self.user.borrowed_books) < 5:  # Verifica o número de livros emprestados pelo usuário
            return super().handle()
        return False
