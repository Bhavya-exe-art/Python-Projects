from typing import List
from Expense import Expense
import calendar
import datetime


def main():
    print(f"Running Expense Tracker")
    expense_file_path = "expenses.csv"
    budget = 1000.00  # Set a budget for the month

    # Get user input for expense.
    expense = get_user_expense()

    # Write their expense to a file.
    save_expense_to_file(expense, expense_file_path)

    # Read file and summarise expense.
    summarise_expenses(expense_file_path, budget)

def get_user_expense():
    print(f"Getting user expense")
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: "))

    expense_categories = [
        "Food",
        "Transport",
        "Entertainment",
        "Utilities",
        "Healthcare",
        "Education",
        "Miscellaneous"
    ]

    while True:
        print("Select a category: ")
        for i, category_name in enumerate(expense_categories):
            print(f" {i + 1}. {category_name}")

        value_range = f"[1 - {len(expense_categories)}]"
        selected_index = int(input(f"Enter a category number {value_range}: ")) - 1


        if selected_index in range(len(expense_categories)): 
            selected_category = expense_categories[selected_index]
            # Pass the name, category, and amount into the Expense constructor
            new_expense = Expense(name=expense_name, category=selected_category, amount=expense_amount)
            return new_expense
        else:
            print("Invalid category. Please try again.")

def save_expense_to_file(expense: Expense, expense_file_path):
    print(f"Saving user expense: {expense} to {expense_file_path}")
    with open(expense_file_path, "a") as f:
        f.write(f"{expense.name}, {expense.amount}, {expense.category}\n")


def summarise_expenses(expense_file_path, budget):
    print(f"Summarising user expense")
    expenses: List[Expense] = []
    with open(expense_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            stripped_line = line.strip()
            expense_name, expense_amount, expense_category = stripped_line.split(",")
            print(expense_name, expense_amount, expense_category)
            line_expense = Expense(name=expense_name, amount=float(expense_amount), category=expense_category)

            expenses.append(line_expense)


    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else: 
            amount_by_category[key] = expense.amount

    print("Expenses by Category:")
    for key, amount in amount_by_category.items():
        print(f" {key}: ${amount:.2f}")

    total_spent = sum([x.amount for x in expenses])
    print(f"You've spent: ${total_spent:.2f}")

    remaining_budget = budget - total_spent
    print(f"Budget Remaining: ${remaining_budget:.2f}")


    now = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    remaining_days = days_in_month - now.day
    print("Remaining days in the current month:", remaining_days)

    daily_budget = remaining_budget / remaining_days
    print(f"Budget per day: ${daily_budget:.2f}")

def green(text):
    return f"\033[92m{text}\033[0m"

if __name__ == "__main__":
    main()


