# True , False
""" True and False are the two boolean values in Python."""

x = (True == 0)
y = (False == 0)

print(x , y)



# None
"""The Python keyword None represents no value."""

z = None

print(z == 0)
print(z)



# and , or
"""and keyword is a logical operator that returns True if both the operands are True, otherwise False.
or keyword is a logical operator that returns True if any of the operands is True, otherwise False."""

name = input("Enter your name: ")
age = int(input("Enter your age: "))
education = int(input("Enter your education: "))

if ((age >= 20) and (education >= 14)):
    print(f"{name}, you can apply for this job.")
elif ((age >= 20) or (education <= 14)):
    print(f"{name}, you can't apply for this job.")
else:
    print("Apply for another job.")


# not
"""not keyword is a logical operator that returns True if the operand is False, otherwise True."""

case = "win"

if(not(case == "win")):
    print("You win.")
elif(case == "win"):
    print("You lose.")
else:
    print("Come Again.")
    


# in 
"""in m]keyword is membership operator that returns True if the specified object is present in the specified sequence, otherwise False."""

name = "Minal"

print("M" in name)



# is
"""is keyword check if two variables point to the same object in memory. It returns True if the objects are identical."""

a = [2, 7, 13]
b = a
c = [2, 7, 13]

print(a is b)
print(a is c)  #same value but are different objects in memory



# if , elif , else
"""if, elif, and else are conditional statements that are used to control the flow of the program based on some condition."""

runs = int(input("Enter the runs: "))

if(runs >= 250):
    print("Pakistan won the match.")
elif(runs < 250):
    print("Pakistan lose the match.")
else:
    print("Match will play again.")



# for , break , continue 
""" for keyword is use for looping . break keyword is used to break out of the loop. countine keyword skips the current iteration of the loop but does not end the loop."""

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
multipler = 2

for number in numbers:
    if(number*multipler == 8):
        continue
    if(number*multipler == 12):
        break
    print(number * multipler)
print("End of the loop.")



# pass

"""pass is a null statement, a statement that will do nothing"""

x = True

if x:
    pass
else:
    print("False")



# del
"""del keyword is used to delete an object from a list or delete the entire list."""

names = ["Minal", "Darakhshan", "Ariba", "Konain"]
del names[3]

print(names)



# def
"""def keyword is used to define a function"""

def greet():
    print("Hello, World!")

greet()



# return
"""return keyword is used to exit a function and return a value from a function."""

def add():
    return 2 + 3

print(add())



# global
"""global keyword is  used when modify a variable that is not defined in a function but is defined in the global scope"""


weather = "sunny"

def update_weather():
    global weather
    weather = "rainy"
    print("Weather inside function: ", weather)

update_weather()
print("Weather outside function: ", weather)



# nonlocal
"""nonlocal keyword used to declare a variable in a nested function as not local to that function. It allows you to modify variables defined in the enclosing scope from within an inner function."""


def outer_function():
    num = 2
    def inner_function():
        nonlocal num
        num = 3
        print("Inner: ", num)
    inner_function()
    print("Outer: ", num)

outer_function()