class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.id} - {self.name}"

class StudentUserType(User):
    def __init__(self, id, name):
        super().__init__(id, name)

class TeacherUserType(User):
    def __init__(self, id, name):
        super().__init__(id, name)
