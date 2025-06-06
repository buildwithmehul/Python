#program to list items in a directory using os module

import os

dic_path = "/"

contents = os.listdir(dic_path)

for item in contents:
    # Method 1 : # Using os.path.join to create the full path
    item_path = os.path.join(dic_path,item)
    if os.path.isfile(item_path):
        print(f"File: {item_path}")
    elif os.path.isdir(item_path):
        print(f"Directory: {item_path}")
    else :
        print(f"Other: {item_path}")

    # Method 2 : Simple Method
    # print(item)

    """ os is an external module which has a use that it can list items in a directory.
      Here our dictionary was the C drive.Using os.path.join we joined the dictionary path with the item name to get the full path of the item. 
      Then we checked if it was a file or directory using os.path.isfile and os.path.isdir respectively.
        If it was neither, we printed it as 'Other'. This is a simple way to list items in a directory using Python's os module."""