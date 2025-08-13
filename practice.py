#WAP tp input side of a square & print its Area & Perimeter

side= input("Enter the side of the square: ")
side = float(side)  # Convert input to float for calculations

area = side ** 2
perimeter = 4 * side

print("Area of the square:", area)  # Output: Area of the square: <calculated value>
print("Perimeter of the square:", perimeter)  # Output: Perimeter of the square

a = float(input("Enter a number: "))
b = float(input("Enter another number: "))

average = (a + b) / 2
print("a is greater than or equal to b:", a >= b)  # Output: True or False
print("a is less than or equal to b:", a <= b)  # Output:
print("Average of the two numbers:", average)  # Output: Average of the two numbers: <calculated value>
print("Type of average:", type(average))  # Output: <class 'float'>

