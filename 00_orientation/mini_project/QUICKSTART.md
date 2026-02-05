# 🚀 Quick Start Guide

## For Absolute Beginners

If you're new to Python, follow these simple steps:

### Step 1: Open Terminal

On Mac, press `Cmd + Space`, type "Terminal", and press Enter.

### Step 2: Navigate to the Project

```bash
cd /Users/alisadiq/how-to-become-a-backend-developer/00_orientation/mini_project
```

### Step 3: Run the Demo

```bash
python3 example_usage.py
```

You'll see a complete demonstration of all features!

### Step 4: Explore the Code

Open the files in VS Code or any text editor:

```bash
code .
```

Or just open them manually:
- `student_manager.py` - Read the code and comments
- `example_usage.py` - See how to use the classes
- `README.md` - Full documentation

### Step 5: Try It Yourself

Create a new file called `my_test.py`:

```python
from student_manager import Student, StudentManager

# Create a manager
manager = StudentManager()

# Create your own student (use your name!)
my_student = Student("Your Name", 20, [85, 90, 95])

# Add to manager
manager.add_student(my_student)

# View it
manager.view_all_students()

# Save it
manager.save_to_file()

print("✅ You did it!")
```

Run it:
```bash
python3 my_test.py
```

---

## 🎯 What to Do Next

1. **Read the code** - Open `student_manager.py` and read every comment
2. **Modify the example** - Change names, ages, grades in `example_usage.py`
3. **Add features** - Try adding a new method to the Student class
4. **Create your own** - Build a similar system (Library, Inventory, etc.)

---

## ❓ Need Help?

- **Error: "No module named 'student_manager'"**
  - Make sure you're in the `mini_project` folder
  - Run: `cd /Users/alisadiq/how-to-become-a-backend-developer/00_orientation/mini_project`

- **Error: "python3: command not found"**
  - Try: `python example_usage.py` (without the 3)

- **Want to start fresh?**
  - Delete `students.json` and run the example again

---

**Happy Coding! 🎓**
