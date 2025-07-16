#LISTS IN PYTHON
# Lists are ordered, mutable, and allow duplicate elements. They are a collection of different data types and mutable at the same time.
# Lists are defined using square brackets []. They can be indexed and sliced like strings.                                                                                                                      

list = ["Apple", "Banana", 34, 1.5, True, None, "Rohan", "Rocky"]
print(list[5])
print(list[0]) #indexing starts from 0

list[0] = "Mango"  #Unlike strings, lists are mutable
print(list[0])  # Now it will print "Mango" 

print(list[1:4])  # Slicing the list from index 1 to 3 (4 is not included)
print(list[-1])  # Accessing the last element using negative indexing
print(list[1:])  # Slicing from index 1 to the end of the list
print(list[:3])  # Slicing from the start to index 2 (3 is not included)
print(list[:-3])  # Slicing from the start to the third last element (not included)
print(list[-4:-1])  # Slicing from the fourth last element to the secondlast element            
print(list[-4:])  # Slicing from the fourth last element to the end of the list

# Lists Methods
#Unlike strings where a new string is created when modified, lists are mutable and can be changed "in place".

list.append("Rahul")  # Adds an item to the end of the list
print(list)  

list.insert(2, "Rohan")  # Inserts an item at a specific index (2 in this case)  // ".insert()" requires two arguments: the index and the item to insert. Otherwise, it will raise a TypeError.
print(list)  

list.remove("Banana")  # Removes the first occurrence of "Banana" from the list // ".remove()" requires the specific item to remove and never the index. It raises a ValueError if given the index.
print(list)  

print(list.pop(3)) # prints the item that is removed from the list at index 3
  # Removes and returns the item at index 3 from the list // ".pop()" requires the index of the item to remove and never the item itself.
print(list)  


list1 = [3, 46, 4, 2, 56, 43, 34, 22, 1, 0.3, 0.1]

list1.pop()  # Removes and returns the last item from the list
print(list1)    # Here it will remove the last item (0.1) from the list

list1.sort() # Sorts the list in ascending order
print(list1)  # Prints the sorted list

list1.pop()
print(list1)  #Here it will remove the last item after getting sorted that is 56

""" This shows us that every function we apply mutates / changes the original list.
 If any other function is applied, it is applied on the mutated list."""

list1.reverse()  # Reverses the order of the list
print(list1)  # Prints the reversed list


