# Student Management System - Mini Project

## Overview

A beginner-friendly Python project that demonstrates all fundamental concepts covered in the orientation phase. This project integrates variables, data types, control flow, data structures, functions, and basic object-oriented programming.

## Learning Objectives

By completing this project, you will practice:

- Variables & Data Types - strings, integers, lists
- String Operations - f-strings, formatting
- Control Flow - if/else statements, loops
- Data Structures - lists, dictionaries
- Functions - defining and calling functions
- OOP Concepts - classes, objects, __init__, methods, self
- File I/O - reading/writing JSON files
- Exception Handling - try/except blocks
- List Comprehensions - filtering and transforming data

## Features

1. Add Student - Create new student records with name, age, and grades
2. View All Students - Display all students in the system
3. Search Student - Find a student by name
4. Update Grades - Modify a student's grades
5. Delete Student - Remove a student from the system
6. Calculate Average - Compute average grade for a student
7. Save to File - Persist data to JSON file
8. Load from File - Retrieve data from JSON file

## Project Structure

```
mini_project/
├── README.md              # This file
├── student_manager.py     # Main application code
├── example_usage.py       # Usage demonstrations
└── students.json          # Data storage (auto-created)
```

## Setup Instructions

### Prerequisites
- Python 3.11+ installed
- Basic understanding of Python syntax

### Installation

1. Navigate to the project directory:
   ```bash
   cd /Users/alisadiq/how-to-become-a-backend-developer/00_orientation/mini_project
   ```

2. No additional packages needed. This project uses only Python standard library.

## Usage

### Option 1: Run Example Usage Script

```bash
python3 example_usage.py
```

This will demonstrate all features with sample data.

### Option 2: Interactive Mode

```bash
python3 -i student_manager.py
```

Then in the Python REPL:

```python
# Create a student manager
manager = StudentManager()

# Create a student
student1 = Student("Ali", 20, [85, 90, 88])

# Add student to manager
manager.add_student(student1)

# View all students
manager.view_all_students()

# Search for a student
manager.search_student("Ali")

# Update grades
manager.update_grades("Ali", [90, 92, 89])

# Calculate average
manager.calculate_average("Ali")

# Save to file
manager.save_to_file()

# Load from file
manager.load_from_file()
```

### Option 3: Create Your Own Script

```python
from student_manager import Student, StudentManager

# Your code here
manager = StudentManager()
# ... add your logic
```

## Code Examples

### Creating Students

```python
# Create a student with name, age, and grades
student = Student("Sara", 19, [92, 88, 95])

# Access student attributes
print(student.name)        # Sara
print(student.age)         # 19
print(student.grades)      # [92, 88, 95]

# Calculate student's average
avg = student.get_average()
print(avg)                 # 91.67
```

### Managing Students

```python
# Create manager
manager = StudentManager()

# Add multiple students
manager.add_student(Student("Ali", 20, [85, 90, 88]))
manager.add_student(Student("Sara", 19, [92, 88, 95]))
manager.add_student(Student("Ahmed", 21, [78, 82, 80]))

# View all students
manager.view_all_students()

# Search for a specific student
manager.search_student("Ali")

# Update grades
manager.update_grades("Sara", [95, 90, 98])

# Delete a student
manager.delete_student("Ahmed")

# Save data
manager.save_to_file()
```

## Concepts Demonstrated

### 1. Object-Oriented Programming (OOP)

```python
class Student:
    def __init__(self, name, age, grades):
        self.name = name      # Instance attribute
        self.age = age        # Instance attribute
        self.grades = grades  # Instance attribute
```

Concepts:
- Classes as blueprints
- __init__ method for initialization
- self keyword for instance reference
- Instance attributes

### 2. Methods

```python
def get_average(self):
    """Calculate and return average grade"""
    if not self.grades:
        return 0
    return sum(self.grades) / len(self.grades)
```

Concepts:
- Methods are functions inside classes
- Accessing instance data with self
- Return values

### 3. Data Structures

```python
# List of Student objects
self.students = []

# Dictionary for JSON serialization
{
    "name": "Ali",
    "age": 20,
    "grades": [85, 90, 88]
}
```

Concepts:
- Lists for collections
- Dictionaries for key-value pairs

### 4. Control Flow

```python
# if/else statements
if age < 0:
    raise ValueError("Age cannot be negative")

# for loops
for student in self.students:
    print(student.name)

# List comprehensions
student = [s for s in self.students if s.name == name]
```

### 5. Exception Handling

```python
try:
    with open(filename, 'r') as file:
        data = json.load(file)
except FileNotFoundError:
    print("No saved data found")
except json.JSONDecodeError:
    print("Error reading file")
```

### 6. File I/O

```python
# Writing to file
with open('students.json', 'w') as file:
    json.dump(data, file, indent=2)

# Reading from file
with open('students.json', 'r') as file:
    data = json.load(file)
```

## Customization Ideas

Extend this project to practice more:

1. Add More Attributes
   - Add student_id, email, phone
   - Add enrollment_date

2. Add More Features
   - Sort students by name or average grade
   - Filter students by grade range
   - Export to CSV format
   - Add attendance tracking

3. Improve Validation
   - Email format validation
   - Grade range validation (0-100)
   - Duplicate name checking

4. Add Statistics
   - Class average
   - Highest/lowest grades
   - Grade distribution

5. Create a Menu System
   - Interactive command-line menu
   - User input for all operations

## Troubleshooting

### Issue: FileNotFoundError
Solution: The students.json file is created automatically when you save data. If you see this error, it means no data has been saved yet.

### Issue: JSONDecodeError
Solution: The JSON file might be corrupted. Delete students.json and run the program again.

### Issue: ValueError: Age cannot be negative
Solution: Make sure to provide a positive age when creating students.

### Issue: Student not found
Solution: Check the spelling of the student name. Names are case-sensitive.

## Practice Exercises

1. Basic Practice:
   - Create 5 students with different grades
   - Calculate and display each student's average
   - Find the student with the highest average

2. Intermediate Practice:
   - Add a method to find all students with average > 85
   - Add a method to sort students by name
   - Add a method to count total students

3. Advanced Practice:
   - Add a Course class with multiple subjects
   - Implement grade history (track grade changes)
   - Add data validation for all inputs

## Next Steps

After completing this project:

1. Review the code and understand each line
2. Modify the code to add new features
3. Create your own similar project (Library System, Inventory Manager, etc.)
4. Move on to the next phase of the roadmap (FastAPI Fundamentals)

## Related Orientation Notebooks

This project reinforces concepts from:
- 02_python_basics_syntax_&_types.ipynb - Variables, types, strings
- 03_control_flow.ipynb - if/else, loops, comprehensions
- 04_data_structures.ipynb - Lists, dictionaries
- 05_File_and_basic_scripts.ipynb - File I/O
- 06_exceptions_and_debugging.ipynb - Exception handling
- 09_Basic_OOP_concepts_introduction.ipynb - Classes, objects, methods

## Tips for Success

1. Read the Code: Start by reading student_manager.py carefully
2. Run Examples: Execute example_usage.py to see it in action
3. Experiment: Modify the code and see what happens
4. Add Comments: Add your own comments to explain what you learn
5. Build Your Own: Create a similar project from scratch

Happy Coding!