from handlers.handler import BookAvailabilityHandler, UserEligibilityHandler, LoanLimitHandler

class LibraryMediator:
    def __init__(self, facade):
        self.facade = facade

    def borrow_book(self, user_id, book_id):
        user = self.facade.get_user_info(user_id)
        book = self.facade.get_book_info(book_id)

        if not user or not book:
            return False

        # Handlers encadeados para verificar a possibilidade de empréstimo
        availability_handler = BookAvailabilityHandler(book)
        eligibility_handler = UserEligibilityHandler(user)
        limit_handler = LoanLimitHandler(user)

        availability_handler.set_next(eligibility_handler).set_next(limit_handler)

        if availability_handler.handle():
            if self.facade.add_borrowed_book(user_id, book_id) and self.facade.set_borrowed(book_id, True):
                return True

        return False

    def return_book(self, user_id, book_id):
        user = self.facade.get_user_info(user_id)
        book = self.facade.get_book_info(book_id)

        if user and book and self.facade.remove_borrowed_book(user_id, book_id) and self.facade.set_borrowed(book_id, False):
            return True

        return False
