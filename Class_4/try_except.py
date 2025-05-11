# try block
try:
    age = int(input("Enter your age: "))
    print(f"You are {age} years old")
except ValueError:
    print("Please enter a valid number!")


# else block
try:
    x = float(input("Enter a number: "))
    y = float(input("Enter another number: "))
except ValueError:
    print("Invalid input! Please enter numbers.")
else:
    print(f"Sum: {x + y}")


# finally block
def login(username, password):
    authenticated = False
    try:
        if not username or not password:
            raise ValueError("Username and password required")
        
        if username == "admin" and password == "secret123":
            authenticated = True
            print("Login successful!")
        else:
            raise PermissionError("Invalid credentials")
            
    except ValueError as e:
        print(f"Validation error: {e}")
    except PermissionError as e:
        print(f"Security error: {e}")
    finally:
        print(f"Login attempt completed (Success: {authenticated})")
        print("Session log updated\n")

login("admin", "secret123")  
login("user", "wrongpass")   
login("", "")          


# raise
def calculate_bmi(weight, height):
    if weight <= 0 or height <= 0:
        raise ValueError("Weight and height must be positive numbers")
    return weight / (height ** 2)

try:
    bmi = calculate_bmi(-70, 1.75)
except ValueError as e:
    print(e)


# NoReturn
from typing import NoReturn

def fail_immediately(reason: str) -> NoReturn:
    print(f"Critical failure: {reason}")
    exit(1)

try:
    fail_immediately("Disk full")
    print("This will never print")
except SystemExit:
    print("Program exited cleanly")