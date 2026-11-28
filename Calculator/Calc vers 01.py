print("--- Simple Calculator ---")
print("Choose an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

# Get user choice and numbers
choice = input("Enter choice (1/2/3/4): ")

# Convert input from text to decimal numbers (float)
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform the calculation based on user choice
if choice == '1':
    result = num1 + num2
    print(f"Result: {num1} + {num2} = {result}")

elif choice == '2':
    result = num1 - num2
    print(f"Result: {num1} - {num2} = {result}")

elif choice == '3':
    result = num1 * num2
    print(f"Result: {num1} * {num2} = {result}")

elif choice == '4':
    # Prevent crashing if user tries to divide by zero
    if num2 == 0:
        print("Error! Division by zero is not allowed.")
    else:
        result = num1 / num2
        print(f"Result: {num1} / {num2} = {result}")

else:
    print("Invalid Input! Please select a choice from 1 to 4.")
