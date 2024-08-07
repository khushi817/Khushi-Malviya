# Get user input for two numbers and an operation
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Choose an operation:")
print("+ for Addition")
print("- for Subtraction")
print("* for Multiplication")
print("/ for Division")

operation = input("Enter your choice (+/-/*/): ")

# Perform the calculation based on the user's choice
if operation == "+":
    result = num1 + num2
    print(f"The result of the addition is: {result}")
elif operation == "-":
    result = num1 - num2
    print(f"The result of the subtraction is: {result}")
elif operation == "*":
    result = num1 * num2
    print(f"The result of the multiplication is: {result}")
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"The result of the division is: {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation choice. Please try again.")