"""num = "4"+"2"
val =int(num)+6
print(float(val))"""


num = int(input("enter a number:"))
res = ["even","odd"][num %2]
print(res)