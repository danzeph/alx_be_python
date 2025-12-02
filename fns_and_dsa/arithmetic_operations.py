def perform_operation(num1, num2, operation):
    result = None
    
    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Cannot divide by Zero"
    else:
        result = "Please Enter a Valid operation (add, subtract, multiply, divide)"
    
    return result
