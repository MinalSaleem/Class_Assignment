# Built-in Module
import random
print(random.randint(1, 10))  


# User-Defined Module
import module
print(module.multiply(3, 4))


# External Module
import numpy as np
arr = np.array([1, 2, 3])
print(arr)


# Basic Import
import math
print(math.sqrt(16))


# Positional-only Arguments
def power(x, y, /):
    return x ** y
print(power(2, 3)) 


# Keyword-only Arguments
def greet(*, name, message):
    print(f"{message}, {name}!")
greet(name="Saad", message="Hello")


# Arbitrary Arguments
def average(*numbers):
    return sum(numbers)/len(numbers)
print(average(1, 2, 3, 4))


# Arbitrary Keyword Arguments 
def print_data(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_data(name="Saad", age=22, city="Islamabad")


# Generator Function
def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1
counter = count_up_to(5)
print(list(counter))  


# Recursive Function
def sum_to(n):
    if n == 1:
        return 1
    return n + sum_to(n-1)
print(sum_to(5))  


# Anonymous Functions
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))

print(evens)