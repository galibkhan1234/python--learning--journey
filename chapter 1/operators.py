# Arithmetic operators in Python
a = 10
b = 3

# Addition
print(a + b)  # Output: 13

# Subtraction
print(a - b)  # Output: 7

# Multiplication
print(a * b)  # Output: 30

# Division
print(a / b)  # Output: 3.3333333333333335

# Modulus
print(a % b)  # Output: 1

# Exponentiation
print(a ** b)  # Output: 1000

# Floor Division
print(a // b)  # Output: 3

# Comparison operators in Python
print(a == b)  # Output: False
print(a != b)  # Output: True
print(a > b)   # Output: True
print(a < b)   # Output: False
print(a >= b)  # Output: True
print(a <= b)  # Output: False

# Logical operators in Python
print(a > 5 and b < 5)  # Output: True
print(a > 5 or b > 5)   # Output: True
print(not (a > 5))       # Output: False

# Assignment operators in Python
x = 5
x += 2  # Equivalent to x = x + 2
print(x)  # Output: 7

# Bitwise operators in Python
print(a & b)  # Bitwise AND
print(a | b)  # Bitwise OR
print(a ^ b)  # Bitwise XOR

# Identity operators in Python
print(a is b)  # Output: False
print(a is not b)  # Output: True

# Membership operators in Python
my_list = [1, 2, 3, 4, 5]
print(3 in my_list)  # Output: True
print(6 not in my_list)  # Output: True

# Ternary operator in Python
result = "Yes" if a > b else "No"
print(result)  # Output: Yes


# Lambda function in Python
square = lambda x: x * x
print(square(5))  # Output: 25