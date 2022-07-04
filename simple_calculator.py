print("Simple calculator\n")
print("Please. Enter two numbers and what operation you want to perform.")

num1 = float(input("Type first number: "))
num2 = float(input("Type second number: "))

print("\nOperation:\n"
        "1. Addition\n"
        "2. Subtraction\n"
        "3. Multiplication\n"
        "4. Division\n")

operation = input("Choose operation:")

if operation == "1":
    print("\nResult: ", num1 + num2)
elif operation == "2":
    print("\nResult: ", num1 - num2)
elif operation == "3":
    print("\nResult: ", num1 * num2)
elif operation == "4":
    print("\nResult: ", num1 / num2)
else:
    print("Wrong number. There is no such operation")