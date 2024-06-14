# Simplified Library Management System

class Book:
    """Represents a book in the library."""

    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True  

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Available: {self.available}"


class Library:
    """Manages a collection of books."""

    def __init__(self):
        self.books = []

    def add_book(self, book):
        """Adds a book to the library collection."""
        self.books.append(book)
        print(f"Book '{book.title}' added successfully.")

    def remove_book(self, isbn):
        """Removes a book from the library collection by ISBN."""
        for index, book in enumerate(self.books):
            if book.isbn == isbn:
                self.books.pop(index)
                print(f"Book '{book.title}' removed from the library.")
                return
        print(f"Book with ISBN {isbn} not found in the library.")

    def list_books(self):
        """Prints a list of all books in the library."""
        if not self.books:
            print("No books available in the library.")
        else:
            print("** Available Books **")
            for book in self.books:
                print(book)

    def borrow_book(self, isbn):
        """Attempts to borrow a book by ISBN."""
        for book in self.books:
            if book.isbn == isbn:
                if book.available:
                    book.available = False
                    print(f"Book '{book.title}' borrowed successfully.")
                    return
                else:
                    print(f"Book '{book.title}' is already borrowed.")
                return
        print(f"Book with ISBN {isbn} not found in the library.")

    def return_book(self, isbn):
        """Attempts to return a book by ISBN."""
        for book in self.books:
            if book.isbn == isbn:
                if not book.available:
                    book.available = True
                    print(f"Book '{book.title}' returned successfully.")
                    return
                else:
                    print(f"Book '{book.title}' is already available.")
                return
        print(f"Book with ISBN {isbn} not found in the library.")


def main():
    """The main function that runs the library management system."""
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter book ISBN: ")
            book = Book(title, author, isbn)
            library.add_book(book)

        elif choice == '2':
            isbn = input("Enter book ISBN to remove: ")
            library.remove_book(isbn)

        elif choice == '3':
            library.list_books()

        elif choice == '4':
            isbn = input("Enter book ISBN to borrow: ")
            library.borrow_book(isbn)

        elif choice == '5':
            isbn = input("Enter book ISBN to return: ")
            library.return_book(isbn)

        elif choice == '6':
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
