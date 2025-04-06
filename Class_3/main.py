# and
user_age = 19

is_student = True

if user_age < 18 and is_student:
    print('You can vote')
else:
    print('You can not vote')

# or
age = 55
if age < 18 or age > 50:
    print('you can get a discount')
else:
    print('you can not get a discount')

# not

is_student = False
if not is_student:
    print('You are a student')
else:
    print('You are not a student')


# If statement

country = 'pakistan'
if country == country:
    print("Karachi is capital of Pakistan.")

# else statement
country_name = "Pakistan"
if country_name == "Pakistan":
    print("Karachi is the city of Pakistan")
else:
    print("Something wrong")

# elif statement

fruit = 'banana'

if fruit == 'apple':
    print('Apples are crunchy and sweet!')

elif fruit == 'banana':
    print('Bananas give you quick energy!')

elif fruit == 'mango': 
    print('Mangoes are the king of fruits!')

else:
    print('I haven’t heard much about that fruit.')


# same same but different (name)

subject = 'math'

if subject == 'science':
    print("Science is full of exciting experiments!")

elif subject == 'english':
    print("English helps you become a better communicator.")

elif subject == 'math':
    print("Math is all about logic and numbers!")

else:
    print("That's an interesting subject!")


# Nested if statement

is_registered = True
attendance_percentage = 85

if is_registered:
    print("You are registered for the exam.")

    if attendance_percentage >= 75:
        print("You are eligible to take the exam.")
    else:
        print("Your attendance is too low.")
else:
    print("Please register before the exam.")
