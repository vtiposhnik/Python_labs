# # Task 1.1
# sequence = [4, 8, 15, 16, 23, 42]
# for number in sequence:
#     print(number, end=' ')

# #Task 1.2
# sequence = [4, 8, 15, 16, 23, 42]
# for number in sequence:
#     print(number)

# # Task 1.3
# try:
#     user_input = int(input("Enter Number: "))
#     for number in range(3):
#         print(number + user_input)
#         number += 1
# except ValueError: 
#     print("Invalid input. Please enter an integer.")
    

# # Task 1.4
# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))
# number3 = int(input("Enter the third number: "))
# total_sum = number1 + number2 + number3
# print("Sum: ", total_sum)

# # Task 1.5
# edge_length = float(input("Enter the edge length of the cube: "))

# volume = edge_length ** 3

# surface_area = 6 * (edge_length ** 2)

# print(f"Volume: {volume}")
# print(f"Total surface area: {surface_area}")

# # Task 2.1
# schoolchildren = int(input("Enter the number of schoolchildren: "))
# tangerines = int(input("Enter the number of tangerines: "))

# tangerines_per_student = tangerines // schoolchildren

# remaining_tangerines = tangerines % schoolchildren

# print(f"{tangerines_per_student}")
# print(f"{remaining_tangerines} whole tangerine(s) will remain in the basket.")

    population = int(input("Enter the population of the universe: "))
    if population % 2 == 0:        alive = population // 2
    else:        alive = (population + 1) // 2
    print("Number of survivors:", alive)
    # 4    NUM1 = int(input("Enter a number: "))
    Result = NUM1 << 1    if Result == 0:
        print("The result of << is zero. Please enter a different number.")    else:
        print("The result of << is", Result)
        # 5        try:
            num1 = float(input("Please enter the first number: "))            num2 = float(input("Please enter the second number: "))
            operation = input("Please choose the operation (+, -, *, /): ")            if operation == '+':
                result = num1 + num2            elif operation == '-':
                result = num1 - num2            elif operation == '*':
                result = num1 * num2            elif operation == '/':
                if num2 != 0:                    result = num1 / num2
                else:                    raise ZeroDivisionError("Division by zero is not allowed.")
            else:                raise ValueError("Invalid operation entered.")
            print(f"{num1} {operation} {num2} = {result:.3f}")
        except ValueError as ve:            print(f"Error: {ve}")
        except ZeroDivisionError as zde:            print(f"Error: {zde}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")