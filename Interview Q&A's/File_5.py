# ==========================================================
# 1. Custom Data Type Conversion
# Count occurrences of each data type in a mixed list
# ==========================================================
def count_types(lst):
    type_count = {"int": 0, "float": 0, "str": 0, "bool": 0}
    for item in lst:
        if isinstance(item, int) and not isinstance(item, bool):
            type_count["int"] += 1
        elif isinstance(item, float):
            type_count["float"] += 1
        elif isinstance(item, str):
            type_count["str"] += 1
        elif isinstance(item, bool):
            type_count["bool"] += 1
    return type_count

# Example
print(count_types([1, 2.5, "hi", True, False, 3]))


# ==========================================================
# 2. Dynamic Input Parser
# Parse input into correct Python data type
# ==========================================================
def parse_value(value):
    if value.lower() in ["true", "false"]:
        return value.lower() == "true"
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError:
            return value

def parse_line(line):
    return [parse_value(x.strip()) for x in line.split(",")]

# Example
print(parse_line("10, 3.14, True, hello"))


# ==========================================================
# 3. String Manipulation Suite
# Remove vowels, count char frequency, substrings of k
# ==========================================================
def remove_vowels(s):
    return ''.join(c for c in s if c.lower() not in "aeiou")

def char_frequency(s):
    return {c: s.count(c) for c in set(s)}

def substrings_of_k(s, k):
    return [s[i:i+k] for i in range(len(s)-k+1)]

# Example
print(remove_vowels("hello world"))
print(char_frequency("banana"))
print(substrings_of_k("python", 3))


# ==========================================================
# 4. Custom Array Operations
# Int-only list class with basic methods
# ==========================================================
class IntList:
    def __init__(self):
        self.data = []

    def append(self, val):
        if isinstance(val, int):
            self.data.append(val)

    def remove(self, val):
        self.data.remove(val)

    def pop(self, idx=-1):
        return self.data.pop(idx)

    def slice(self, start, end):
        return self.data[start:end]

# Example
L = IntList()
L.append(5); L.append(10)
print(L.slice(0,2))


# ==========================================================
# 5. Type Conversion Utility
# Convert dict string values into proper types
# ==========================================================
def convert_dict(d):
    def convert(v):
        if v.lower() in ["true", "false"]:
            return v.lower() == "true"
        try:
            return int(v)
        except:
            try:
                return float(v)
            except:
                return v
    return {k: convert(v) for k, v in d.items()}

# Example
print(convert_dict({"a": "10", "b": "3.14", "c": "True", "d": "hello"}))


# ==========================================================
# 6. Prime Number Generator
# Yield primes up to n
# ==========================================================
def prime_gen(n):
    for num in range(2, n+1):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            yield num

# Example
print(list(prime_gen(20)))


# ==========================================================
# 7. Custom List Class with Undo/Redo
# List with undo/redo functionality
# ==========================================================
class AdvancedList:
    def __init__(self):
        self.data = []
        self.history = []
        self.redo_stack = []

    def _record(self, action):
        self.history.append((action, self.data[:]))
        self.redo_stack.clear()

    def append(self, val):
        self._record("append")
        self.data.append(val)

    def remove(self, val):
        self._record("remove")
        self.data.remove(val)

    def pop(self, idx=-1):
        self._record("pop")
        return self.data.pop(idx)

    def reverse(self):
        self._record("reverse")
        self.data.reverse()

    def sort(self):
        self._record("sort")
        self.data.sort()

    def undo(self):
        if self.history:
            action, prev = self.history.pop()
            self.redo_stack.append((action, self.data[:]))
            self.data = prev

    def redo(self):
        if self.redo_stack:
            action, nxt = self.redo_stack.pop()
            self.history.append((action, self.data[:]))
            self.data = nxt

# Example
AL = AdvancedList()
AL.append(5); AL.append(2); AL.sort()
print(AL.data)
AL.undo(); print(AL.data)


# ==========================================================
# 8. Set Operations
# Union, intersection, difference
# ==========================================================
def set_ops(a, b):
    A, B = set(a), set(b)
    return {"union": A|B, "intersection": A&B, "difference": A-B}

# Example
print(set_ops([1,2,3], [3,4,5]))


# ==========================================================
# 9. Type Casting Engine
# Cast all list values to target type
# ==========================================================
def cast_list(lst, target_type):
    result = []
    for val in lst:
        try:
            result.append(target_type(val))
        except:
            result.append(None)
    return result

# Example
print(cast_list(["1","2.5","a"], float))


# ==========================================================
# 10. List Comprehension Challenge
# Evens, square odds, tuples divisible by 3
# ==========================================================
nums = [1,2,3,4,5,6,7,8,9]
evens = [n for n in nums if n%2==0]
squared_odds = [n**2 for n in nums if n%2!=0]
div3_tuples = [(n,n**2) for n in nums if n%3==0]

# Example
print(evens, squared_odds, div3_tuples)


# ==========================================================
# 11. Set Membership & Manipulation
# Unique chars, remove vowels
# ==========================================================
def unique_chars_no_vowels(s):
    return {c for c in set(s) if c.lower() not in "aeiou"}

# Example
print(unique_chars_no_vowels("programming"))


# ==========================================================
# 12. Function Decorator for Logging
# Log args and return
# ==========================================================
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Returned {result}")
        return result
    return wrapper

@logger
def add(a,b): 
    return a+b

# Example
add(5,3)


# ==========================================================
# 13. Deep Copy vs Shallow Copy
# Demo nested list copy
# ==========================================================
import copy

lst = [[1,2],[3,4]]
shallow = copy.copy(lst)
deep = copy.deepcopy(lst)

lst[0][0] = 99
print("Original:", lst)
print("Shallow:", shallow)
print("Deep:", deep)


# ==========================================================
# 14. Custom Implementation of max, min, sum
# Own versions
# ==========================================================
def my_max(lst):
    m = lst[0]
    for x in lst:
        if x > m: m = x
    return m

def my_min(lst):
    m = lst[0]
    for x in lst:
        if x < m: m = x
    return m

def my_sum(lst):
    total = 0
    for x in lst:
        total += x
    return total

# Example
print(my_max([1,5,3]), my_min([1,5,3]), my_sum([1,5,3]))


# ==========================================================
# 15. Advanced Control Flow
# Skip multiples of 3, break on negative
# ==========================================================
def custom_filter(lst):
    result = []
    for num in lst:
        if num < 0:
            break
        if num % 3 == 0:
            continue
        result.append(num)
    return result

# Example
print(custom_filter([1,2,3,4,6,7,-1,10]))
