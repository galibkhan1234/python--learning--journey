fruit = ["apple", "banana", "cherry", "date", "elderberry"]

# Example of modifying a list in Python
fruit [0]= "apricot"  # Changing the first element
print("Original list:", fruit)
print(fruit[0])  # Accessing the first element

fruit.append("fig")  # Adding a new element
print("List after appending:", fruit)

fruit.remove("date")  # Removing an element
print("Updated list:", fruit)

print(fruit.pop(2))  # Removing and returning the second element

fruit.insert(3, "kiwi")  # Inserting a new element at index 3
print("List after insertion:", fruit)

fruit.sort()  # Sorting the list
print("Sorted list:", fruit)

fruit.remove("elerberry")  # Removing an element
print("List after removing 'elerberry':", fruit)

fruit.reverse()  # Reversing the list
print("Reversed list:", fruit)      
