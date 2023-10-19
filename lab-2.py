# def ratio():
#     try:
#         user_input = int(input("Input: "))
#         default_number = 999

#         if user_input > default_number:
#             thousand = user_input // 1000
#             hundred = (user_input // 100) % 10
#             ten = (user_input - ((hundred * 100) + (thousand * 1000))) // 10
#             one = user_input - ((ten * 10) + (hundred * 100) + (thousand * 1000))
#             if (thousand + one) == (hundred - ten):
#                 print("Yes!")
#             else:
#                 print("No!")
#     except ValueError:
#         print("Please, enter your age!")
#     except TypeError:
#         print("Please, enter your number!")


# # ratio()

# def roskomnadzor():
#     try:
#         user_age = int(input("How old are you: "))
#         if user_age >= 18:
#             print("Access denied!")
#         elif user_age < 18:
#             print("Access is allowed!")
#     except ValueError:
#         print("Please, enter your age")
#     except TypeError:
#         print("Please, enter your number!")


# # roskomnadzor()

# def arithmetic_progression():
#     try:
#         user_input_number = int(input("First number: "))
#         user_input_number2 = int(input("Second number: "))
#         user_input_number3 = int(input("Third number: "))

#         if (user_input_number + user_input_number2) == user_input_number3:
#             print("Yes!")
#         else:
#             print("No!")
#     except ValueError:
#         print("Please, enter number!")
#     except TypeError:
#         print("Please, enter number!")


# def average_number():
#     try:
#         user_input_first = int(input("Your first number: "))
#         user_input_second = int(input("Your second number: "))
#         user_input_third = int(input("Your third number: "))

#         list_sort = [user_input_first, user_input_second, user_input_third]

#         list_sort.sort()

#         print(list_sort[1])

#     except ValueError:
#         print("Please, enter number!")
#     except TypeError:
#         print("Please, enter number!")


# # average_number()


# def number_of_days():
#     try:
#         month = int(input("Month: "))

#         list31 = [1, 3, 5, 7, 8, 10, 12]

#         if month > 12 or month <= 0:
#             print("There are only 12 months in a year")
#         elif month in list31:
#             print("31")
#         elif month == 2:
#             print("28")
#         else:
#             print("30")

#     except ValueError:
#         number_of_days()
#     except TypeError:
#         print("Uvuvuvuvuuvu, ERROR")


# # number_of_days()


# def weigh_in_ceremony():
#     try:
#         weight = int(input("Weight: "))

#         if weight < 60:
#             print("Light weight")
#         elif 60 <= weight <= 64:
#             print("First welterweight")
#         elif 64 < weight <= 69:
#             print("Welterweight")
#     except ValueError:
#         print("Value Error")
#     except TypeError:
#         print("You must enter a number")


# # weigh_in_ceremony()

# def password():
#     user_password = input("Password: ")
#     again = input("Repeat the password: ")

#     if user_password == again:
#         print("Password accepted")
#     elif user_password != again:
#         print("Password not accepted")
#         password()


# # password()

# def odd_and_even():
#     try:
#         number = int(input("Number: "))

#         if number in range(1, 10000, 2):
#             print("Odd number")
#         elif number in range(2, 1000, 2):
#             print("Even number")

#     except ValueError:
#         print("ValueError")
#     except TypeError:
#         print("Enter the 'number' ")


# def the_smallest_of_two_numbers():
#     try:
#         first_number = int(input("First number: "))
#         second_number = int(input("Second number: "))

#         lists = [first_number, second_number]

#         for list_for_request in lists:
#             if list_for_request == '\n':
#                 print("I'm not gonna ask you twice.")
#                 print("Stop IT")
#                 return None

#         print(min(lists))

#     except ValueError:
#         print("Value Error")
#     except TypeError:
#         print("You must enter a number")


# # the_smallest_of_two_numbers()

# def age_group():
#     try:
#         age = int(input("Weight: "))

#         if age <= 13:
#             print("Inclusive-childhood;")
#         elif 14 <= age <= 24:
#             print("Adolescence")
#         elif 25 <= age <= 59:
#             print("Maturity")
#         elif 60 <= age:
#             print("Old")
#         else:
#             raise TypeError("sldkfjsldkfjs")

#     except ValueError:
#         print("ValueError")
#     except TypeError:
#         print("you must enter a number")


# age_group()

# def triangle_view():
#     try:
#         triangle_edges_first = int(input("Triangle edges: "))
#         triangle_edges_second = int(input("Triangle edges: "))
#         triangle_leg = int(input("Triangle: "))

#         if triangle_edges_first == triangle_edges_second:
#             print("Isosceles")

#         elif triangle_edges_first == triangle_leg == triangle_edges_second:
#             print("Equilateral")

#         else:
#             print("Versatile")
#     except ValueError:
#         print("ValueError")


# triangle_view()

# x = int(input())
# y = int(input())
# x2 = int(input())
# y2 = int(input())
# if x == x2 or y == y2:
#     print("YES")
# else:
#     print("NO")

# x1 = int(input("Enter the column number: "))
# y1 = int(input("Enter the row number: "))
# x2 = int(input("Enter the column number 2: "))
# у2 = int(input("Enter the row number 2:"))
# if abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1:
#     print("YES")
# else:
#     print("NO")

x = int(input("the initial x: "))
y = int(input("the initial y: "))
x1 = int(input("X coordinate of a prey: "))
y1 = int(input("Y coordinate of a prey: "))

if (y1 - y == 2 or y1 - y == -2 and x1 - x == 1 or x1 - x == -1) or (x1 - x == 2 or x1 - x == -2 and y1 - y == 1 or y1 - y == -1):
    print("YES")
else:
    print("NO")