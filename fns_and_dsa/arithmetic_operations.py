def perform_operation(num1, num2, operation):
  resullt = None
  match operation:
    case "add":
      result = num1 + num2
    case "subtract":
      result = num1 - num2
    case "multiply":
      result = num1 * num2
    case "divide":
      if (num2 > 0):
        result = num1 / num2
      else:
        result = "Cannot divide by Zero"
    case _:
      result = "Please Enter a Valid operation(add, subtract, multiply, divide,"
    
  return result
