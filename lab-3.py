def task_1():
    #function takes an input number and prints a sequence of even numbers 
    # starting from 2 up to the given number, with an initial "1" printed before the sequence.
    count = int(input("Number: "))

    akzhol = 0

    print(1)

    while count > akzhol:
        akzhol += 2
        print(akzhol)


# task_1()


def task_2():
    # it takes a user input number, calculates its factorial using a while loop, and then prints the result.
    user_input = int(input("Number: "))

    def factorial(n):
        if n == 1:
            return 1

        f = 1
        i = 0

        while n > i:
            i += 1
            f = f * i

        return f

    print(factorial(user_input))


# task_2()

def task_3():
    # this function takes a user input number and checks if it's present in a list of numbers ranging from 1 to 999.
    # then prints out a corresponding message.
    user_input = int(input("Number: "))
    numbers = [int(x) for x in range(1, 1000)]

    while True:
        if user_input in numbers:
            print("We foung your number!", user_input)
            break
        else:
            print("Sorry loser!")
            break


# task_3()

def task_4():
    # takes a user input string, counts the occurrences of the letter 'a' in it, and prints the count
    user_input = str(input("String: "))

    strings = []

    for i in user_input:
        strings += i

    counts = 0

    while len(strings):
        if 'a' in strings:
            strings.remove('a')
            counts += 1

    print(counts)


# task_4()

def task_5():
    #function takes a user input number, converts it to a string, extracts each digit, calculates their sum, and then prints the result. 
    user_input = int(input("Number: "))
    user_input = str(user_input)

    numbers = []

    index, result = 0, 0

    while index < len(user_input):
        numbers.append(int(user_input[index]))
        result += numbers[index]
        index += 1

    print(result)


# task_5()


def fibonnaci():
    # this function calculates and prints the Fibonacci sequence up to a user input number
    # it starts with 0 and 1, and then generates subsequent Fibonacci numbers
    f1, f2 = 0, 1
    user_input = int(input("Number: "))
    akzhol = []

    while user_input > f2:
        f1, f2 = f2, f1 + f2
        print(f2)


# fibonnaci()

def task_7():
    # function takes a user input string and reverses it using Python's string slicing. It then prints the reversed string
    user_input = str(input("String: "))

    index = 0

    result = None

    while index < len(user_input):
        result = user_input[::-1]
        index += 1

    print(result)


# task_7()


def task_8():
    user_input = int(input("Numbers: "))
    user_input = str(user_input)

    index = 0
    akzhol = []

    while index < len(user_input):
        akzhol = int(user_input[index])
        if akzhol % 2 != 0:
            akzhol.append(akzhol)
            index += 1
        else:
            index += 1
            continue

    print(sum(akzhol))


# task_8()

def task_9():
    # this function generates a random number and lets the user guess it
    # providing hints if the guess is too large or too small, and congratulating when the guess is correct
    import random

    numbers = [int(x) for x in range(1, 101)]
    random_element = random.choice(numbers)

    while True:
        user_choice = int(input("Number: "))

        if user_choice < random_element:
            hint = random_element - user_choice
            if hint >= 25:
                print("Слишком маленькое число.")
            else:
                print("Не слишком маленькое число.")

        elif user_choice > random_element:
            hint = user_choice - random_element
            if hint >= 25:
                print("Слишком большое число!")
            else:
                print("Не слишком большое число!")

        else:
            print("Поздравляю! Вы угадали число!")
            break


# task_9()


def task_10():
    #This function takes a user input string, reverses it, and checks if the reversed string is a palindrome
    # it then provides corresponding messages and exits the loop.
    user_input = str(input("String: "))

    while True:
        akzhol = user_input[::-1]

        if akzhol == user_input:
            print("Yeah, sonofabitch!")
            break
        else:
            print("akzhol !")
            break


# task_10()


def task_11():
    user_input_x = int(input("X: "))
    user_input_y = int(input("Y: "))

    n = 0

    if user_input_y == 0:
        print("1")
        return None

    while n < user_input_y:
        n += 1
        result = user_input_x ** n
        print(f'Power: {n} - {result}')


# task_11()

def task_12():
    # function calculates and prints prime numbers up to a user input number it starts with 3 and iterates through odd numbers, checking if they are prime.
    def simple_number(n):
        for i in range(2, n + 1):
            if n == i:
                return True
            elif n % i == 0:
                return False
        return True

    result = []
    i = 3

    akzhol = int(input("Nubmer: "))

    while i < akzhol:
        i += 2
        if simple_number(i):
            result.append(i)
            print(i)


# task_12()

def task_13():
    # this function takes a user input number, converts it to a string, reverses the string, and then prints the reversed string. 
    user_input = int(input("String: "))
    user_str = str(user_input)
    index = 0
    result = None

    while index < len(user_str):
        result = user_str[::-1]
        index += 1
    print(result)


# task_13()

def task_14():
    # function takes a user input number, and if it's not prime, 
    # it increments it until it finds the next prime number, which is then printed.
    def simple_number_check(n):
        for i in range(2, n + 1):
            if n == i:
                return True
            elif n % i == 0:
                return False
        return True

    user_input = int(input("Number: "))
    akzhol = user_input

    if not simple_number_check(user_input):
        if akzhol % 2 == 0:
            akzhol += 1
        else:
            akzhol += 2

    while True:
        if simple_number_check(akzhol):
            print(akzhol)
            break
        akzhol += 2


# task_14()


def task_15():
    # this function takes a user input string and a number, 
    # shifts the letters of the string in the alphabet by that number, and prints the result
    user_string = str(input("String: ")).lower()
    user_input = int(input("Number: "))

    alphabet_dict = {}
    chishr = []

    for i, letter in enumerate('abcdefghijklmnopqrstuvwxyz', 1):
        alphabet_dict[letter] = i

    while True:
        for j in user_string:
            index = 0
            index = alphabet_dict[j]
            index += user_input
            if index > 26:
                index -= 26
            for key, value in alphabet_dict.items():
                if index == value:
                    chishr += key
                    break
        break
    for i in range(len(chishr)):
        print(chishr[i], end="")


# task_15()