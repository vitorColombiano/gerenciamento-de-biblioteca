from core.library_facade import LibraryFacade

class LibraryCLI:
    def __init__(self):
        self.library = LibraryFacade()

    def display_menu(self):
        print("1. Add Book")
        print("2. Add User")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Search Books")
        print("6. Get Book Info")
        print("7. Get User Info")
        print("8. Exit")

    def add_book(self):
        id = input("Book ID: ")
        title = input("Title: ")
        author = input("Author: ")
        category = input("Category: ")
        year = input("Year: ")
        self.library.add_book(id, title, author, category, year)
        print("Book added successfully.")

    def add_user(self):
        id = input("User ID: ")
        name = input("Name: ")
        user_type = input("User Type (student/teacher): ")
        self.library.add_user(id, name, user_type)
        print("User added successfully.")

    def borrow_book(self):
        user_id = input("User ID: ")
        book_id = input("Book ID: ")
        if self.library.borrow_book(user_id, book_id):
            print("Book borrowed successfully.")
        else:
            print("Failed to borrow book.")

    def return_book(self):
        user_id = input("User ID: ")
        book_id = input("Book ID: ")
        if self.library.return_book(user_id, book_id):
            print("Book returned successfully.")
        else:
            print("Failed to return book.")

    def search_books(self):
        criteria = input("Search by (title/author/category): ")
        value = input(f"Enter {criteria}: ")
        books = self.library.search_books(criteria, value)
        for book in books:
            print(book)

    def get_book_info(self):
        book_id = input("Book ID: ")
        book_info = self.library.get_book_info(book_id)
        if book_info:
            print(book_info)
        else:
            print("Book not found.")

    def get_user_info(self):
        user_id = input("User ID: ")
        user_info = self.library.get_user_info(user_id)
        if user_info:
            print(user_info)
        else:
            print("User not found.")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Choose an option: ")

            if choice == '1':
                self.add_book()
            elif choice == '2':
                self.add_user()
            elif choice == '3':
                self.borrow_book()
            elif choice == '4':
                self.return_book()
            elif choice == '5':
                self.search_books()
            elif choice == '6':
                self.get_book_info()
            elif choice == '7':
                self.get_user_info()
            elif choice == '8':
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    cli = LibraryCLI()
    cli.run()
