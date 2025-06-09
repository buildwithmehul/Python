# program to demonstrate the use of different operators in Python


# Arithmetic Operators
a = 7
b = 4
c = a + b
print(c)
# Assignment Operators
a = 4-2 # Assign 4-2 in a
print(a)
b = 6
# b += 3 # Increment the value of b by 3 and then assign it to b
b -= 3 # Decrement the value of b by 3 and then assign it to b
print(b)

# Comparison Operators
d = 5 > 3
print(d)

d = 5 < 3
print(d)

d = 5==5
print(d)

d = 5 != 3
print(d)



# Logical Operators

e = True or False

# Truth table of 'or' 
print("True or False is ", True or False)
print("True or True is ", True or True)
print("False or True is ", False or True)
print("False or False is ", False or False)

# Truth table of 'and'
print("True and False is ", True and False)
print("True and True is ", True and True)
print("False and True is ", False and True)
print("False and False is ", False and False)

print(not(True))


# Program to demonstrate the use of input function and arithmetic operations
""" 
Basically, when we take input using input function, it takes input as a string. So we need to convert it to an integer using int() function.
If we don't convert it, it is string so concatenation will happen instead of addition.
"""
a = int(input("Enter number 1: "))

b = int(input("Enter number 2: "))

print("Number a is: ", a)
print("Number b is: ", b)
print("Sum is ", a + b)



#Example 1 - Modulo Operator  - gives the remainder of the division of two numbers

a = 57
b = 5

print("Remainder when a is divided by b is", a % b)


#Example 2 - To check the type of a input variable

m = input( " Enter anything:")
t = type(m)
print("The data type of m is" , t)