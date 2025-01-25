# Personal-Expense-Tracker--CLI-Project-
 
## Project Overview

The Personal Expense Tracker is a command-line application that helps users manage their personal finances by tracking expenses, generating summaries, and storing data persistently. The project is designed with a modular structure, making it easy to expand functionality and maintain the code.

### Core Objectives

#### Primary Goals:

1. Add, view, and manage personal expenses.
2. Store expenses persistently in a file (CSV, JSON, or plain text).
3. Display meaningful summaries and reports.

### Features

#### 1. Expense Management

###### Add an Expense:

###### Input fields:

Date: Defaults to today’s date if not provided.
Category: Pre-defined categories (e.g., Food, Rent, Utilities, Travel, Miscellaneous).
Amount: Validates to ensure it’s a positive number.
Description: Optional field for additional details.
Expenses are saved in a file with appropriate formatting.

##### View All Expenses:

Displays a neatly formatted list of all expenses (date, category, amount, description).

##### Summary Reports:

Displays total expenses
By category (e.g., total spending on Food, Rent, etc.).

### 2. User Authentication (Optional):

Signup: Allows users to create an account (username/password).
Login: Authenticates users based on saved credentials.
Data Security: User credentials are securely stored in a file (e.g., hashed in JSON or CSV).

### File Handling


### Project Structure

#### Files and Folders:

1. main.py: Entry point of the application. Includes a menu-driven interface for user interaction.
2. expense_tracker.py: Core functions for expense management (add, view, summarize).
3. auth.py (Optional for user authentication): Handles login and signup functionality.
4. data/expenses.csv: File to store user expenses.
5. data/users.json (Optional): File to store user credentials.

### Menu-Driven CLI Design


==== Personal Expense Tracker ====
1. Add a new expense
2. View all expenses
3. View summary report
4. Exit
=================================
Enter your choice:

For each choice, the respective function (e.g., add_expense(), view_expenses()) will be called.

### License

This project is licensed under the MIT License. Feel free to use, modify, and distribute it as per the license terms.
