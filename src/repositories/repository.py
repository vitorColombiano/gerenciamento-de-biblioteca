import json

class BookRepository:
    def __init__(self, file_path='data/books.json'):
        self.file_path = file_path
        self.books = self.load_books()

    def load_books(self):
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_books(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.books, file, indent=4)

    def add(self, id, book):
        self.books.append(book)
        self.save_books()

    def get(self, book_id):
        for book in self.books:
            if book['id'] == book_id:
                return book
        return None
    
    def set_borrowed(self, book_id, borrowed):
        for book in self.books:
            if book['id'] == book_id:
                book['borrowed'] = borrowed
                self.save_books()
                return True
        return False

class UserRepository:
    def __init__(self, file_path='data/users.json'):
        self.file_path = file_path
        self.users = self.load_users()

    def load_users(self):
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_users(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.users, file, indent=4)

    def add(self, id, user):
        self.users.append(user)
        self.save_users()

    def get(self, user_id):
        for user in self.users:
            if user['id'] == user_id:
                return user
        return None

    def remove_borrowed_book(self, user_id, book_id):
        user = self.get(user_id)
        if user:
            if book_id in user['borrowed_books']:
                user['borrowed_books'].remove(book_id)
                self.save_users()
                return True
        return False

    def add_borrowed_book(self, user_id, book_id):
        user = self.get(user_id)
        if user:
            user['borrowed_books'].append(book_id)
            self.save_users()
            return True
        return False
