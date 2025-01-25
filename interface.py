from expense_tracker import Expense_Management

class userInterface:
    def __init__(self, filename):
        obj = Expense_Management()
        while True:
            print("\n===Welcome to Personal Expense Tracker===\n")
            print("1. Add new expense")
            print("2. View all expenses")
            print("3. Summary expenses")
            print("4. Exit")
            print("\n=======================")
            num = input("Press Enter a number to continue: ")
            if num == "1":
                category = input("Enter the category you would like to add: "
                                 "\n1. Food"
                                 "\n2. Rent"
                                 "\n3. Utilities"
                                 "\n4. Travel"
                                 "\n5. Miscellaneous\n")
                amount = float(input("Enter the amount you would like to add: "))
                description = input("Enter the description you would like to add: ")
                obj.add_expense(filename,category, amount, description)
            elif num == "2":
                obj.view_expense(filename)
            elif num == "3":
                obj.summary_reports(filename)
            else:
                break






