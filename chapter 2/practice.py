#find even or odd, positive or negative, and largest of three numbers
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even")  
else:
    print("Odd")    
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero") 



print("Enter three numbers to find the largest:")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b and a > c:
    print("First number is the largest")
elif b > a and b > c:
    print("Second number is the largest")
else:
    print("Third number is the largest")
    