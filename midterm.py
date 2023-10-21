# Task 1
# try:
#     name = input("Enter your name please: ")
#     salary = input("Enter your desired salary level: ")
#     if isinstance(salary, int) == False:
#         raise TypeError
#     tax = salary * 0.2
#     print(f"{name}, the tax level you will pay with the salary {salary} is {tax}")
# except TypeError:
#     print(f"{name}, please enter your desired salary as a digit")


# Task 2
# addition = lambda x, y: x + y
# multiplication = lambda x, y: x * y
# division = lambda x, y: x / y
# exponentiation = lambda x, y: x ** y

# print("Please choose the task you want to perform:")
# print("1.Addition")
# print("2.Multiplication")
# print("3.Division")
# print("4.Exponent")

# operation = int(input())
# number1 = input("Enter your first number: ")
# number2 = input("Enter your second number: ")

# result = 0
# if operation == 1:
#     result = addition(number1, number2)
# elif operation == 2:
#     result = multiplication(number1, number2)
# elif operation == 3:
#     result = division(number1, number2)
# elif operation == 4:
#     result = exponentiation(number1, number2)
# print(result)


# Task 3
# def fibonaci(length):
#     sequence = [1, 1] 

#     for i in range(2, length):
#         next_number = sequence[i - 1] + sequence[i - 2]
#         sequence.append(next_number)

#     return sequence

# length = int(input("enter the length of Fibonacci sequence: "))

# if length <= 0:
#     print("you must enter a positive integer!!!")
# else:
#     sequence = fibonaci(length)
#     print("The Fibonacci sequence for {} is".format(length))
#     print(', '.join(map(str, sequence)))

# # Task 4
# unique = set()
# not_unique = []
# while True:
#     print("Please choose the option you want to perform: ")
#     print("1.Enter items")
#     print("2.Exit")
    
#     option = input("enter: ")
    
#     if option == '1':
#         items = input("enter items separated by comma: ")
#         list = [item.strip() for item in items.split(",")]
        
#         for item in list:
#             if list.count(item) > 1:
#                 not_unique.append((item, list.count(item)))
#             else:
#                 unique.add(item)
        
#         print("Items are saved")
#     elif option == '2':
#         break
#     else:
#         print("Invalid option. Please choose 1 or 2.")
# print(f"Unique items: {unique}")
# print(f"Not unique items: {tuple(not_unique)}")

# Task 4    
todos = {}
while True:
    print("Please choose the task you want to perform:")
    print("1.Add Task")
    print("2.View All Tasks")
    print("3.Exit")
    
    task = input("User Input: ")

    if task == '1':
        task = input("Enter the task: ")
        todos[task] = False # not completed as initial value
        print(f'"{task}" was added to the todo list')

    elif task == '2':
        if todos:
            print("tasks:")
            for task, completed in todos.items():
                print(f'{task} {"(completed)" if completed else "(not completed)"}')
        else:
            print("todo list is empty.")

    elif task == '3':
        break

    else:
        print("Please choose a valid option (1-5).")
