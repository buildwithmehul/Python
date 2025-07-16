#STRINGS IN PYTHON
# Strings are ordered, immutable, and allow duplicate elements. They are a collection of characters and immutable at the same time.
# Strings are defined using single quotes '' or double quotes "". They can be indexed and sliced like lists.
# The difference between strings and lists is that strings are immutable, meaning once created, their elements cannot be changed, added, or removed.    

name = "Aishwarya"

"""Index and Slicing"""

print(name[5])

print(name[-4])

name2 = name[0:6]  # Slicing from index 0 to 5(6 is not included that is upper limit is exclusive)
print(name2)

name3 = name[-4:-2]
print(name3)  # Slicing from index -4 to -3(-2 is not included that is upper limit is exclusive)

print(name[:4]) 
 # Slicing from index 0 to 3(4 is not included that is upper limit is exclusive. This is same as name[0:4] as no start index is given meaning it starts from 0)

print(name[2:])
# Slicing from index 2 to end of the string (no end index is given meaning it goes till the end)

print(name[1:7:2])
# Slicing from index 1 to 6(7 is not included that is upper limit is exclusive) with step of 2 (it will take every second character)

name[3] = "Aish"  # This will raise an error as strings are immutable in Python, meaning you cannot change a character at a specific index directly

"""Functions"""

#Length of string
print(len(name))  # Returns the length of the string

#Endswith 
print(name.endswith("warya"))  # Returns True if the string ends with the specified suffix, otherwise False
print(name.endswith("Aish"))  # Returns False
print(name.endswith("rya"))  # Returns True

#Startswith

print(name.startswith("Aish"))  # Returns True if the string starts with the specified prefix, otherwise False
print(name.startswith("war"))  # Returns False

#Capitalize

name5 = "mehul"
print(name5.capitalize())  # Returns the string with the first character capitalized and the rest lowercased

#title

name6 = "mehul aishwarya"
print(name6.title())  # Returns the string with the first character of each word capitalized

#Lower and Upper
name7 = "MeHuL"
print(name7.lower())  # Returns the string in lowercase
print(name7.upper())  # Returns the string in uppercase

#Find
print(name.find("Aish"))  # Returns the lowest index of the substring if found, otherwise -1
print(name.find("warya"))  # Returns the lowest index of the substring if found, otherwise -1
print(name.find("xyz"))  # Returns -1 as "xyz" is not found in the string
print(name6.find("a"))  # Returns the lowest index of the substring "a" in "mehul aishwarya"))

#Replace
print(name.replace("Aish", "Mehul"))  # Replaces the first occurrence of "Aish" with "Mehul"
print(name.replace("Aish", "Mehul", 1))  # Replaces the first occurrence of "Aish" with "Mehul" (the third argument is the count of replacements)
print(name6.replace("a","P"))  # Replaces all occurrences of "a" with "P" in "mehul aishwarya" 

#Escape Characters using \
string_with_escape = "Hello, I am Aishwarya.\nI am learning Python.\tIt is fun!" # \n for new line, \t for tab
print(string_with_escape)
# Multiline String using triple quotes
multiline_string = """Hello, I am Aishwarya.
I am learning Python.
It is fun!"""
print(multiline_string)
# String Concatenation
string1 = "Hello"
string2 = "World"
concatenated_string = string1 + " " + string2  # Concatenating two strings with a space in between
print(concatenated_string)  # Output: Hello World

# "" in a string
'''  string_with_quotes = "He said, "Hello World!"" ''' # cause error as " is used to define the string
# To include quotes in a string, we can use escape characters or use single quotes to define the string

string_with_quotes = "He said, \"Hello World!\""  #Using escape character \ to include double quotes in the string
print(string_with_quotes)  # Output: He said, "Hello World!"


# PRACTICE SET
#1
string = input("Enter your name:")
print("Good Afternoon!",string)
print(f"Good Afternoon! {string}")  # Using f-string for formatted string literals
print("Good Afternoon! {}".format(string))  # Using format() method for string formatting
# Using string concatenation
print("Good Afternoon! " + string)  # Using string concatenation


#2
string2 = input("Enter your name:")
date = input("Enter the date:")

letter = '''
Dear string2 
You are selected! 
Date : date '''
print(letter.replace("string2",string2).replace("date",date))  # Using replace() method to replace placeholders in the letter with actual values


 #3
string3 = "This is a python  programming  class"
print(string3.index("  ")) #This code is to detect double spaces in a string so we use index method to return the index of it and -1 if none.
string3.replace("  ", " ") # This line does not modify string3 in place, it returns a new string with the replacements.As strings are immutable in Python, we need to assign the result back to string3 or another variable.
print(string3)  ## This will print the original string as the replace() method does not modify the string in place.
# Assigning the modified string back to string3
string3 = string3.replace("  ", " ")  # Now string3 will have the double spaces replaced with single spaces
print(string3)  # This will print the modified string with single spaces