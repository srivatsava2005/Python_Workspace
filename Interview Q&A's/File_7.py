

# ----------------------------------------
# 1️⃣ Recursive Data Processing
# ----------------------------------------

# We write a recursive function that adds up all numbers inside nested lists/dicts.

def sum_nested(data):
    """Recursively add all numbers inside nested data structures."""
    total = 0

    if isinstance(data, dict):
        # If data is a dictionary, loop through its values
        for value in data.values():
            total += sum_nested(value)
    elif isinstance(data, list):
        # If data is a list, loop through each element
        for value in data:
            total += sum_nested(value)
    elif isinstance(data, (int, float)):
        # If it's a number, return it directly
        total = data
    # If it’s something else (like string), ignore it
    return total

example_data = {"a": 10, "b": [1, 2, {"c": 3, "d": [4, 5]}]}
print("1️⃣ Recursive Sum:", sum_nested(example_data))
print("-" * 50)


# ----------------------------------------
# 2️⃣ Regex-based Data Extraction
# ----------------------------------------

import re

def extract_data(text):
    """Extract emails, phone numbers, and dates using regex."""
    emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)
    phones = re.findall(r"\+?\d[\d\s\-().]{7,}\d", text)
    dates = re.findall(r"\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b", text)
    return emails, phones, dates

sample_text = """
Email: test@example.com, info@school.org
Call: +91-9876543210 or (022) 1234 5678
Dates: 12/10/2025, 2025-10-16
"""
emails, phones, dates = extract_data(sample_text)
print("2️⃣ Extracted Emails:", emails)
print("Extracted Phones:", phones)
print("Extracted Dates:", dates)
print("-" * 50)


# ----------------------------------------
# 3️⃣ Custom Iterator for Fibonacci Sequence
# ----------------------------------------

class Fibonacci:
    """An iterator that generates Fibonacci numbers up to a limit."""

    def __init__(self, n):
        self.n = n  # Number of terms
        self.a, self.b = 0, 1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.n:
            raise StopIteration
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        self.count += 1
        return result

print("3️⃣ Fibonacci Sequence:")
for num in Fibonacci(8):
    print(num, end=" ")
print("\n" + "-" * 50)


# ----------------------------------------
# 4️⃣ Advanced Exception Handling
# ----------------------------------------

def read_file(filename):
    """Read a file and handle different types of exceptions."""
    try:
        with open(filename, "r") as f:
            data = f.read()
        print("File content:", data)
    except FileNotFoundError:
        print("❌ File not found!")
    except PermissionError:
        print("❌ You don’t have permission to read this file.")
    except Exception as e:
        print("❌ Some other error occurred:", e)

# Example: trying to open a missing file
read_file("non_existing_file.txt")
print("-" * 50)


# ----------------------------------------
# 5️⃣ Assertions and Debugging
# ----------------------------------------

def validate_age(age):
    """Validate that age is a positive number."""
    try:
        assert age > 0, "Age must be positive!"
        print("✅ Age is valid.")
    except AssertionError as e:
        with open("assertion_log.txt", "a") as log:
            log.write(str(e) + "\n")
        print("❌", e)

validate_age(25)
validate_age(-5)
print("-" * 50)


# ----------------------------------------
# 6️⃣ Module and Package Management (Simulated)
# ----------------------------------------
# We’ll simulate a mini math package using functions

def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    if b == 0:
        print("❌ Cannot divide by zero")
        return None
    return a / b

print("6️⃣ Math Package Example:")
print("Add:", add(2, 3))
print("Subtract:", subtract(5, 2))
print("Multiply:", multiply(3, 4))
print("Divide:", divide(10, 2))
print("-" * 50)


# ----------------------------------------
# 7️⃣ Class Design with Multiple Constructors
# ----------------------------------------

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, info):
        """Create a Person from a string like 'Name,Age'."""
        name, age = info.split(",")
        return cls(name.strip(), int(age.strip()))

    @classmethod
    def from_dict(cls, data):
        """Create a Person from a dictionary."""
        return cls(data["name"], data["age"])

p1 = Person("Alice", 25)
p2 = Person.from_string("Bob, 30")
p3 = Person.from_dict({"name": "Charlie", "age": 35})
print("7️⃣ Persons:", p1.__dict__, p2.__dict__, p3.__dict__)
print("-" * 50)


# ----------------------------------------
# 8️⃣ Inheritance and MRO
# ----------------------------------------

class A:
    def greet(self):
        return "Hello from A"

class B(A):
    def greet(self):
        return "Hello from B → " + super().greet()

class C(A):
    def greet(self):
        return "Hello from C → " + super().greet()

class D(B, C):
    def greet(self):
        return "Hello from D → " + super().greet()

d = D()
print("8️⃣ MRO Example:", d.greet())
print("MRO Order:", [cls.__name__ for cls in D.mro()])
print("-" * 50)


# ----------------------------------------
# 9️⃣ Polymorphism with Abstract Base Classes
# ----------------------------------------

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self): pass

    @abstractmethod
    def perimeter(self): pass

class Circle(Shape):
    def __init__(self, r): self.r = r
    def area(self): return math.pi * self.r ** 2
    def perimeter(self): return 2 * math.pi * self.r

class Rectangle(Shape):
    def __init__(self, w, h): self.w, self.h = w, h
    def area(self): return self.w * self.h
    def perimeter(self): return 2 * (self.w + self.h)

shapes = [Circle(5), Rectangle(4, 6)]
print("9️⃣ Polymorphism:")
for s in shapes:
    print(f"{type(s).__name__} → Area: {s.area():.2f}, Perimeter: {s.perimeter():.2f}")
print("-" * 50)


# ----------------------------------------
# 🔟 Encapsulation and Property Decorators
# ----------------------------------------

class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance  # private attribute

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            print("❌ Balance cannot be negative")
        else:
            self._balance = amount

acct = BankAccount(100)
acct.balance += 50
acct.balance = -10  # invalid
print("🔟 Account Balance:", acct.balance)
print("-" * 50)


# ----------------------------------------
# 11️⃣ Custom Exception Class
# ----------------------------------------

class InsufficientFunds(Exception):
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFunds("Not enough funds!")
    return balance - amount

try:
    print("11️⃣ New Balance:", withdraw(100, 150))
except InsufficientFunds as e:
    print("❌", e)
print("-" * 50)


# ----------------------------------------
# 12️⃣ Inner Classes and Composition
# ----------------------------------------

class Car:
    class Engine:
        def __init__(self, power):
            self.power = power

        def start(self):
            return f"Engine with {self.power} HP started."

    def __init__(self, brand, power):
        self.brand = brand
        self.engine = Car.Engine(power)

    def start(self):
        return f"{self.brand} car: {self.engine.start()}"

car = Car("Tesla", 500)
print("12️⃣ Inner Class:", car.start())
print("-" * 50)


# ----------------------------------------
# 13️⃣ Garbage Collection and Destructors
# ----------------------------------------

class Demo:
    def __init__(self, name):
        self.name = name
        print(f"Object {self.name} created")

    def __del__(self):
        print(f"Object {self.name} destroyed")

d1 = Demo("Temp")
del d1  # force delete
print("-" * 50)


# ----------------------------------------
# 14️⃣ Function Aliasing and Higher-Order Functions
# ----------------------------------------

def greet(name):
    return f"Hello, {name}!"

# Assign function to a variable
say_hi = greet
print("14️⃣ Function Aliasing:", say_hi("Alice"))

# Higher order function
def shout(func):
    def wrapper(name):
        return func(name).upper()
    return wrapper

loud_greet = shout(greet)
print("Loud Greeting:", loud_greet("Bob"))
print("-" * 50)


# ----------------------------------------
# 15️⃣ Interface Simulation using ABC
# ----------------------------------------

class Serializer(ABC):
    @abstractmethod
    def serialize(self, obj): pass

class JSONSerializer(Serializer):
    def serialize(self, obj):
        import json
        return json.dumps(obj)

s = JSONSerializer()
print("15️⃣ Interface Simulation:", s.serialize({"name": "Alice", "age": 25}))
print("-" * 50)


print("✅ All sections executed successfully!")
