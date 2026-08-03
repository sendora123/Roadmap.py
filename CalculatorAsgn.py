def calculator(num1, num2):
    operator = input("Enter operator (+, -, /, *): ")

    if operator == "+":
        Result = num1 + num2
    elif operator == "-":
        Result = num1 - num2
    elif operator == "*":
        Result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            return "Error: Cannot divide by zero."
        Result = num1 / num2
    else:
        return f"Error: '{operator}' is not a valid operator. Use +, -, *, or /"

    return Result


# MAIN PROGRAM
while True:
    try:
        num1 = float(input("\nEnter the first number:  "))
        num2 = float(input("Enter the second number: "))
        Result = calculator(num1, num2)
        print(f"\nThe Result is: {Result}")
    except ValueError:
        print("Error: Please enter valid numbers.")

    again = input("\nDo you want to calculate again? (yes/no): ").strip().lower()
    if again != "yes":
        print("\nThank you for using the calculator. Goodbye!")
        break