from auth import *

obj = User_Authentication()

while True:
    print("Welcome to Personal Expense Tracker\n")
    print("1. Signup")
    print("2. Login")
    print("3. Exit")

    num = input("Press Enter a number to continue: ")
    if num == "1":
        name = input("Enter your Name: ")
        username = input("Enter your username: ")
        email = input("Enter your Email: ")
        password = input("Enter your password: ")
        obj.signup(name, username, email, password)
    elif num == "2":
        email = input("Please enter your email: ")
        password = input("Please enter your password: ")
        obj.login(email, password)
        break
    elif num == "3":
        break
    else:
        print("Invalid Input")