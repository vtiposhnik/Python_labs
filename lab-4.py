# 1.1 Problem
while True:
    try:
        user_input = input("Enter a space-free string: ")
        # checking for spaces in the input
        if any(char.isspace() for char in user_input):
            raise ValueError("Input contains spaces. Please try again.")
        # create a tuple from the input
        char_tuple = tuple(user_input)
        # display the tuple
        print(f"Created tuple: {char_tuple}")
        break  # exit the loop if input is valid
    except ValueError as e:
        print(e)

# 1.2 Problem
while True:
    try:
        user_input = input("Enter a tuple as a string: ")
        char_tuple = eval(user_input)        # check if the result is a valid tuple
        
        # check if it's a valid tuple with single-character strings
        if not isinstance(char_tuple, tuple) or not all(isinstance(char, str) and len(char) == 1 for char in char_tuple):
            raise ValueError("Invalid input. Enter a valid tuple of single-character strings.")
        
        result_string = ''.join(char_tuple)        # Convert the tuple into a string
        print("Result:", result_string)
        break
    except (ValueError, SyntaxError) as e:
        print("Error:", e)

# 1.3 Problem
try:
    # define two input tuples
    tuple_A = (1, 2, 3, 4, 5, 6, 7)
    tuple_B = (5, 6, 7, 9, 7, 1, 10, 10)
    # calculate half lengths of both tuples
    half_len_A = len(tuple_A) // 2
    half_len_B = len(tuple_B) // 2

    # if both tuples have an even number of elements
    if len(tuple_A) % 2 != 0 or len(tuple_B) % 2 != 0:
        raise ValueError("Both tuples must have an even number of elements.")
    # combine the first half of A and the second half of B
    result_tuple = tuple_A[:half_len_A] + tuple_B[half_len_B:]
    # display the result
    print(result_tuple)

except ValueError as e:
    print("Error:", e)

# 1.4 Problem
try:
    user_elements = []
    # keep taking user input until 'done' is entered
    while True:
        user_input = input("enter an element: ")
        if user_input.lower() == 'done':
            break
        user_elements.append(user_input)
    # create a tuple from the user's input elements
    input_tuple = tuple(user_elements)

    element_counts = {}

    # count the occurrences of each element in the tuple
    for element in input_tuple:
        if element in element_counts:
            element_counts[element] += 1
        else:
            element_counts[element] = 1
    # create a tuple of elements and their occurrence counts
    result_tuple = tuple((element, count) for element, count in element_counts.items())

    # display the elements and their occurrences
    print(f"elements and their occurrences: {result_tuple}")

except Exception as e:
    # display an error message if an exception occurs
    print("error:", e)

# 1.5 Problem
try:
    # initialize empty tuples
    int_tuple = ()
    float_tuple = ()
    str_tuple = ()

    while True:
        # take user input
        user_input = input("enter a data object: ")
        if user_input.lower() == 'done':
            break
        elif user_input.isdigit():
            int_tuple += (int(user_input),)
        elif user_input.replace('.', '', 1).isdigit():
            float_tuple += (float(user_input),)
        else:
            str_tuple += (user_input,)
    # display the resulting tuples
    print(int_tuple)
    print(float_tuple)
    print(str_tuple)

except Exception as e:
    # display an error message if an exception occurs
    print("error:", e)

# 2.1 Problem
while True:
    try:
        # take user input
        user_input = input("enter a string without whitespaces: ")

        # check for whitespaces in the input
        if any(char.isspace() for char in user_input):
            raise ValueError("input contains whitespaces. please enter a string without whitespaces.")
        # create a set from the input
        char_set = {char for char in user_input}
        # display the created set
        print(f"created set is: {char_set}")
        break

    except ValueError as e:
        # display an error message if there are whitespaces
        print(e)

# 2.2 Problem
while True:
    try:
        # take user input for set A and convert to a set of integers
        input_A = input("enter elements for set A: ")
        set_A = set(map(int, input_A.split(',')))

        # take user input for set B and convert to a set of integers
        input_B = input("enter elements for set B: ")
        set_B = set(map(int, input_B.split(',')))
        # calculate the symmetric difference
        difference_A_B = set_A - set_B
        difference_B_A = set_B - set_A
        result_set = difference_A_B.union(difference_B_A)

        # display the result set
        print(result_set)

        break

    except ValueError:
        # display an error message for invalid input
        print("Invalid input BRO!!! Please enter comma-separated integers for both sets.")

# 2.3 Problem
try:
    # take user input for set A and convert to a set of integers
    input_A = input("enter elements for set A (comma-separated): ")
    set_A = set(map(int, input_A.split(',')))
    # take user input for set B and convert to a set of integers
    input_B = input("enter elements for set B (comma-separated): ")
    set_B = set(map(int, input_B.split(',')))

    # calculate the difference of set A with set B
    set_A.difference_update(set_B)
    # display the modified set A
    print(set_A)

except ValueError as e:
    # display an error message if an exception occurs
    print("error:", e)

# 2.4 Problem
try:
    # take user input for set A and convert to a set of integers
    input_A = input("enter elements for set A (comma-separated): ")
    set_A = set(map(int, input_A.split(',')))

    # take user input for set B and convert to a set of integers
    input_B = input("enter elements for set B (comma-separated): ")
    set_B = set(map(int, input_B.split(',')))
    # take user input for set C and convert to a set of integers
    input_C = input("enter elements for set C (comma-separated): ")
    set_C = set(map(int, input_C.split(',')))
    # find common elements between set A and set B
    common_elements = set_A.intersection(set_B)

    # add the common elements to set C
    set_C.update(common_elements)

    # display the updated set C
    print(f"updated set_C: {set_C}")

except ValueError as e:
    # display an error message if an exception occurs
    print("error:", e)

# 2.5 Problem
import itertools
try:
    # take user input for superset A and convert to a set of integers
    input_A = input("enter elements for superset A (comma-separated): ")
    A = set(map(int, input_A.split(',')))

    # take user input for the size of each set (n)
    n = int(input("enter the size of each set (n): "))
    # take user input for the number of sets to generate (m)
    m = int(input("enter the number of sets to generate (m): "))
    # check if n is greater than the size of superset A
    if n > len(A):
        raise ValueError("n should not be greater than the size of superset A.")

    # generate combinations of size n from superset A
    combinations = list(itertools.combinations(A, n))

    # check if there are enough unique combinations to create m sets
    if len(combinations) < m:
        raise ValueError("not enough unique combinations to create m sets.")

    # create m sets from the combinations
    result_list = [set(combination) for combination in combinations[:m]]
    print(result_list)

except ValueError as e:
    print("error:", e)

# 3.1 Problem
try:
    cars_list = {}
    while True:
        # take user input for manufacturer and model, and exit when 'done' is entered
        input_data = input("enter manufacturer and model, and when you're done, input 'done': ")
        if input_data.lower() == 'done':
            break
        # split input into manufacturer and model, then strip any extra spaces
        manufacturer, model = map(str.strip, input_data.split(','))

        if manufacturer in cars_list:
            cars_list[manufacturer].append(model)
        else:
            cars_list[manufacturer] = [model]
    # get a sorted list of manufacturers
    manufacturers = list(cars_list.keys())
    manufacturers.sort()

    # display manufacturer, model count, and models for each manufacturer
    for manufacturer in manufacturers:
        models = cars_list[manufacturer]
        count = len(models)
        print(f"{manufacturer} {count}")
        for model in models:
            print(f"- {model}")
except Exception as e:
    print("error:", e)

# Bonus Problem
try:
    user_elements = []
    while True:
        user_input = input("enter an element: ")
        if user_input.lower() == 'done':
            break
        user_elements.append(user_input)
    input_tuple = tuple(user_elements)
    element_counts = {}
    
    # count the occurrences of each element in the input tuple
    for element in input_tuple:
        if element in element_counts:
            element_counts[element] += 1
        else:
            element_counts[element] = 1

    # create a tuple of elements and their occurrence counts
    result_tuple = tuple((element, count) for element, count in element_counts.items())

    print(f"elements and their occurrences: {result_tuple}")
    # most popular element
    max_count = max(element_counts.values())
    most_popular = [(element, count) for element, count in result_tuple if count == max_count]
    #  least popular element
    min_count = min(element_counts.values())
    least_popular = [(element, count) for element, count in result_tuple if count == min_count]

    # find elements with occurrences at least three times
    frequent_elements = [(element, count) for element, count in result_tuple if list(element_counts.values()).count(count) >= 3]

    # display the most popular, least popular, and frequent elements
    print(f"the most popular element: {most_popular if len(most_popular) == 1 else 'no most popular element'}")
    print(f"the least popular element: {least_popular}")
    print(f"the frequent elements: {frequent_elements}")

except Exception as e:
    # display an error message if an exception occurs
    print("error:", e)
