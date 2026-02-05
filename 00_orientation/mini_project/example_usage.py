"""
Example Usage - Student Management System
==========================================

This script demonstrates all features of the Student Management System.
Run this file to see the system in action!

Usage:
    python3 example_usage.py
"""

from student_manager import Student, StudentManager


def print_section(title):
    """Helper function to print section headers"""
    print("\n" + "="*60)
    print(f"  {title}")
    print("="*60)


def main():
    """
    Main function demonstrating all features of the Student Management System.
    """
    
    print("\n🎓 STUDENT MANAGEMENT SYSTEM - DEMO")
    print("="*60)
    print("This demo shows all features of the system.\n")
    
    # ========================================
    # 1. CREATE STUDENT MANAGER
    # ========================================
    print_section("1️⃣  Creating Student Manager")
    
    manager = StudentManager()
    print("✅ StudentManager created successfully!")
    
    # ========================================
    # 2. CREATE STUDENTS
    # ========================================
    print_section("2️⃣  Creating Students")
    
    # Create student objects with different data
    student1 = Student("Ali Sadiq", 20, [85, 90, 88, 92])
    student2 = Student("Sara Ahmed", 19, [92, 88, 95, 90])
    student3 = Student("Ahmed Khan", 21, [78, 82, 80, 85])
    student4 = Student("Fatima Ali", 20, [95, 98, 94, 96])
    
    print("✅ Created 4 student objects")
    
    # ========================================
    # 3. ADD STUDENTS TO MANAGER
    # ========================================
    print_section("3️⃣  Adding Students to Manager")
    
    manager.add_student(student1)
    manager.add_student(student2)
    manager.add_student(student3)
    manager.add_student(student4)
    
    # ========================================
    # 4. VIEW ALL STUDENTS
    # ========================================
    print_section("4️⃣  Viewing All Students")
    
    manager.view_all_students()
    
    # ========================================
    # 5. SEARCH FOR A STUDENT
    # ========================================
    print_section("5️⃣  Searching for a Student")
    
    print("\n🔍 Searching for 'Sara Ahmed'...")
    manager.search_student("Sara Ahmed")
    
    print("\n🔍 Searching for 'John Doe' (doesn't exist)...")
    manager.search_student("John Doe")
    
    # ========================================
    # 6. CALCULATE AVERAGE
    # ========================================
    print_section("6️⃣  Calculating Student Average")
    
    manager.calculate_average("Ali Sadiq")
    manager.calculate_average("Fatima Ali")
    
    # ========================================
    # 7. UPDATE GRADES
    # ========================================
    print_section("7️⃣  Updating Student Grades")
    
    print("\n📝 Updating Ahmed Khan's grades...")
    print("   Old grades: [78, 82, 80, 85]")
    print("   New grades: [85, 88, 90, 87]")
    manager.update_grades("Ahmed Khan", [85, 88, 90, 87])
    
    # ========================================
    # 8. ADD A NEW GRADE
    # ========================================
    print_section("8️⃣  Adding a New Grade")
    
    print("\n➕ Adding a new grade to Ali Sadiq...")
    student1.add_grade(94)
    print(f"✅ New grades: {student1.grades}")
    print(f"   New average: {student1.get_average()}")
    
    # ========================================
    # 9. CLASS STATISTICS
    # ========================================
    print_section("9️⃣  Class Statistics")
    
    stats = manager.get_class_statistics()
    print("\n📊 Class Statistics:")
    print(f"   Total Students: {stats['total_students']}")
    print(f"   Class Average: {stats['class_average']}")
    print(f"   Highest Average: {stats['highest_average']}")
    print(f"   Lowest Average: {stats['lowest_average']}")
    
    # ========================================
    # 10. SAVE TO FILE
    # ========================================
    print_section("🔟 Saving Data to File")
    
    manager.save_to_file()
    print("✅ Data saved to 'students.json'")
    
    # ========================================
    # 11. LOAD FROM FILE
    # ========================================
    print_section("1️⃣1️⃣  Loading Data from File")
    
    # Create a new manager to demonstrate loading
    new_manager = StudentManager()
    print("📂 Created new manager (empty)")
    
    # Load data from file
    new_manager.load_from_file()
    
    # Verify data was loaded
    print("\n✅ Verifying loaded data:")
    new_manager.view_all_students()
    
    # ========================================
    # 12. DELETE A STUDENT
    # ========================================
    print_section("1️⃣2️⃣  Deleting a Student")
    
    print("\n🗑️  Deleting 'Ahmed Khan'...")
    manager.delete_student("Ahmed Khan")
    
    print("\n📋 Students after deletion:")
    manager.view_all_students()
    
    # ========================================
    # 13. EXCEPTION HANDLING DEMO
    # ========================================
    print_section("1️⃣3️⃣  Exception Handling Demo")
    
    print("\n⚠️  Trying to create student with negative age...")
    try:
        invalid_student = Student("Invalid Student", -5, [80, 85])
    except ValueError as e:
        print(f"❌ Error caught: {e}")
    
    print("\n⚠️  Trying to add invalid grade...")
    try:
        student1.add_grade(150)  # Grade > 100
    except ValueError as e:
        print(f"❌ Error caught: {e}")
    
    # ========================================
    # FINAL SUMMARY
    # ========================================
    print_section("✅ DEMO COMPLETE!")
    
    print("\n📚 What you learned:")
    print("   ✅ Creating and managing Student objects")
    print("   ✅ Using StudentManager for CRUD operations")
    print("   ✅ Saving and loading data with JSON")
    print("   ✅ Exception handling for invalid inputs")
    print("   ✅ Calculating statistics and averages")
    
    print("\n🎯 Next Steps:")
    print("   1. Open 'student_manager.py' and read the code")
    print("   2. Try modifying this script to add your own students")
    print("   3. Create your own script using the classes")
    print("   4. Add new features (see README.md for ideas)")
    
    print("\n" + "="*60)
    print("🎓 Happy Learning!")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()
