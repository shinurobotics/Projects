from datetime import datetime

expenses = []

while True:
    print("\n--- Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Expenses & Total")
    print("3. Edit Expense")
    print("4. Delete Expense")
    print("5. Search by Category")
    print("6. Monthly Summary")
    print("7. Exit")

    choice = input("Choose (1-7): ").strip()

    # 1. Add new expense
    if choice == "1":
        while True:
            try:
                amount = float(input("Amount (RM): "))
                if amount > 0:
                    break
                print("Enter a number above 0.")
            except ValueError:
                print("Invalid number. Try again.")

        while True:
            category = input("Category (e.g., Food, Transport): ").strip().title()
            if category:
                break
            print("Category cannot be empty.")

        while True:
            description = input("Description: ").strip()
            if description:
                break
            print("Description cannot be empty.")

        while True:
            date_input = input("Date YYYY-MM-DD (or press Enter for today): ").strip()
            if date_input == "":
                date_str = datetime.today().strftime("%d-%m-%Y")
                break
            try:
                datetime.strptime(date_input, "%d-%m-%Y")
                date_str = date_input
                break
            except ValueError:
                print("Use format DD-MM-YYYY (e.g., 27-11-2026).")

        expenses.append({
            "amount": amount,
            "category": category,
            "description": description,
            "date": date_str
        })
        print("Expense added.")

    # 2. View all expenses and total
    elif choice == '2':
        print("\n--- Your Expenses ---")
        
        if len(expenses) == 0:
            print("No expenses recorded yet.")
        
        else:
            total = 0
            for item in expenses:
                print(f"Date: {item['date']} | Category: {item['category']} | Amount: RM{item['amount']:.2f} | Description: {item['description']}")
                total += item['amount']
                print(f"Total Spent: RM{total:.2f}")


    # 3. Edit an expense
    elif choice == "3":
        if len(expenses) == 0:
            print("No expenses to edit.")

        else:
            print("\n--- Your Expenses ---")
            count = 1
            for item in expenses:
                print(f"{count}. {item['category']} - RM{item['amount']:.2f}")
                count += 1
                try:
                    num = int(input("Enter expense number to edit: "))
                    item = expenses[num - 1]
                except (ValueError, IndexError):
                    print("Invalid number.")
                    continue

                new_amt = input("New amount (Enter to keep): ").strip()
                if new_amt:
                    try:
                        val = float(new_amt)
                        if val > 0:
                            item["amount"] = val
                        else:
                            print("Invalid amount. Old amount kept.")
                    except ValueError:
                        print("Invalid number. Old amount kept.")
                        
                new_cat = input("New category (Enter to keep): ").strip().title()
                if new_cat:
                    item["category"] = new_cat

        new_desc = input("New description (Enter to keep): ").strip()

        if new_desc:
            item["description"] = new_desc

        new_date = input("New date DD-MM-YYYY (Enter to keep): ").strip()
        if new_date:
            try:
                datetime.strptime(new_date, "%d-%m-%Y")
                item["date"] = new_date
            except ValueError:
                print("Invalid date. Old date kept.")

        print("Expense updated.")

    # 4. Delete an expense
    elif choice == "4":
        if len(expenses) == "0":
            print("No expenses to delete.")
        else:
            print("\n--- Your Expenses ---")
            count = "1"
            for item in expenses:
                print(f"{count}. [{item['date']}] {item['category']} - RM{item['amount']:.2f} ({item['description']})")
                count += 1
            try:
                num = int(input("Enter expense number to delete: "))
                removed = expenses.pop(num - 1)
                print(f"Deleted: {removed['description']} (RM{removed['amount']:.2f})")
            except(ValueError,IndexError):
                print("Invalid number")
                
    # 5. Search by category
    elif choice == "5":
        search_cat = input("Search category: ").strip().lower()
        found = []
        for item in expenses:
            if item["category"].lower() == search_cat:
                found.append(item)
        if len(found) == 0:
            print("No matching expenses.")
        else:
            sub_total = 0
            for item in found:
                print(f"[{item['date']}] {item['category']} - RM{item['amount']:.2f} ({item['description']})")
                sub_total += item["amount"]
            print(f"Category Total: RM{sub_total:.2f}")

    # 6. Monthly summary
    elif choice == "6":
        if len(expenses) == 0:
            print("No expenses yet.")
        else:
            monthly = {}
            for item in expenses:
                month = item["date"][3:10]
                if month in monthly:
                    monthly[month] += item["amount"]
                else:
                    monthly[month] = item["amount"]
            for month in monthly:
                print(f"{month}: RM{monthly[month]:.2f}")

    # 7. Exit
    elif choice == "7":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Enter 1-7.")
