class BookCategory:
    def __init__(self, name):
        self.name = name
        self.subcategories = {}

    def add_subcategory(self, subcategory):
        self.subcategories[subcategory.name] = subcategory

    def __str__(self):
        subcategories_str = ", ".join(self.subcategories.keys())
        return f"Category: {self.name}, Subcategories: [{subcategories_str}]"
