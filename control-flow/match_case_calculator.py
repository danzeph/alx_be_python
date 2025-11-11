while True:
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        break 
    except ValueError:
        print("Please enter valid integers.\n")


operation = input("Choose the operation (+, -, *, /): ")
result = None

match operation:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = num1 / num2
    case _:
        print("Invalid operation")

if result is not None:
    print(f"The result is {result}.")

