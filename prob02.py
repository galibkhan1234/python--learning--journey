import os

# Specify the directory path ('.' means current directory)
directory_path = '/New folder'


    # List all files and folders in the directory
contents = os.listdir(directory_path)

for item in contents:
     print(item)

