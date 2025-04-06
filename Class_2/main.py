# Arithmetic operators
"""Arithmetic operators are symbols used to perform mathematical operations on numerical values."""

a = 2
b = 13

# Addition 
print(a + b)

# Subtraction
print(a - b)

# Multiplication
print(a * b)

# Division
print(a / b)

# Floor Division
print(a // b)

# Exponent
print(a ** b)




# Assignment operators
"""An assignment operator in Python is used to assign values or expressions to the left-hand side operand. These operators assign the value of the right-hand side operand to the left-hand side operand."""

x = 2

# Addition Assignment Operator
x += 13
print(x)

# Subtraction Assignment Operator
x -= 7
print(x)

# Multiplication Assignment Operator
x *= 5
print(x)

# Division Assignment Operator
x /= 2
print(x)

# Modulus Assignment Operator
x %= 7
print(x)

# Floor Division Assignment Operator
x //= 2
print(x)

# Exponentiation Assignment Operator
x **= 3
print(x)




# Comparison operators
"""Comparison operators in Python compare values and determine relationships between them.
These operators return either True or False. It is based on whether the comparison is true or false, respectively."""

a = 5
b = 7

# Equality Operator
print(a == b)

# Inequality Operator
print(a != b)

# Greater Than Operator
print(a > b)

# Less Than Operator
print(a < b)




# Logical operators
"""Logical operators are used on conditional statements (either True or False)."""

x = 2
y = 13

print((x < y) and (x == y))
print((x < y) or (x == y))
print(not(x < y))




# Identity operators
"""The Python Identity Operators are used to compare the objects if both the objects are actually of the same data type and share the same memory location."""

a = [ 2, 7, 13, 5]
b = [ 2, 7, 13, 5] 
m = a

# IS Operator
print(a is m)
print(a is b)

# IS Not Operator
print(a is not m)
print(a is not b)




# Membership operators
"""The membership operators in Python help us determine whether an item is present in a given container type object, or in other words, whether an item is a member of the given container type object."""

names = ["Minal", "Darakhshan", "Konain"]

# In Operator
print("Minal" in names)
print("Ariba" in names)

# Not In Operator
print("Ariba" not in names)
print("Darakhshan" not in names)




# Bitwise operators
"""Python bitwise operators are normally used to perform bitwise operations on integer-type objects. However, instead of treating the object as a whole, it is treated as a string of bits. Different operations are done on each bit in the string."""

a = 13
b = 5

# Bitwise AND Operator
result = a & b 
print(result)

# Bitwise OR Operator
result = a | b 
print(result)

# Bitwise XOR Operator
result = a ^ b 
print(result)

# Bitwise NOT Operator
result = ~a
print(result)

# Bitwise Left Shift Operator
result = a << 1
print(result)

# Biwtise Right Shift Operator
result = a >> 1
print(result)