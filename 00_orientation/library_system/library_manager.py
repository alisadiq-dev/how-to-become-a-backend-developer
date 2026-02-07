"""
Library Management System

A Python application demonstrating:
- Object-Oriented Programming (OOP) with multiple classes
- Complex data relationships (books, members, borrowing)
- Business logic and validation rules
- File I/O with JSON
- Exception handling
- CRUD operations
"""

import json
from typing import List, Optional, Dict


class Book:
    """
    Represents a book in the library.
    
    Attributes:
        title (str): Book title
        author (str): Author name
        isbn (str): ISBN number (unique identifier)
        category (str): Book category/genre
        is_available (bool): Availability status
    """
    
    def __init__(self, title: str, author: str, isbn: str, category: str):
        """Initialize a new Book object."""
        if not all([title, author, isbn, category]):
            raise ValueError("All book fields must be provided")
        
        self.title = title
        self.author = author
        self.isbn = isbn
        self.category = category
        self.is_available = True
    
    def to_dict(self) -> Dict:
        """Convert book to dictionary for JSON serialization."""
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "category": self.category,
            "is_available": self.is_available
        }
    
    def __str__(self) -> str:
        """String representation of book."""
        status = "Available" if self.is_available else "Borrowed"
        return f"'{self.title}' by {self.author} [{self.category}] - {status}"


class Member:
    """
    Represents a library member.
    
    Attributes:
        name (str): Member's full name
        member_id (str): Unique member ID
        email (str): Email address
        borrowed_books (list): List of borrowed book ISBNs
    """
    
    def __init__(self, name: str, member_id: str, email: str):
        """Initialize a new Member object."""
        if not all([name, member_id, email]):
            raise ValueError("All member fields must be provided")
        
        if "@" not in email:
            raise ValueError("Invalid email format")
        
        self.name = name
        self.member_id = member_id
        self.email = email
        self.borrowed_books: List[str] = []
    
    def borrow_book(self, isbn: str) -> None:
        """Add a book to member's borrowed list."""
        if isbn not in self.borrowed_books:
            self.borrowed_books.append(isbn)
    
    def return_book(self, isbn: str) -> None:
        """Remove a book from member's borrowed list."""
        if isbn in self.borrowed_books:
            self.borrowed_books.remove(isbn)
    
    def can_borrow_more(self) -> bool:
        """Check if member can borrow more books (max 3)."""
        return len(self.borrowed_books) < 3
    
    def to_dict(self) -> Dict:
        """Convert member to dictionary for JSON serialization."""
        return {
            "name": self.name,
            "member_id": self.member_id,
            "email": self.email,
            "borrowed_books": self.borrowed_books
        }
    
    def __str__(self) -> str:
        """String representation of member."""
        book_count = len(self.borrowed_books)
        return f"{self.name} (ID: {self.member_id}) - {book_count} book(s) borrowed"


class Library:
    """
    Manages the library system including books, members, and borrowing.
    """
    
    def __init__(self, filename: str = "library_data.json"):
        """Initialize the library system."""
        self.books: List[Book] = []
        self.members: List[Member] = []
        self.filename = filename
    
    def add_book(self, book: Book) -> None:
        """Add a new book to the library."""
        if any(b.isbn == book.isbn for b in self.books):
            raise ValueError(f"Book with ISBN {book.isbn} already exists")
        
        self.books.append(book)
        print(f"Added book: {book.title}")
    
    def remove_book(self, isbn: str) -> None:
        """Remove a book from the library."""
        book = self._find_book_by_isbn(isbn)
        if book:
            if not book.is_available:
                print(f"Cannot remove '{book.title}' - currently borrowed")
                return
            
            self.books.remove(book)
            print(f"Removed book: {book.title}")
        else:
            print(f"Book with ISBN {isbn} not found")
    
    def search_books(self, query: str, search_by: str = "title") -> List[Book]:
        """Search for books by title, author, or category."""
        query_lower = query.lower()
        results = []
        
        for book in self.books:
            if search_by == "title" and query_lower in book.title.lower():
                results.append(book)
            elif search_by == "author" and query_lower in book.author.lower():
                results.append(book)
            elif search_by == "category" and query_lower in book.category.lower():
                results.append(book)
        
        return results
    
    def view_all_books(self) -> None:
        """Display all books in the library."""
        if not self.books:
            print("No books in the library.")
            return
        
        print("\n" + "="*70)
        print("ALL BOOKS IN LIBRARY")
        print("="*70)
        
        for i, book in enumerate(self.books, 1):
            print(f"{i}. {book}")
        
        print("="*70 + "\n")
    
    def get_available_books(self) -> List[Book]:
        """Get list of available books."""
        return [book for book in self.books if book.is_available]
    
    def get_borrowed_books(self) -> List[Book]:
        """Get list of borrowed books."""
        return [book for book in self.books if not book.is_available]
    
    def register_member(self, member: Member) -> None:
        """Register a new library member."""
        if any(m.member_id == member.member_id for m in self.members):
            raise ValueError(f"Member ID {member.member_id} already exists")
        
        self.members.append(member)
        print(f"Registered member: {member.name}")
    
    def remove_member(self, member_id: str) -> None:
        """Remove a member from the library."""
        member = self._find_member_by_id(member_id)
        if member:
            if member.borrowed_books:
                print(f"Cannot remove {member.name} - has borrowed books")
                return
            
            self.members.remove(member)
            print(f"Removed member: {member.name}")
        else:
            print(f"Member with ID {member_id} not found")
    
    def search_member(self, query: str) -> Optional[Member]:
        """Search for a member by ID or name."""
        # Search by ID first
        for member in self.members:
            if member.member_id == query:
                return member
        
        # Search by name
        query_lower = query.lower()
        for member in self.members:
            if query_lower in member.name.lower():
                return member
        
        return None
    
    def view_all_members(self) -> None:
        """Display all library members."""
        if not self.members:
            print("No members registered.")
            return
        
        print("\n" + "="*70)
        print("ALL LIBRARY MEMBERS")
        print("="*70)
        
        for i, member in enumerate(self.members, 1):
            print(f"{i}. {member}")
        
        print("="*70 + "\n")
    
    def borrow_book(self, member_id: str, isbn: str) -> None:
        """Process a book borrowing transaction."""
        member = self._find_member_by_id(member_id)
        book = self._find_book_by_isbn(isbn)
        
        if not member:
            print(f"Member ID {member_id} not found")
            return
        
        if not book:
            print(f"Book with ISBN {isbn} not found")
            return
        
        if not book.is_available:
            print(f"'{book.title}' is currently borrowed")
            return
        
        if not member.can_borrow_more():
            print(f"{member.name} has reached the borrowing limit (3 books)")
            return
        
        # Process borrowing
        book.is_available = False
        member.borrow_book(isbn)
        
        print(f"{member.name} borrowed '{book.title}'")
        print(f"Books borrowed: {len(member.borrowed_books)}/3")
    
    def return_book(self, member_id: str, isbn: str) -> None:
        """Process a book return transaction."""
        member = self._find_member_by_id(member_id)
        book = self._find_book_by_isbn(isbn)
        
        if not member:
            print(f"Member ID {member_id} not found")
            return
        
        if not book:
            print(f"Book with ISBN {isbn} not found")
            return
        
        if isbn not in member.borrowed_books:
            print(f"{member.name} hasn't borrowed '{book.title}'")
            return
        
        # Process return
        book.is_available = True
        member.return_book(isbn)
        
        print(f"{member.name} returned '{book.title}'")
        print(f"Books borrowed: {len(member.borrowed_books)}/3")
    
    def get_member_books(self, member_id: str) -> List[Book]:
        """Get all books borrowed by a member."""
        member = self._find_member_by_id(member_id)
        if not member:
            return []
        
        return [self._find_book_by_isbn(isbn) for isbn in member.borrowed_books]
    
    def get_statistics(self) -> Dict:
        """Calculate library statistics."""
        available = len(self.get_available_books())
        borrowed = len(self.get_borrowed_books())
        
        # Count books by category
        categories = {}
        for book in self.books:
            categories[book.category] = categories.get(book.category, 0) + 1
        
        # Find most popular category
        popular_category = max(categories.items(), key=lambda x: x[1])[0] if categories else "N/A"
        
        # Count members with borrowed books
        active_members = sum(1 for m in self.members if m.borrowed_books)
        
        return {
            "total_books": len(self.books),
            "available_books": available,
            "borrowed_books": borrowed,
            "total_members": len(self.members),
            "active_members": active_members,
            "categories": categories,
            "popular_category": popular_category
        }
    
    def save_to_file(self, filename: Optional[str] = None) -> None:
        """Save library data to JSON file."""
        if filename is None:
            filename = self.filename
        
        try:
            data = {
                "books": [book.to_dict() for book in self.books],
                "members": [member.to_dict() for member in self.members]
            }
            
            with open(filename, 'w') as file:
                json.dump(data, file, indent=2)
            
            print(f"Saved {len(self.books)} books and {len(self.members)} members to {filename}")
        
        except Exception as e:
            print(f"Error saving to file: {e}")
    
    def load_from_file(self, filename: Optional[str] = None) -> None:
        """Load library data from JSON file."""
        if filename is None:
            filename = self.filename
        
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
            
            # Clear current data
            self.books = []
            self.members = []
            
            # Load books
            for book_data in data.get('books', []):
                book = Book(
                    title=book_data['title'],
                    author=book_data['author'],
                    isbn=book_data['isbn'],
                    category=book_data['category']
                )
                book.is_available = book_data['is_available']
                self.books.append(book)
            
            # Load members
            for member_data in data.get('members', []):
                member = Member(
                    name=member_data['name'],
                    member_id=member_data['member_id'],
                    email=member_data['email']
                )
                member.borrowed_books = member_data['borrowed_books']
                self.members.append(member)
            
            print(f"Loaded {len(self.books)} books and {len(self.members)} members from {filename}")
        
        except FileNotFoundError:
            print(f"File '{filename}' not found. Starting with empty library.")
        
        except json.JSONDecodeError:
            print(f"Error reading '{filename}'. File may be corrupted.")
        
        except Exception as e:
            print(f"Unexpected error loading file: {e}")
    
    def _find_book_by_isbn(self, isbn: str) -> Optional[Book]:
        """Find a book by ISBN."""
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None
    
    def _find_member_by_id(self, member_id: str) -> Optional[Member]:
        """Find a member by ID."""
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None


if __name__ == "__main__":
    print("Library Management System")
    print("="*50)
    print("\nThis is the main module. Import it to use the classes.")
    print("\nQuick start:")
    print("  from library_manager import Book, Member, Library")
    print("\nOr run: python3 example_usage.py")
    print("="*50)
