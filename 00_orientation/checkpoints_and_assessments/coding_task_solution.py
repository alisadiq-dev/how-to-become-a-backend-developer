"""
Coding Task Solution: Library Class Implementation

This is the complete solution with explanations.
"""

class Book:
    def __init__(self, title, author, isbn):
        """Initialize a book with title, author, and ISBN"""
        self.title = title
        self.author = author
        self.isbn = isbn
    
    def __str__(self):
        """Return string representation of the book"""
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"


class Library:
    def __init__(self):
        """Initialize library with empty book list"""
        self.books = []
    
    def add_book(self, book):
        """Add a book to the library"""
        self.books.append(book)
        print(f"Added: {book.title}")
    
    def remove_book(self, isbn):
        """Remove a book by ISBN"""
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"Removed: {book.title}")
                return
        print("Book not found")
    
    def search_book(self, title):
        """Search for a book by title (case-insensitive)"""
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None
    
    def display_books(self):
        """Display all books in the library"""
        if not self.books:
            print("No books in library")
            return
        
        for book in self.books:
            print(f"- {book}")


# Test the implementation
if __name__ == "__main__":
    # Create a library
    library = Library()
    
    # Create some books
    book1 = Book("Python Basics", "John Smith", "123")
    book2 = Book("Data Structures", "Jane Doe", "456")
    book3 = Book("Algorithms", "Bob Johnson", "789")
    
    # Add books
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    
    # Display all books
    print("\nAll books:")
    library.display_books()
    
    # Search for a book
    print("\nSearching for 'Python Basics':")
    found = library.search_book("Python Basics")
    if found:
        print(f"Found: {found}")
    
    # Remove a book
    print("\nRemoving book with ISBN 456:")
    library.remove_book("456")
    
    # Display books after removal
    print("\nBooks after removal:")
    library.display_books()


"""
Expected Output:
----------------
Added: Python Basics
Added: Data Structures
Added: Algorithms

All books:
- Python Basics by John Smith (ISBN: 123)
- Data Structures by Jane Doe (ISBN: 456)
- Algorithms by Bob Johnson (ISBN: 789)

Searching for 'Python Basics':
Found: Python Basics by John Smith (ISBN: 123)

Removing book with ISBN 456:
Removed: Data Structures

Books after removal:
- Python Basics by John Smith (ISBN: 123)
- Algorithms by Bob Johnson (ISBN: 789)


Key Concepts Used:
------------------
1. Classes and Objects
   - Book class represents a book entity
   - Library class manages a collection of books

2. __init__ method
   - Initializes object attributes
   - Called automatically when creating an object

3. Instance attributes
   - self.title, self.author, self.isbn for Book
   - self.books list for Library

4. Methods
   - add_book(): Adds book to list
   - remove_book(): Removes book by ISBN
   - search_book(): Finds book by title
   - display_books(): Shows all books

5. __str__ method
   - Defines how object is printed
   - Returns formatted string

6. List operations
   - append(): Add to list
   - remove(): Remove from list
   - Iteration with for loop

7. String methods
   - .lower(): Convert to lowercase for case-insensitive search

8. Conditional logic
   - if/else statements
   - Checking if list is empty
"""
