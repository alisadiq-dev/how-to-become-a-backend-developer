"""
Student Management System - Mini Project
=========================================

A beginner-friendly Python application demonstrating fundamental programming concepts:
- Object-Oriented Programming (OOP)
- Data structures (lists, dictionaries)
- File I/O with JSON
- Exception handling
- CRUD operations

Author: Backend Engineering Roadmap
Purpose: Practice project for orientation phase
"""

import json
from typing import List, Optional


class Student:
    """
    Represents a student with name, age, and grades.
    
    This class demonstrates:
    - Class definition
    - __init__ method (constructor)
    - Instance attributes (self.name, self.age, self.grades)
    - Instance methods
    - Type hints
    """
    
    def __init__(self, name: str, age: int, grades: List[float]):
        """
        Initialize a new Student object.
        
        Args:
            name (str): Student's full name
            age (int): Student's age
            grades (list): List of grade scores (0-100)
        
        Raises:
            ValueError: If age is negative or grades are invalid
        """
        if age < 0:
            raise ValueError("Age cannot be negative")
        
        if not all(0 <= grade <= 100 for grade in grades):
            raise ValueError("Grades must be between 0 and 100")
        
        self.name = name
        self.age = age
        self.grades = grades
    
    def get_average(self) -> float:
        """
        Calculate and return the average grade.
        
        Returns:
            float: Average grade rounded to 2 decimal places
        """
        if not self.grades:
            return 0.0
        
        average = sum(self.grades) / len(self.grades)
        return round(average, 2)
    
    def add_grade(self, grade: float) -> None:
        """
        Add a new grade to the student's grade list.
        
        Args:
            grade (float): Grade to add (0-100)
        
        Raises:
            ValueError: If grade is not between 0 and 100
        """
        if not 0 <= grade <= 100:
            raise ValueError("Grade must be between 0 and 100")
        
        self.grades.append(grade)
    
    def to_dict(self) -> dict:
        """
        Convert student object to dictionary for JSON serialization.
        
        Returns:
            dict: Student data as dictionary
        """
        return {
            "name": self.name,
            "age": self.age,
            "grades": self.grades
        }
    
    def __str__(self) -> str:
        """
        String representation of student for printing.
        
        Returns:
            str: Formatted student information
        """
        avg = self.get_average()
        return f"Student: {self.name}, Age: {self.age}, Average: {avg}"


class StudentManager:
    """
    Manages a collection of students with CRUD operations.
    
    CRUD operations: Create, Read, Update, Delete
    """
    
    def __init__(self, filename: str = "students.json"):
        """
        Initialize the student manager.
        
        Args:
            filename (str): Name of JSON file for data persistence
        """
        self.students: List[Student] = []
        self.filename = filename
    
    def add_student(self, student: Student) -> None:
        """
        Add a new student to the manager.
        
        Args:
            student (Student): Student object to add
        """
        self.students.append(student)
        print(f"Added student: {student.name}")
    
    def view_all_students(self) -> None:
        """
        Display all students in the system.
        """
        if not self.students:
            print("No students in the system.")
            return
        
        print("\n" + "="*50)
        print("ALL STUDENTS")
        print("="*50)
        
        for i, student in enumerate(self.students, 1):
            print(f"{i}. {student}")
        
        print("="*50 + "\n")
    
    def search_student(self, name: str) -> Optional[Student]:
        """
        Search for a student by name.
        
        Args:
            name (str): Student name to search for
        
        Returns:
            Student or None: Found student or None if not found
        """
        found = [s for s in self.students if s.name.lower() == name.lower()]  
        
        if found:
            student = found[0]
            print(f"Found: {student}")
            return student
        else:
            print(f"Student '{name}' not found.")
            return None
    
    def update_grades(self, name: str, new_grades: List[float]) -> None:
        """
        Update a student's grades.
        
        Args:
            name (str): Student name
            new_grades (list): New list of grades
        """
        student = self.search_student(name)
        
        if student:
            if not all(0 <= grade <= 100 for grade in new_grades):
                print("All grades must be between 0 and 100")
                return
            
            student.grades = new_grades
            print(f"Updated grades for {name}")
            print(f"New average: {student.get_average()}")
    
    def delete_student(self, name: str) -> None:
        """
        Remove a student from the system.
        
        Args:
            name (str): Student name to delete
        """
        student = self.search_student(name)
        
        if student:
            self.students.remove(student)
            print(f"Deleted student: {name}")
    
    def calculate_average(self, name: str) -> Optional[float]:
        """
        Calculate and display a student's average grade.
        
        Args:
            name (str): Student name
        
        Returns:
            float or None: Average grade or None if student not found
        """
        student = self.search_student(name)
        
        if student:
            avg = student.get_average()
            print(f"{name}'s average: {avg}")
            return avg
        
        return None
    
    def get_class_statistics(self) -> dict:
        """
        Calculate statistics for all students.
        
        Returns:
            dict: Statistics including class average, highest, lowest
        """
        if not self.students:
            return {"message": "No students to calculate statistics"}
        
        averages = [s.get_average() for s in self.students]
        
        stats = {
            "total_students": len(self.students),
            "class_average": round(sum(averages) / len(averages), 2),
            "highest_average": max(averages),
            "lowest_average": min(averages)
        }
        
        return stats
    
    def save_to_file(self, filename: Optional[str] = None) -> None:
        """
        Save all students to a JSON file.
        
        Args:
            filename (str, optional): Custom filename (uses default if None)
        """
        if filename is None:
            filename = self.filename
        
        try:
            data = [student.to_dict() for student in self.students]
            
            with open(filename, 'w') as file:
                json.dump(data, file, indent=2)
            
            print(f"Saved {len(self.students)} student(s) to {filename}")
        
        except Exception as e:
            print(f"Error saving to file: {e}")
    
    def load_from_file(self, filename: Optional[str] = None) -> None:
        """
        Load students from a JSON file.
        
        Args:
            filename (str, optional): Custom filename (uses default if None)
        """
        if filename is None:
            filename = self.filename
        
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
            
            self.students = []
            
            for student_data in data:
                student = Student(
                    name=student_data['name'],
                    age=student_data['age'],
                    grades=student_data['grades']
                )
                self.students.append(student)
            
            print(f"Loaded {len(self.students)} student(s) from {filename}")
        
        except FileNotFoundError:
            print(f"File '{filename}' not found. Starting with empty student list.")
        
        except json.JSONDecodeError:
            print(f"Error reading '{filename}'. File may be corrupted.")
        
        except Exception as e:
            print(f"Unexpected error loading file: {e}")


if __name__ == "__main__":
    print("Student Management System")
    print("="*50)
    print("\nThis is the main module. Import it to use the classes.")
    print("\nQuick start:")
    print("  from student_manager import Student, StudentManager")
    print("\nOr run: python3 example_usage.py")
    print("="*50)