from models.book import Book
from models.user import StudentUserType, TeacherUserType
from repositories.repository import BookRepository, UserRepository
from adapters.external_catalog_adapter import ExternalCatalogAdapter
from core.library_mediator import LibraryMediator

class LibraryFacade:
    def __init__(self):
        self.books = BookRepository('data/books.json')
        self.users = UserRepository('data/users.json')
        self.catalog_adapter = ExternalCatalogAdapter()
        self.mediator = LibraryMediator(self)

    def add_book(self, id, title, author, category, year):
        book = Book(id, title, author, category, year)
        self.books.add(id, book.__dict__)

    def add_user(self, id, name, user_type):
        if user_type == 'student':
            user = StudentUserType(id, name)
        elif user_type == 'teacher':
            user = TeacherUserType(id, name)
        else:
            raise ValueError("Invalid user type")
        self.users.add(id, user.__dict__)

    def borrow_book(self, user_id, book_id):
        return self.mediator.borrow_book(user_id, book_id)

    def return_book(self, user_id, book_id):
        return self.mediator.return_book(user_id, book_id)

    def search_books(self, criteria, value):
        return self.catalog_adapter.search_books(criteria, value)

    def get_book_info(self, book_id):
        return self.books.get(book_id)

    def get_user_info(self, user_id):
        return self.users.get(user_id)
    
    def add_borrowed_book(self, user_id, book_id):
        return self.users.add_borrowed_book(user_id, book_id)
    
    def remove_borrowed_book(self, user_id, book_id):
        return self.users.remove_borrowed_book(user_id, book_id)
    
    def set_borrowed(self, book_id, borrowed):
        return self.books.set_borrowed(book_id, borrowed)
