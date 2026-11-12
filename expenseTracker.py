import calendar
import datetime

from expense import Expense

def main():
    print("Welcome to CashTrack!")
    expense_file_path = "expenses.csv"
    budget = float(input("Enter your monthly budget: "))

    #Get user input for expense details
    expense = get_user_expense()
    print(expense)

    #Write their expense to a file
    save_expense_to_file(expense, expense_file_path)

    #Read file and summarize expenses
    summarize_expenses(expense_file_path, budget)


def get_user_expense():
    expense_name = input("Enter the name of the expense: ")
    expense_amount = float(input("Enter the amount of the expense: "))

    expense_categories = ["Food", "Transportation", "Entertainment", "Home", "Misc"]
    while True:
        print("Select a category for the expense:")
        for i, cat in enumerate(expense_categories):
            print(f"  {i + 1}. {cat}")
        cat_choice = input("Enter the number of the category: ")
        if cat_choice.isdigit() and 1 <= int(cat_choice) <= len(expense_categories):
            selected_expense_category = expense_categories[int(cat_choice) - 1]
            new_expense = Expense(
                expense_name, expense_amount, selected_expense_category
            )
            return new_expense
    
        else:
            print("Invalid choice. Please try again.")


def save_expense_to_file(expense, expense_file_path):
    print(f"Saving {expense} to {expense_file_path}")
    with open(expense_file_path, "a") as f:
        f.write(f"{expense.name},{expense.category},{expense.amount}\n")


def summarize_expenses(expense_file_path, budget):
    print("Summarizing expenses...")
    expenses = []
    with open(expense_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            expense_name, expense_category, expense_amount = line.strip().split(",")
            line_expense = Expense(
                expense_name, float(expense_amount), expense_category
            )
            expenses.append(line_expense)

    amt_by_category = {}
    for expense in expenses:
        if expense.category not in amt_by_category:
            amt_by_category[expense.category] = expense.amount
        else:
            amt_by_category[expense.category] += expense.amount

    print("Expenses by category:")
    for category, total in amt_by_category.items():
        print(f"  {category}: ${total:.2f}")

    total_spent = sum([expense.amount for expense in expenses])
    remaining_budget = budget - total_spent
    print(f"Total spent: ${total_spent:.2f}")
    print(f"Remaining budget: ${remaining_budget:.2f}")

    now = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    remaining_days = days_in_month - now.day
    daily_budget = remaining_budget / remaining_days if remaining_days > 0 else 0
    print(f"Daily budget: ${daily_budget:.2f}")


if __name__ == "__main__":
    main()