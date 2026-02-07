# Library Management System

## Overview

A Python application demonstrating advanced programming concepts through a library management system. This project integrates multiple classes, complex business logic, data relationships, and validation rules.

## Learning Objectives

- Advanced OOP with multiple classes
- Complex business logic and validation
- Data relationships (books and members via borrowing)
- CRUD operations
- State management (availability tracking)
- File I/O with JSON
- Exception handling
- List comprehensions
- Type hints

## Features

### Book Management
- Add books with ISBN validation
- Remove books (if not borrowed)
- Search by title, author, or category
- View all books with availability status
- Track availability in real-time

### Member Management
- Register members with email validation
- Remove members (if no borrowed books)
- Search by ID or name
- View all members with borrow count

### Borrowing System
- Borrow available books
- Return borrowed books
- Max 3 books per member
- Availability checking
- View books borrowed by member

### Statistics & Reports
- Total books, available, borrowed
- Books by category
- Active members count
- Popular categories

### Data Persistence
- Save all data to JSON
- Load data on startup

## Project Structure

```
library_system/
├── README.md              # This file
├── library_manager.py     # Main application
├── example_usage.py       # Complete demonstration
└── library_data.json      # Auto-generated data file
```

## Setup

### Prerequisites
- Python 3.11+
- Basic understanding of Python and OOP

### Installation

Navigate to the project directory:
```bash
cd /Users/alisadiq/how-to-become-a-backend-developer/00_orientation/library_system
```

No additional packages needed - uses only Python standard library.

## Usage

### Run Demo

```bash
python3 example_usage.py
```

### Interactive Mode

```bash
python3 -i library_manager.py
```

Then:

```python
# Create library
library = Library()

# Add a book
book = Book("1984", "George Orwell", "978-0-452-28423-4", "Fiction")
library.add_book(book)

# Register a member
member = Member("Ali", "M001", "ali@example.com")
library.register_member(member)

# Borrow a book
library.borrow_book("M001", "978-0-452-28423-4")

# View all books
library.view_all_books()

# Save data
library.save_to_file()
```

## Code Examples

### Creating and Managing Books

```python
# Create books
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "978-0-7432-7356-5", "Fiction")
book2 = Book("Sapiens", "Yuval Noah Harari", "978-0-06-231609-7", "Non-Fiction")

# Add to library
library.add_book(book1)
library.add_book(book2)

# Search books
fiction_books = library.search_books("Fiction", "category")
orwell_books = library.search_books("Orwell", "author")

# View all books
library.view_all_books()
```

### Managing Members

```python
# Register members
member1 = Member("Ali Sadiq", "M001", "ali@example.com")
member2 = Member("Sara Ahmed", "M002", "sara@example.com")

library.register_member(member1)
library.register_member(member2)

# Search member
member = library.search_member("M001")
member = library.search_member("Ali")

# View all members
library.view_all_members()
```

### Borrowing and Returning

```python
# Borrow a book
library.borrow_book("M001", "978-0-7432-7356-5")

# Check member's borrowed books
books = library.get_member_books("M001")
for book in books:
    print(book.title)

# Return a book
library.return_book("M001", "978-0-7432-7356-5")

# View available books
available = library.get_available_books()
```

### Statistics

```python
# Get library statistics
stats = library.get_statistics()

print(f"Total Books: {stats['total_books']}")
print(f"Available: {stats['available_books']}")
print(f"Borrowed: {stats['borrowed_books']}")
print(f"Popular Category: {stats['popular_category']}")
```

## Concepts Demonstrated

### Multiple Classes with Relationships

```python
class Book:
    # Represents a book entity
    
class Member:
    # Represents a library member
    # Has relationship to books via borrowed_books list
    
class Library:
    # Manages both books and members
    # Coordinates relationships and business logic
```

### Complex Business Logic

```python
def borrow_book(self, member_id, isbn):
    # Multiple validation checks
    if not book.is_available:
        return
    
    if not member.can_borrow_more():
        return
    
    # Update both book and member state
    book.is_available = False
    member.borrow_book(isbn)
```

### Data Relationships

```python
# Member tracks borrowed books by ISBN
member.borrowed_books = ["978-0-7432-7356-5", "978-0-452-28423-4"]

# Library can find books from ISBNs
books = [library._find_book_by_isbn(isbn) for isbn in member.borrowed_books]
```

### Comprehensive Validation

```python
# Email validation
if "@" not in email:
    raise ValueError("Invalid email format")

# Duplicate prevention
if any(b.isbn == book.isbn for b in self.books):
    raise ValueError("ISBN already exists")

# Business rule enforcement
if len(member.borrowed_books) >= 3:
    print("Borrowing limit reached")
```

## Extension Ideas

### Easy
1. Add book copies tracking
2. Add book descriptions
3. Add publication year
4. Sort books by title, author, or category

### Medium
5. Add due dates for borrowed books
6. Calculate late fees
7. Implement reservation system
8. Track borrowing history
9. Add book ratings

### Advanced
10. Fine management system
11. Multiple library branches
12. Book recommendations
13. Export reports to CSV/PDF
14. Email notifications for due dates

## Troubleshooting

**ValueError: ISBN already exists**
- Each book must have a unique ISBN

**ValueError: Invalid email format**
- Email must contain '@' symbol

**Cannot borrow - limit reached**
- Members can borrow maximum 3 books

**Cannot remove book - currently borrowed**
- Books must be returned before removal

**FileNotFoundError**
- JSON file is created on first save

## Practice Exercises

### Beginner
1. Add 10 books from different categories
2. Register 5 members
3. Have each member borrow 2 books
4. Generate and print statistics

### Intermediate
1. Find all books by a specific author
2. Find members who haven't borrowed any books
3. Find the most active member
4. List all overdue books (requires adding due dates)

### Advanced
1. Implement a reservation system
2. Add borrowing history feature
3. Create recommendation system
4. Implement fine calculation for late returns

## Related Concepts

This project builds on:
- Python basics (variables, types)
- Control flow (if/else, loops)
- Data structures (lists, dictionaries)
- File I/O
- Exception handling
- OOP concepts (classes, objects, methods)

## Tips

1. Understand relationships between books and members
2. Follow the logic through borrowing/returning
3. Test edge cases
4. Read error messages carefully
5. Experiment with modifications

## Learning Path

1. Run example_usage.py
2. Read library_manager.py code
3. Try interactive mode
4. Create your own script
5. Add new features
