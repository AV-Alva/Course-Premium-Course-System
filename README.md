# 🎓 Course & Premium Course System

A simple **Online Learning Platform** built using Python Object-Oriented Programming (OOP).

This project demonstrates how a real-world EdTech platform can model **regular courses and premium courses** using inheritance while also incorporating **packages, modules, exception handling, custom exceptions, and logging**.

---

## 📌 Project Overview

An online learning platform may offer different types of courses.

A regular course contains basic information such as:

- Course name
- Instructor
- Duration
- Price

A premium course contains all the features of a regular course along with additional benefits such as:

- Mentor support
- Live sessions

Instead of creating the same attributes and methods again, this project uses **inheritance** so that `PremiumCourse` can reuse the functionality available in `Course`.

---

## 🎯 Objectives

The main objectives of this project are to understand:

- Classes and Objects
- Constructors
- Instance Attributes
- Instance Methods
- Class Variables
- Class Methods
- Inheritance
- Method Overriding
- `super()`
- Packages and Modules
- Exception Handling
- Custom Exceptions
- Logging

---

## 🏗️ Class Structure

```text
                Course
                   │
                   │ inherits
                   ▼
             PremiumCourse
```

### Course

The `Course` class contains:

```text
course_name
instructor
duration
price
```

Methods:

```text
show_course_details()
calculate_discount()
get_course_count()
```

### PremiumCourse

`PremiumCourse` inherits from `Course`.

It contains all the properties of `Course` and adds:

```text
mentor_support
live_sessions
```

It also overrides:

```text
show_course_details()
```

to display premium-course-specific information.

---

## 📁 Project Structure

```text
course_platform/
│
├── main.py
├── README.md
│
├── courses/
│   ├── __init__.py
│   ├── course.py
│   └── premium_course.py
│
├── exceptions/
│   ├── __init__.py
│   └── custom_exceptions.py
│
├── utils/
│   ├── __init__.py
│   └── logger_config.py
│
└── logs/
    └── course_platform.log
```

---

## 📦 Packages and Modules

The project is divided into multiple packages and modules to keep the code organized.

### `courses`

Contains the classes related to courses.

```text
course.py
premium_course.py
```

### `exceptions`

Contains custom exceptions used by the application.

```text
custom_exceptions.py
```

### `utils`

Contains reusable utility functionality.

```text
logger_config.py
```

### `logs`

Stores application log files.

```text
course_platform.log
```

---

## 🧩 OOP Concepts Used

### 1. Class

A class acts as a blueprint for creating objects.

```python
class Course:
    pass
```

---

### 2. Objects

Objects represent actual courses available on the platform.

```python
python_course = Course(
    "Python Fundamentals",
    "Amrutha Varshini Alva",
    20,
    3000
)
```

---

### 3. Constructor

The `__init__()` method initializes an object when it is created.

```python
def __init__(self, course_name, instructor, duration, price):
    self.course_name = course_name
    self.instructor = instructor
    self.duration = duration
    self.price = price
```

---

### 4. Inheritance

`PremiumCourse` inherits from `Course`.

```python
class PremiumCourse(Course):
```

This means `PremiumCourse` can reuse attributes and methods defined inside `Course`.

---

### 5. `super()`

The `super()` function allows the child class to call functionality from its parent class.

```python
super().__init__(
    course_name,
    instructor,
    duration,
    price
)
```

This avoids rewriting the parent constructor inside `PremiumCourse`.

---

### 6. Method Overriding

Both `Course` and `PremiumCourse` contain:

```python
show_course_details()
```

The premium version extends the parent functionality to display:

```text
Mentor Support
Live Sessions
```

---

### 7. Class Variable

The application keeps track of the total number of courses created.

```python
course_count = 0
```

Whenever a course is successfully created:

```python
Course.course_count += 1
```

---

### 8. Class Method

The total number of courses can be retrieved using:

```python
@classmethod
def get_course_count(cls):
    return cls.course_count
```

Example:

```python
Course.get_course_count()
```

---

## 💰 Discount Calculation

The project allows discounts to be applied to courses.

Example:

```python
discounted_price = ai_course.calculate_discount(20)
```

If the original course price is:

```text
₹10,000
```

and the discount is:

```text
20%
```

the final price becomes:

```text
₹8,000
```

---

## ⚠️ Exception Handling

The project uses exception handling to prevent the application from crashing when invalid data is provided.

The application handles situations such as:

- Negative course price
- Zero course price
- Invalid course duration
- Invalid discount percentage
- Unexpected application errors

Example:

```python
try:
    course = Course(
        "Python",
        "Instructor",
        20,
        -5000
    )

except InvalidPriceError as error:
    print("Price Error:", error)
```

---

## 🚨 Custom Exceptions

Custom exceptions make errors easier to understand.

The project contains:

```python
InvalidPriceError
InvalidDurationError
InvalidDiscountError
```

For example:

```python
class InvalidPriceError(Exception):
    pass
```

If the price is invalid:

```python
raise InvalidPriceError(
    "Course price must be greater than zero."
)
```

---

## 📝 Logging

The application records important activities inside:

```text
logs/course_platform.log
```

Examples of logged activities include:

```text
Course created
Premium course created
Discount calculated
Invalid price entered
Invalid duration entered
Invalid discount entered
Unexpected application error
```

Logging levels used include:

```python
logger.info()
logger.warning()
logger.error()
logger.exception()
```

Example log output:

```text
2026-10-02 10:15:10 - INFO - Course created: Python Fundamentals
2026-10-02 10:15:11 - INFO - Premium course created: Generative AI Masterclass
2026-10-02 10:15:12 - INFO - 20% discount applied to Generative AI Masterclass
```

---

## ▶️ How to Run the Project

### Step 1 — Open the project

Open the `course_platform` folder in VS Code.

### Step 2 — Open the terminal

Make sure the terminal is pointing to the project root:

```text
course_platform/
```

### Step 3 — Run the program

```bash
python main.py
```

---

## 🖥️ Sample Output

```text
===== ONLINE LEARNING PLATFORM =====

--- Course Details ---
Course Name: Python Fundamentals
Instructor: Amrutha Varshini Alva
Duration: 20 hours
Price: ₹ 3000

--- Course Details ---
Course Name: Generative AI Masterclass
Instructor: Ananya
Duration: 30 hours
Price: ₹ 10000
Course Type: Premium
Mentor Support: Yes
Live Sessions: 10

--- Discount Example ---

Price after 20% discount: ₹ 8000.0

Total courses created: 4
```

---

## 🧪 Testing Exception Handling

### Invalid Price

Try creating:

```python
invalid_course = Course(
    "Machine Learning",
    "Kiran",
    20,
    -5000
)
```

Expected result:

```text
Price Error: Course price must be greater than zero.
```

---

### Invalid Discount

Try:

```python
python_course.calculate_discount(120)
```

Expected result:

```text
Discount Error: Discount must be between 0 and 100.
```

The error will also be recorded in the log file.

---

## 🔄 Program Flow

```text
START
  │
  ▼
main.py
  │
  ├── Create Course objects
  │
  ▼
Course.__init__()
  │
  ├── Validate price
  ├── Validate duration
  ├── Store course details
  ├── Increase course_count
  └── Write log
  │
  ▼
Create PremiumCourse
  │
  ▼
PremiumCourse.__init__()
  │
  ▼
super().__init__()
  │
  ▼
Course.__init__()
  │
  ▼
Add mentor support + live sessions
  │
  ▼
Display Course Details
  │
  ▼
Calculate Discount
  │
  ▼
Display Total Course Count
  │
  ▼
END
```

If an error occurs:

```text
Invalid Input
     │
     ▼
Custom Exception
     │
     ├── Display Error
     │
     └── Write Error to Log
```

---

## 🌍 Real-World Application

This structure is similar to how an EdTech platform could organize different course offerings.

For example:

```text
Course
│
├── Python Fundamentals
├── SQL Fundamentals
└── Git Basics
```

Premium offerings can extend the normal course:

```text
Course
   │
   └── PremiumCourse
          │
          ├── Mentor Support
          └── Live Sessions
```

Instead of duplicating common properties such as course name, instructor, duration, and price, inheritance allows the premium course to **reuse and extend** the existing `Course` functionality.

---

## 📚 Concepts Demonstrated

| Concept | Implementation |
|---|---|
| Class | `Course`, `PremiumCourse` |
| Object | `python_course`, `ai_course` |
| Constructor | `__init__()` |
| Instance Attributes | `self.course_name`, `self.price` |
| Instance Method | `show_course_details()` |
| Class Variable | `course_count` |
| Class Method | `get_course_count()` |
| Inheritance | `PremiumCourse(Course)` |
| Parent Constructor | `super().__init__()` |
| Method Overriding | `show_course_details()` |
| Packages | `courses`, `exceptions`, `utils` |
| Modules | `course.py`, `premium_course.py` |
| Exception Handling | `try` and `except` |
| Custom Exceptions | `InvalidPriceError`, etc. |
| Logging | Python `logging` module |

---

## 🚀 Key Learning

The most important concept demonstrated by this project is **inheritance**.

Instead of duplicating code:

```text
Course
   ↓
Common course functionality
```

can be reused by:

```text
PremiumCourse
```

and the child class only needs to add the features that make it different.

This makes the application:

- Easier to maintain
- More reusable
- Better organized
- Easier to extend
- Closer to real-world software design

---

## 👩‍💻 Author

**AMRUTHA VARSHINI ALVA**

Keep learning. Keep building. Keep evolving.
