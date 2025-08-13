name = "GalibKhan"
name1 = 'Galibkhan'
name2 = """GalibKhan"""


print(name)  # Output: Galib
print(name[0])  # Output: G
print(name[0:3])  # Output: Gal
print(name[1:4])  # Output: ali
print(name[2:5])  # Output: lib
print(name[0:5])  # Output: Galib
print(name[0:])   # Output: Galib
print(name[:3])   # Output: Gal
print(name[1:])   # Output: alib
print(name[:])    # Output: Galib

print(name[-1])   # Output: b
print(name[-2])   # Output: i
print(name[-3])   # Output: l
print(name[-4])   # Output: a
print(name[-5])   # Output: G

print(name[-5:])  # Output: Galib
print(name[-5:-1])  # Output: Galib
print(name[-5:-2])  # Output: Galib
print(name[-5:-3])  # Output: Galib
print(name[-5:-4])  # Output: Galib
print(name[-5:-5])  # Output: (empty string)
print(name[-5:-6])  # Output: (empty string)

print(name[0:5:1])  # Output: Galib
print(name[0:5:2])  # Output: Glb
print(name[0:5:3])  # Output: Gb
print(name[0:5:4])  # Output: G
print(name[0:5:5])  # Output: G
print(name[0:5:6])  # Output: G
print(name[0:5:-1])  # Output: (empty string)



