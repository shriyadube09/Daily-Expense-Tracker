# DAILY EXPENSE TRACKER

expenses = []

def add_expense():
    print("\n--- ADD NEW EXPENSE ---")

    date = input("Enter date: ")
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")

    expense = {
        "date": date,
        "category": category,
        "amount": amount,
        "description": description
    }

    expenses.append(expense)

    print("\nExpense added successfully!")


def view_expenses():
    print("\n--- EXPENSE HISTORY ---")

    if len(expenses) == 0:
        print("No expenses recorded yet.")
    else:
        for i, expense in enumerate(expenses, start=1):
            print("\nExpense", i)
            print("Date:", expense["date"])
            print("Category:", expense["category"])
            print("Amount: Rs.", expense["amount"])
            print("Description:", expense["description"])


def total_expenses():
    total = 0

    for expense in expenses:
        total = total + expense["amount"]

    print("\nTotal Expenses: Rs.", total)


def search_category():
    category = input("\nEnter category to search: ")
    found = False

    for expense in expenses:
        if expense["category"].lower() == category.lower():
            print("\nDate:", expense["date"])
            print("Amount: Rs.", expense["amount"])
            print("Description:", expense["description"])
            found = True

    if found == False:
        print("\nNo expenses found in this category.")


def check_budget(budget):
    total = 0

    for expense in expenses:
        total = total + expense["amount"]

    remaining = budget - total

    print("\nMonthly Budget: Rs.", budget)
    print("Total Spent: Rs.", total)
    print("Remaining Budget: Rs.", remaining)

    if remaining < 0:
        print("Warning! You have exceeded your budget.")
    else:
        print("You are within your budget.")


def main():
    print("===== DAILY EXPENSE TRACKER =====")

    budget = float(input("Enter your monthly budget: Rs. "))

    while True:
        print("\n========== MAIN MENU ==========")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Calculate Total Expenses")
        print("4. Search by Category")
        print("5. Check Remaining Budget")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            total_expenses()

        elif choice == "4":
            search_category()

        elif choice == "5":
            check_budget(budget)

        elif choice == "6":
            print("\nThank you for using Daily Expense Tracker!")
            break

        else:
            print("\nInvalid choice! Please try again.")


main()