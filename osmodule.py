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