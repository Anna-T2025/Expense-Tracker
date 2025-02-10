import datetime

# Creat a dictionary
total_expenses = []

def add_expense():
    amount = input("Enter your expense:\n")
    date_str = input("Enter the reminder date (YYYY-MM-DD):\n")
    Category = input("Where did you spend this money on:\n")
    try:
        amount = float(amount)
        date = datetime.strptime(date_str, '%Y-%m-%d').date()
        expense = {"Category" : category, "amount": amount, "date":date}
        total_expenses.append(expense)
        print ("A new expense haas been added")
        return total_expenses
    except ValueError:
        print("Invalid input. Please enter a valid amount and date (YYYY-MM-DD).")

def filter_expenses_by_category(category):
   filtered = [expense for expense in expenses if expense["category"] == category]
   if not filtered:
       print(f"No expenses found for category '{category}'.")
       return
   print(f"\nExpenses for category '{category}':")
   for i, expense in enumerate(filtered, 1):
       print(f"{i}. Amount: ${expense['amount']}, Date: {expense['date']}")

def view_expense():
    if no total_expenses:
        print("No expense recorded.")
        return
    sorted_expense = sort_expense_by_date()
    for index,expense in enumerate (sorted_expense):
        print (f"{index+1}. {date} - {category}: ${amount:.2f}")
        
def calculate_total_expense():
    total = sum (total_expenses["amount"] for expense in total_expenses)
    print (f"Total expenses: ${total:.2f}")

def delete_expense():
    try:
        view_expense()
        index = int(input("Enter the number of the expense to remove:\n")) - 1
        if 0 <= index < len(total_expenses):
           # Remove the selected reminder
           removed = sort_expense_by_date(total_expenses).pop(index)
           print(f"Removed expense: {removed['date']} - {removed['category']}: {removed[amount]}")
        else:
           # Handle invalid index
           print("Invalid number. Please try again.")
    except ValueError:
       # Handle invalid index
       print("Invalid input. Please enter a number.")
   return total_expenses

