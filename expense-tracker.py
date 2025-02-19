# Import datetime module to handle dates
import datetime

# Creat a dictionary
total_expenses = []

# Function to add an expense
def add_expense():
  amount = input("Enter the amount of your expense:\n")
  date_str = input("Enter the reminder date (YYYY-MM-DD):\n")
  category = input("Where did you spend this money on:\n").lower()
  try:
    amount = float(amount)
    date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
    expense = {"category" : category, "amount": amount, "date":date}
    total_expenses.append(expense)
    print ("A new expense has been added")
    return total_expenses
  except ValueError:
    print("Invalid input. Please enter a valid amount and date (YYYY-MM-DD).")
        
# Function to view all recorded expenses
def view_expense():
  if not total_expenses:
    print("No expense recorded.")
    return
  global expenses_by_category
  # Dictionary to store expenses grouped by category  
  expenses_by_category = {}
  for expense in total_expenses:
    category = expense["category"]
    if category not in expenses_by_category:
      expenses_by_category[category] = []
    expenses_by_category[category].append(expense)
  # Display expenses grouped by category 
  print("\nAll Expenses (Grouped by Category):")
  for category, expenses in expenses_by_category.items():
    print(f"\nCategory: {category}")
    # Sort the list of expenses in each category by date.
    sorted_expenses = sorted(expenses, key=lambda x: x["date"])
    for i, expense in enumerate(sorted_expenses, 1):
      print(f"  {i}. {expense['date']} - ${expense['amount']:.2f}")
           
# Function to calculate total expenses           
def calculate_total_expense():
  # Calculate and display total expense amount
  total = sum (expense["amount"] for expense in total_expenses)
  print (f"Total expenses: ${total:.2f}")


# Function to deleate an expense
def delete_expense():
  if not total_expenses:
    print("No expenses to delete.")
    return
# Group expense by category
  expenses_by_category = {}
  for expense in total_expenses:
    category = expense ["category"]
    if category not in expenses_by_category:
      expenses_by_category[category] = []
    expenses_by_category[category].append(expense)
# Show available categories    
  print("\n Available Categories:")
  for category in expenses_by_category.keys():
    print(f" {category}")
# User select category       
  category_choice = input("\nEnter the category from which you want to delete an expense from: ").lower
  if category_choice not in expenses_by_category:
    print("Invalid choice. Try again.")
    return
# Display expenses in the selected category
  category_expenses = expenses_by_category [category_choice]
  print(f"\n Expense in '{category_choice}':")
  for i, expense in enumerate(category_expenses, 1):
    print(f"{i}.{expense['date']} - ${expense['amount']:.2f}")
# Ask user for the expense to remove       
  try:
      i = int(input("\nEnter the number of expense to remove: "))-1
      if 0<= i < len(category_expenses):
        removed = category_expenses.pop(i)
        total_expenses.remove(removed)
        print(f"Removed expense: {removed['date']} - {removed['category']}: ${removed['amount']:.2f}")
      else:
        print("Invalid number. Try again.")   
  except ValueError:
    print("Invalid input. Please enter a number.") 

# Main loop
while True:
  print("\nExpense Tracker")
  print("1. Add Expense")
  print("2. View Expense")
  print("3. Calculate Total Expense")
  print("4. Delete Expense")
  print("5. Exit")
    
  choice = input("Choose an option: ") 
  if choice == "1":
    add_expense()
  elif choice == "2":
    view_expense()
  elif choice == "3":
    calculate_total_expense()
  elif choice == "4":
    delete_expense()
  elif choice == "5":
    print("Exiting... Goodbye!")
    break   
  else:
    print ("Invalid choice, try again.")  
