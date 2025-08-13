print("hellow world")

name =input("Enter your name: ")
age= input("Enter your age: ")
city = input("Enter your city: ")
marks = input("Enter your marks: ") 
country = input("Enter your country: ")
hobby = input("Enter your hobby: ")

print("welcome:", name)
print("age:",age)
print("marks:", marks)
print("city:",city)
print("country:", country)
print("hobby:", hobby)

print(type(name))  # Output: <class 'str'>
print(type(age))  # Output: <class 'str'>
print(type(city))  # Output: <class 'str'>
print(type(marks))  # Output: <class 'str'> 
print(type(country))  # Output: <class 'str'>
print(type(hobby))  # Output: <class 'str'> 

#iput() satement is always string
#typecasting is required to convert string to int or float

print(type(int(age)))  # Output: <class 'int'>
print(type(float(marks)))  # Output: <class 'float'>Galib
