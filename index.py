# # Task 1.1
# sequence = [4, 8, 15, 16, 23, 42]
# for number in sequence:
#     print(number, end=' ')

# #Task 1.2
# sequence = [4, 8, 15, 16, 23, 42]
# for number in sequence:
#     print(number)

# # Task 1.3
# user_input = int(input("Enter Number: "))
# for number in range(3):
#     print(number + user_input)
#     number += 1

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

# Task 2.1
schoolchildren = int(input("Enter the number of schoolchildren: "))
tangerines = int(input("Enter the number of tangerines: "))

tangerines_per_student = tangerines // schoolchildren

remaining_tangerines = tangerines % schoolchildren

print(f"{tangerines_per_student}")
print(f"{remaining_tangerines} whole tangerine(s) will remain in the basket.")
