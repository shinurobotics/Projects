expenses = []

while True:
    print("--- Expense Tracker Menu ---")
    print("1. Add New Expense")
    print("2. View All Expenses")
    print("3. Exit")
    
    choice = input("Choose an option (1-3): ")
    
    if choice == '1':
        # Record expense amount
        amount_input = input("Enter expense amount: ")
        amount = float(amount_input)
        
        # Record expense category
        category = input("Enter category (e.g., Food, Transport, Bills, etc): ")
        
        # Save the expense in a list
        expense_entry = {"amount": amount, "category": category}
        expenses.append(expense_entry)
        
        print("Success! Expense added.")
        
    elif choice == '2':
        print("\n--- Your Expenses ---")
        if len(expenses) == 0:
            print("No expenses recorded yet.")
        else:
            total = 0
            for item in expenses:
                print(f"Category: {item['category']} | Amount: RM{item['amount']:.2f}")
                total += item['amount']
            print(f"Total Spent: RM{total:.2f}")
            
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
