# Python Basics + OOP Quiz

## Instructions
- Answer all 10 questions
- For MCQ: Choose the correct option (A, B, C, or D)
- For code output questions: Write what the code will print

---

## Section 1: Multiple Choice Questions (MCQ)

### Question 1
What is the correct way to create a list in Python?

A) `list = (1, 2, 3)`  
B) `list = [1, 2, 3]`  
C) `list = {1, 2, 3}`  
D) `list = <1, 2, 3>`

**Your Answer:** ___

---

### Question 2
Which of the following is a valid way to define a class in Python?

A) `class MyClass():`  
B) `def MyClass:`  
C) `class MyClass:`  
D) `create class MyClass:`

**Your Answer:** ___

---

### Question 3
What does `self` represent in a class method?

A) The class itself  
B) The current instance of the class  
C) A global variable  
D) A static method

**Your Answer:** ___

---

### Question 4
Which data structure does NOT allow duplicate values?

A) List  
B) Tuple  
C) Set  
D) Dictionary

**Your Answer:** ___

---

### Question 5
What is the purpose of `__init__` method in a class?

A) To delete an object  
B) To initialize object attributes  
C) To print object information  
D) To create a copy of the object

**Your Answer:** ___

---

## Section 2: Code Output Questions

### Question 6
What will be the output of this code?

```python
x = [1, 2, 3]
x.append(4)
print(x)
```

**Your Answer:** ___

---

### Question 7
What will be the output of this code?

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Ali", 20)
print(p.name)
```

**Your Answer:** ___

---

### Question 8
What will be the output of this code?

```python
numbers = [1, 2, 3, 4, 5]
result = [n * 2 for n in numbers if n > 2]
print(result)
```

**Your Answer:** ___

---

### Question 9
What will be the output of this code?

```python
student = {"name": "Sara", "age": 19}
print(student.get("grade", "Not Found"))
```

**Your Answer:** ___

---

### Question 10
What will be the output of this code?

```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return self.balance

account = BankAccount(100)
account.deposit(50)
print(account.balance)
```

**Your Answer:** ___

---

## Answer Key

<details>
<summary>Click to reveal answers</summary>

1. **B** - `list = [1, 2, 3]`
2. **C** - `class MyClass:`
3. **B** - The current instance of the class
4. **C** - Set
5. **B** - To initialize object attributes
6. `[1, 2, 3, 4]`
7. `Ali`
8. `[6, 8, 10]`
9. `Not Found`
10. `150`

</details>

---

## Scoring Guide

- 9-10 correct: Excellent! You have a strong understanding.
- 7-8 correct: Good! Review the topics you missed.
- 5-6 correct: Fair. Go back and review the orientation notebooks.
- Below 5: Need more practice. Revisit the fundamentals.
