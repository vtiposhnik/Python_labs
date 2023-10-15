try:
    num1 = float(input("Enter the number: "))
    operation = input("Enter operator (+, -, *, /, %): ")
    num2 = float(input("Enter second number: "))
    result = 0
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            raise ZeroDivisionError("You must not divide by zero!")
    elif operation == '%':
        result = num1 % num2
    elif operation == '**':
        resultSqr = [num1 ** 2, num2 ** 2]
    else:
        raise ValueError("You entered a wrong value!")
    print(f"Result: {result:.3f}")
except ValueError as valErr:
    print(f"Error: {valErr}")
except ZeroDivisionError as zeroDivErr:
    print(f"Error: {zeroDivErr}")