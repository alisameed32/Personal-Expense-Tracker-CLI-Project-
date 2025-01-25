import json
from datetime import datetime


class Expense_Management:

    def add_expense(self, filename, category, amount, description):
        categories = {
            1: "Food",
            2: "Rent",
            3: "Utilities",
            4: "Travel",
            5: "Miscellaneous"
        }
        new_data = {
            'date': datetime.now().strftime("%Y-%m-%d"),
            'category': categories[int(category)],
            'amount': amount,
            'description': description
        }
        data = []
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
        except:
            data = []

        data.append(new_data)
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)


    def view_expense(self, filename):
       try:
           with open(filename, 'r') as file:
               data = json.load(file)
               print(data)
       except:
           raise FileNotFoundError


    def  summary_reports(self, filename):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                category_summary = {}
                for expense in data:
                    category = expense['category']
                    amount = expense['amount']

                    # Initialize category if not already present
                    if category not in category_summary:
                        category_summary[category] = {'count': 0, 'total_amount': 0}

                    # Increment count and total amount for the category
                    category_summary[category]['count'] += 1
                    category_summary[category]['total_amount'] += amount

                print("Summary Report:")
                print(f"{'Category':<15}{'Count':<10}{'Total Expense'}")
                print("-" * 35)

                for category, details in category_summary.items():
                    print(f"{category:<15}{details['count']:<10}{details['total_amount']}")

        except FileNotFoundError:
            print("File not found. Please add expenses first.")
        except json.JSONDecodeError:
            print("Error reading the file. Please ensure it contains valid JSON data.")










