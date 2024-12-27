class Book:
    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available

    def check_out(self):
        if self.available:
            self.available = False
            return f"{self.title} has been checked out."
        else:
            return f"{self.title} is currently unavailable."

    def return_book(self):
        if not self.available:
            self.available = True
            return f"{self.title} has been returned."
        else:
            return f"{self.title} was not checked out."

class Library:
    def __init__(self):
        self.catalogue = []

    def add_book(self, book):
        self.catalogue.append(book)

    def view_catalogue(self):
        for book in self.catalogue:
            availability = "Available" if book.available else "Checked out"
            print(f"Title: {book.title}, Author: {book.author}, Status: {availability}")

def main():
    book1 = Book("1984", "George Orwell")
    book2 = Book("To Kill a Mockingbird", "Harper Lee", False)
    library = Library()
    library.add_book(book1)
    library.add_book(book2)

    print("Library Catalogue:")
    library.view_catalogue()

    print("\nChecking out '1984':")
    print(book1.check_out())

    print("\nReturning '1984':")
    print(book1.return_book())

    print("\nLibrary Catalogue After Transactions:")
    library.view_catalogue()

main()
