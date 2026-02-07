"""
Coding Task: Library Class Implementation

Task:
Create a Library class to manage books with the following features:
1. Add books
2. Remove books
3. Search for books by title

Requirements:
- Each book should have: title, author, and ISBN
- The Library class should store books in a list
- Implement methods: add_book(), remove_book(), and search_book()

Instructions:
1. Complete the Book class
2. Complete the Library class
3. Test your implementation with the provided test cases

Good luck!
"""

# TODO: Complete the Book class
class Book:
    def __init__(self, title, author, isbn):
        # Initialize book attributes
        pass
    
    def __str__(self):
        # Return a string representation of the book
        # Format: "Title by Author (ISBN: isbn)"
        pass


# TODO: Complete the Library class
class Library:
    def __init__(self):
        # Initialize an empty list to store books
        pass
    
    def add_book(self, book):
        # Add a book to the library
        # Print: "Added: [book title]"
        pass
    
    def remove_book(self, isbn):
        # Remove a book by ISBN
        # Print: "Removed: [book title]" if found
        # Print: "Book not found" if not found
        pass
    
    def search_book(self, title):
        # Search for a book by title (case-insensitive)
        # Return the book if found, None otherwise
        pass
    
    def display_books(self):
        # Display all books in the library
        # If no books, print: "No books in library"
        pass


# Test your implementation
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
