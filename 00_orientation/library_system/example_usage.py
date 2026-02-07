"""
Example Usage - Library Management System

This script demonstrates all features of the Library Management System.

Usage:
    python3 example_usage.py
"""

from library_manager import Book, Member, Library


def print_section(title):
    """Helper function to print section headers"""
    print("\n" + "="*70)
    print(f"  {title}")
    print("="*70)


def main():
    """Main function demonstrating all features."""
    
    print("\nLIBRARY MANAGEMENT SYSTEM - DEMO")
    print("="*70)
    print("This demo shows all features of the library system.\n")
    
    # Create library
    print_section("1. Creating Library System")
    library = Library()
    print("Library system created successfully!")
    
    # Add books
    print_section("2. Adding Books to Library")
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "978-0-7432-7356-5", "Fiction")
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "978-0-06-112008-4", "Fiction")
    book3 = Book("1984", "George Orwell", "978-0-452-28423-4", "Fiction")
    book4 = Book("Sapiens", "Yuval Noah Harari", "978-0-06-231609-7", "Non-Fiction")
    book5 = Book("Educated", "Tara Westover", "978-0-399-59050-4", "Non-Fiction")
    book6 = Book("Python Crash Course", "Eric Matthes", "978-1-59327-928-8", "Programming")
    
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    library.add_book(book4)
    library.add_book(book5)
    library.add_book(book6)
    
    # View all books
    print_section("3. Viewing All Books")
    library.view_all_books()
    
    # Register members
    print_section("4. Registering Library Members")
    member1 = Member("Ali Sadiq", "M001", "ali@example.com")
    member2 = Member("Sara Ahmed", "M002", "sara@example.com")
    member3 = Member("Ahmed Khan", "M003", "ahmed@example.com")
    
    library.register_member(member1)
    library.register_member(member2)
    library.register_member(member3)
    
    # View all members
    print_section("5. Viewing All Members")
    library.view_all_members()
    
    # Search books
    print_section("6. Searching for Books")
    print("\nSearching by title: 'Python'")
    results = library.search_books("Python", "title")
    for book in results:
        print(f"   Found: {book}")
    
    print("\nSearching by author: 'Orwell'")
    results = library.search_books("Orwell", "author")
    for book in results:
        print(f"   Found: {book}")
    
    print("\nSearching by category: 'Fiction'")
    results = library.search_books("Fiction", "category")
    print(f"   Found {len(results)} fiction books")
    
    # Borrow books
    print_section("7. Borrowing Books")
    print("\nAli borrows 'The Great Gatsby'")
    library.borrow_book("M001", "978-0-7432-7356-5")
    
    print("\nAli borrows '1984'")
    library.borrow_book("M001", "978-0-452-28423-4")
    
    print("\nSara borrows 'Sapiens'")
    library.borrow_book("M002", "978-0-06-231609-7")
    
    print("\nAhmed borrows 'Python Crash Course'")
    library.borrow_book("M003", "978-1-59327-928-8")
    
    # View books after borrowing
    print_section("8. Books Status After Borrowing")
    library.view_all_books()
    
    # Testing borrowing rules
    print_section("9. Testing Borrowing Rules")
    print("\nSara tries to borrow '1984' (already borrowed by Ali)")
    library.borrow_book("M002", "978-0-452-28423-4")
    
    print("\nAli borrows 'Educated' (3rd book)")
    library.borrow_book("M001", "978-0-399-59050-4")
    
    print("\nAli tries to borrow 4th book (exceeds limit)")
    library.borrow_book("M001", "978-0-06-112008-4")
    
    # View member's borrowed books
    print_section("10. Viewing Member's Borrowed Books")
    print("\nAli's borrowed books:")
    ali_books = library.get_member_books("M001")
    for book in ali_books:
        print(f"   - {book.title}")
    
    # Return books
    print_section("11. Returning Books")
    print("\nAli returns 'The Great Gatsby'")
    library.return_book("M001", "978-0-7432-7356-5")
    
    print("\nSara returns 'Sapiens'")
    library.return_book("M002", "978-0-06-231609-7")
    
    # Available vs borrowed books
    print_section("12. Available vs Borrowed Books")
    available = library.get_available_books()
    borrowed = library.get_borrowed_books()
    
    print(f"\nAvailable books: {len(available)}")
    for book in available:
        print(f"   - {book.title}")
    
    print(f"\nBorrowed books: {len(borrowed)}")
    for book in borrowed:
        print(f"   - {book.title}")
    
    # Library statistics
    print_section("13. Library Statistics")
    stats = library.get_statistics()
    print("\nLibrary Statistics:")
    print(f"   Total Books: {stats['total_books']}")
    print(f"   Available: {stats['available_books']}")
    print(f"   Borrowed: {stats['borrowed_books']}")
    print(f"   Total Members: {stats['total_members']}")
    print(f"   Active Members: {stats['active_members']}")
    print(f"   Most Popular Category: {stats['popular_category']}")
    
    print("\nBooks by Category:")
    for category, count in stats['categories'].items():
        print(f"   {category}: {count} book(s)")
    
    # Save to file
    print_section("14. Saving Data to File")
    library.save_to_file()
    
    # Load from file
    print_section("15. Loading Data from File")
    new_library = Library()
    print("Created new library (empty)")
    new_library.load_from_file()
    
    print("\nVerifying loaded data:")
    new_library.view_all_books()
    new_library.view_all_members()
    
    # Search member
    print_section("16. Searching for Members")
    print("\nSearching by ID: 'M001'")
    member = library.search_member("M001")
    if member:
        print(f"   Found: {member}")
    
    print("\nSearching by name: 'Sara'")
    member = library.search_member("Sara")
    if member:
        print(f"   Found: {member}")
    
    # Exception handling demo
    print_section("17. Exception Handling Demo")
    print("\nTrying to add book with empty title...")
    try:
        invalid_book = Book("", "Author", "123", "Fiction")
    except ValueError as e:
        print(f"Error caught: {e}")
    
    print("\nTrying to register member with invalid email...")
    try:
        invalid_member = Member("John Doe", "M999", "invalid-email")
    except ValueError as e:
        print(f"Error caught: {e}")
    
    print("\nTrying to add duplicate ISBN...")
    try:
        duplicate_book = Book("Duplicate", "Author", "978-0-7432-7356-5", "Fiction")
        library.add_book(duplicate_book)
    except ValueError as e:
        print(f"Error caught: {e}")
    
    # Remove book
    print_section("18. Removing Books")
    print("\nTrying to remove borrowed book...")
    library.remove_book("978-0-452-28423-4")  # 1984 (borrowed by Ali)
    
    print("\nRemoving available book...")
    library.remove_book("978-0-06-112008-4")  # To Kill a Mockingbird
    
    # Remove member
    print_section("19. Removing Members")
    print("\nTrying to remove member with borrowed books...")
    library.remove_member("M001")  # Ali has borrowed books
    
    print("\nRemoving member without borrowed books...")
    library.remove_member("M002")  # Sara returned all books
    
    # Final summary
    print_section("DEMO COMPLETE")
    print("\nWhat you learned:")
    print("   - Managing books and members with OOP")
    print("   - Complex borrowing system with validation rules")
    print("   - Searching and filtering data")
    print("   - Tracking availability and relationships")
    print("   - Calculating statistics")
    print("   - Saving and loading data with JSON")
    print("   - Exception handling for business rules")
    
    print("\nNext Steps:")
    print("   1. Open 'library_manager.py' and study the code")
    print("   2. Try adding your own books and members")
    print("   3. Modify the borrowing limit or add new features")
    print("   4. Create a similar system (e.g., Video Rental, Hotel Booking)")
    
    print("\nExtension Ideas:")
    print("   - Add due dates for borrowed books")
    print("   - Implement late fees")
    print("   - Add book reservations")
    print("   - Track borrowing history")
    print("   - Add book ratings and reviews")
    
    print("\n" + "="*70)
    print("Happy Learning!")
    print("="*70 + "\n")


if __name__ == "__main__":
    main()
