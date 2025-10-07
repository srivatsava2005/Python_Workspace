# ==========================================================
# 1. Data Structure Design
# Class that supports stack & queue operations
# ==========================================================
class StackQueue:
    def __init__(self):
        self.data = []

    # Stack operations
    def push(self, val):
        self.data.append(val)

    def pop(self):
        if not self.data: return None
        return self.data.pop()

    # Queue operations
    def enqueue(self, val):
        self.data.append(val)

    def dequeue(self):
        if not self.data: return None
        return self.data.pop(0)

    def peek(self):
        return self.data[-1] if self.data else None

# Example
sq = StackQueue()
sq.push(10); sq.enqueue(20)
print(sq.pop(), sq.dequeue())


# ==========================================================
# 2. Custom String Formatter
# Replace placeholders with dict values
# ==========================================================
def custom_format(template, values):
    result = template
    for key, val in values.items():
        result = result.replace("{" + key + "}", str(val))
    # Handle missing keys
    import re
    result = re.sub(r"\{.*?\}", "?", result)
    return result

# Example
print(custom_format("Hello {name}, you have {count} messages.", {"name": "Alice"}))


# ==========================================================
# 3. Multi-type Sorting
# Numbers first, then strings
# ==========================================================
def multi_sort(lst):
    nums = sorted([x for x in lst if isinstance(x, (int, float))])
    strs = sorted([x for x in lst if isinstance(x, str)])
    return nums + strs

# Example
print(multi_sort([3, "banana", 1.5, "apple", 2]))


# ==========================================================
# 4. Recursive List Flattening
# Flatten nested list
# ==========================================================
def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

# Example
print(flatten([1,[2,[3,4],5],6]))


# ==========================================================
# 5. Dynamic Function Dispatcher
# Dispatch string command to correct function
# ==========================================================
def add(a,b): return a+b
def subtract(a,b): return a-b
def multiply(a,b): return a*b
def divide(a,b): return a/b if b!=0 else None

dispatcher = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide
}

def dispatch(cmd, *args):
    func = dispatcher.get(cmd)
    if func: return func(*args)
    return None

# Example
print(dispatch("multiply", 5, 3))


# ==========================================================
# 6. Custom Exception Handling
# Raise exceptions for invalid values
# ==========================================================
class InvalidTypeError(Exception): pass
class NegativeNumberError(Exception): pass
class DivisionByZeroError(Exception): pass

def process_values(lst):
    for val in lst:
        try:
            if not isinstance(val, (int, float)):
                raise InvalidTypeError(f"Invalid type: {type(val)}")
            if val < 0:
                raise NegativeNumberError(f"Negative number: {val}")
            if val == 0:
                raise DivisionByZeroError("Division by zero risk")
            print(f"Processed: {100/val}")
        except Exception as e:
            print("Error:", e)

# Example
process_values([10, -2, "abc", 0, 5])


# ==========================================================
# 7. Advanced List Comprehensions
# Matrix diagonal, transpose, filter rows with negatives
# ==========================================================
matrix = [
    [1,2,3],
    [4,-5,6],
    [7,8,9]
]

diagonal = [matrix[i][i] for i in range(len(matrix))]
transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
no_neg_rows = [row for row in matrix if all(x >= 0 for x in row)]

# Example
print("Diagonal:", diagonal)
print("Transpose:", transpose)
print("No negative rows:", no_neg_rows)


# ==========================================================
# 8. Set and Dictionary Interactions
# Keep only dict items with keys in set
# ==========================================================
def filter_dict(d, s):
    return {k:v for k,v in d.items() if k in s}

# Example
print(filter_dict({"a":1,"b":2,"c":3}, {"a","c"}))


# ==========================================================
# 9. Memoized Recursive Fibonacci
# Optimized vs Naive
# ==========================================================
from functools import lru_cache
import time

@lru_cache(None)
def fib_memo(n):
    if n<=1: return n
    return fib_memo(n-1) + fib_memo(n-2)

def fib_naive(n):
    if n<=1: return n
    return fib_naive(n-1) + fib_naive(n-2)

# Example speed comparison
start = time.time(); fib_naive(20); print("Naive time:", time.time()-start)
start = time.time(); fib_memo(20); print("Memoized time:", time.time()-start)


# ==========================================================
# 10. Custom Iterable Class
# Iterate in reverse order
# ==========================================================
class ReverseIterable:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

# Example
for x in ReverseIterable([1,2,3,4]):
    print(x, end=" ")
print()


# ==========================================================
# 11. List Partitioning
# Split list into n nearly equal parts
# ==========================================================
def partition(lst, n):
    k, m = divmod(len(lst), n)
    return [lst[i*k + min(i,m):(i+1)*k + min(i+1,m)] for i in range(n)]

# Example
print(partition([1,2,3,4,5,6,7], 3))


# ==========================================================
# 12. Type-safe Function Decorator
# Checks arg types
# ==========================================================
def type_check(*types):
    def decorator(func):
        def wrapper(*args):
            for a,t in zip(args, types):
                if not isinstance(a, t):
                    raise TypeError(f"Expected {t}, got {type(a)}")
            return func(*args)
        return wrapper
    return decorator

@type_check(int, int)
def add_nums(a,b): return a+b

# Example
print(add_nums(3,4))
# print(add_nums(3,"x"))   # would raise error


# ==========================================================
# 13. Deep Copy with Custom Objects
# Demonstrate independence after copy
# ==========================================================
import copy

class Person:
    def __init__(self,name): self.name=name
    def __repr__(self): return f"Person({self.name})"

p1 = Person("Alice"); p2 = Person("Bob")
people = [p1,p2]
deep_people = copy.deepcopy(people)

deep_people[0].name = "Eve"
print("Original:", people)
print("Deep Copy:", deep_people)


# ==========================================================
# 14. Dynamic Attribute Access
# Add/delete/access attributes dynamically
# ==========================================================
class DynamicObject:
    def __init__(self):
        self.__dict__['data'] = {}

    def __getattr__(self, name):
        return self.data.get(name, None)

    def __setattr__(self, name, value):
        self.data[name] = value

    def __delattr__(self, name):
        if name in self.data: del self.data[name]

# Example
obj = DynamicObject()
obj.age = 25
print(obj.age)
del obj.age
print(obj.age)


# ==========================================================
# 15. Functional Programming Challenge
# map, filter, reduce
# ==========================================================
from functools import reduce

nums = [1,2,3,4,5,6,7,8,9,10]

processed = list(map(lambda x: x*2, filter(lambda x: x%2==0, nums)))
filtered = list(filter(lambda x: x>=10, processed))
product = reduce(lambda a,b: a*b, filtered, 1)

print("Processed:", processed)
print("Filtered:", filtered)
print("Product:", product)
