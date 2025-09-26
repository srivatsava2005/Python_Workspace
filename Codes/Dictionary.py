# Creating a dictionary
student = {
    "name": "Rahul",
    "age": 21,
    "course": "Python"
}

# Accessing values
print(student["name"])      # Rahul
print(student.get("age"))   # 21

# Adding new key-value pair
student["grade"] = "A"

# Updating values
student["age"] = 22

# Removing key-value pair
del student["course"]

# Iterating over dictionary
for key, value in student.items():
    print(key, ":", value)

# Dictionary methods
print(student.keys())    # dict_keys(['name', 'age', 'grade'])
print(student.values())  # dict_values(['Rahul', 22, 'A'])
print(student.items())   # dict_items([('name', 'Rahul'), ('age', 22), ('grade', 'A')])
