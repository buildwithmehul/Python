#TUPLES IN PYTHON
# Tuples are ordered and allow duplicate elements. They are a collection of different data types and immutable at the same time.
# Tuples are defined using parentheses (). They can be indexed and sliced like lists.
# The differnce between tuples and lists is that tuples are immutable, meaning once created, their elements cannot be changed, added, or removed.

tuple0 = (1,4,5,6,7,8,4)
print(type(tuple))

empty_tuple = ()  # An empty tuple can be created using parentheses with no elements inside
print(empty_tuple)  # This will print an empty tuple

tuple1 =(1)
print(type(tuple1))  # This will print <class 'int'> because python interprets this as an integer enclosed in parentheses, not a tuple.

tuple2 = (1,)  # To create a single-element tuple, you need to include a comma after the element, that's how python recognizes it as a tuple.
print(type(tuple2))  # Now this will print <class 'tuple'>.


tuple3 = ("Apple", "Banana", 34, 1.5, True, None,34, "Rohan", "Rocky")
print(tuple3[4])
''' tuple3[4] = "Mango" '''  # This will raise a TypeError because tuples are immutable and cannot be changed after creation.


#Indexing and Slicing

print(tuple3[0])  # Indexing starts from 0

print(tuple3[1:4])  # Slicing the tuple from index 1 to 3 (4 is not included)
print(tuple3[-1])  # Accessing the last element using negative indexing
print(tuple3[1:])  # Slicing from index 1 to the end of the tuple
print(tuple3[:3])  # Slicing from the start to index 2 (3 is not included)
print(tuple3[:-3])  # Slicing from the start to the third last element (not included)
print(tuple3[-4:-1])  # Slicing from the fourth last element to the secondlast element
print(tuple3[-4:])  # Slicing from the fourth last element to the end of the tuple


#Tuples Methods
# Unlike lists, tuples have very few methods because they are immutable.

tuple_count = tuple3.count("Apple")  # Counts the number of occurrences of "Apple" in the tuple
print(tuple_count)  # Prints the count of "Apple" 

print(tuple3.count(34))  # Counts the number of occurrences of 34 in the tuple

tuple_index = tuple3.index("Rohan")  # Finds the index of the first occurrence of "Rohan" in the tuple
print(tuple_index)  # Prints the index of "Rohan"

print(tuple3.index(34))  # Finds the index of the first occurrence of 34 in the tuple( first occurrence only so 2)

print(len(tuple3))  # Returns the number of elements in the tuple


#Concatenation 
tuple4 = tuple3 + ("Grapes", "Orange")  # Concatenating two tuples
print(tuple4)  # Prints the concatenated tuple

tuple5 =(1,3,4)
tuple6 =(5,6,7)
tuple7 = tuple5 + tuple6  # Concatenating two tuples
print(tuple7)  # Prints the concatenated tuple
tuple8 = tuple6 + tuple5  # Concatenating in reverse order
#This shows that the order of concatenation matters, and the tuples are combined in the order they are added. That is Concatenation is not commutative.
print(tuple8)

#Repetition
tuple9 = tuple5 * 2  # Repeating the tuple twice
print(tuple9)  # Prints the repeated tuple

tuple10 = tuple4 * 3  # Repeating the concatenated tuple thrice
print(tuple10)  # Prints the repeated concatenated tuple



# Converting a list to a tuple
# Lists can be converted to tuples using the `tuple()` function.
list1 = ["Apple", "Banana", 34, 1.5, True, None, "Rohan", "Rocky"]
list1 = tuple(list1)  # Converting the list to a tuple
print(list1)  # This will print the tuple created from the list
print(type(list1))  # This will print <class 'tuple'> because it is a tuple, not a list.
# Note: The tuple type is a built-in type in Python, so using `tuple` as a variable name is not recommended as it shadows the built-in type.



# Converting a tuple to a list
tuple3 = ("Apple", "Banana", 34, 1.5, True, None,34, "Rohan", "Rocky")
tuplee = list(tuple3)  # Converting the tuple to a list
print(tuplee)  # This will print the list created from the tuple
print(type(tuplee))  # This will print <class 'list'>, confirming the conversion from tuple to list
# Note: The list type is also a built-in type in Python, so using `list` as a variable name is not recommended as it shadows the built-in type.