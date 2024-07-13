class BookAvailabilityNotifier:
    def notify(self, user, book):
        print(f"Notification: {user['name']}, the book '{book['title']}' is now available.")
