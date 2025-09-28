# Type Casting in Python

# Integer to Float
num_int = 10
num_float = float(num_int)
print("Integer to Float:", num_float)

# Float to Integer
num_f = 12.56
num_i = int(num_f)
print("Float to Integer:", num_i)

# Integer to String
num = 100
num_str = str(num)
print("Integer to String:", num_str, type(num_str))

# String to Integer
str_num = "250"
int_num = int(str_num)
print("String to Integer:", int_num, type(int_num))

# String to Float
str_f = "45.67"
float_num = float(str_f)
print("String to Float:", float_num, type(float_num))

# Integer to Boolean
n = 0
print("0 to Boolean:", bool(n))   # False
n = 5
print("5 to Boolean:", bool(n))   # True

# List to Set
my_list = [1, 2, 2, 3]
my_set = set(my_list)
print("List to Set:", my_set)

# Tuple to List
my_tuple = (10, 20, 30)
my_list2 = list(my_tuple)
print("Tuple to List:", my_list2)