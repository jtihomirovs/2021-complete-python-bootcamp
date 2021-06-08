# Methods rep
# add to list
mylist = [1, 2, 3, 4]
mylist.append(5)
print(mylist)

# remove from list
mylist.pop()
print(mylist)

# built in help
help(mylist.insert)


# Python functions
# use snake casing  - all is in lowercase with underscore between words
# def name_of_funtction():
# '''
# Docstring explains function
# '''
# print('Hello')

# Basic funtion
def say_hello1():
    print('Hello')


say_hello1()


# We can use .format or just f in the beginnig like there:
def say_hello2(name='Default string'):
    print(f'Hello {name}')


say_hello2('Test')
say_hello2()


def print_result(a, b):
    print(a + b)


def return_result(a, b):
    return a + b


print_result(10, 20)

result = print_result(10, 20)
print(result)

return_result(10, 20)


# mix these two concepts together

def myfunc(a, b):
    print(a + b)
    return a + b


myfunc(1, 2)


def even_check(number):
    result = number % 2 == 0
    print(result)
    return result


def even_check_ol(number):
    return number % 2 == 0


even_check(3)
print(even_check_ol(3))


def check_even_list(num_list):
    for number in num_list:
        if number % 2 == 0:
            print("True")
            return True
        else:
            pass
    print("False")
    return False


check_even_list([3, 2, 5])


def create_even_list(num_list):
    even_numbers = []
    for number in num_list:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            pass
    print(even_numbers)
    return even_numbers


create_even_list([1, 2, 3, 4, 5, 6])
create_even_list([1, 3, 5])

# Lets create list with tuples
stock_prices = [('APPL', 200), ('GOOG', 400), ('MSFT', 100)]

for item in stock_prices:
    print(item)

for ticker, price in stock_prices:
    print(price)

work_hours = [('Abby', 100), ('Billy', 4000), ('Cassie', 800)]


def employee_check(work_hours):
    employee_of_month = ''
    current_max = 0

    for employee, hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass
    # print(employee_of_month, current_max)
    return employee_of_month, current_max


result = employee_check(work_hours)
print(result)

name, hours = employee_check(work_hours)
print(name, hours)

# random example
example = [1, 2, 3, 4, 5, 6, 7]
from random import shuffle

shuffle(example)

print(example)


def shuffle_list(mylist):
    shuffle(mylist)
    return mylist


def player_guess():
    guess = ''
    while guess not in ['0', '1', '2']:
        # input always returns a string
        guess = input('Pick a number: 0, 1 or 2: ')
    return int(guess)


# myindex = player_guess()


def check_guess(mylist, guess):
    if mylist[guess] == 'O':
        print('Correct!')
    else:
        print('Wrong guess!')
        print(mylist)


# INITIAL LIST
mylist = [' ', 'O', ' ']

# SHUFFLE LIST
mixed_list = shuffle_list(mylist)


# USER GUESS
# guess = player_guess()

# CHECK GUESS
# check_guess(mixed_list, guess)


# args
# args = arbitrary choice. Always use *args. * args returns a tuple
def myfunc(*args):
    return sum(args) * 0.05


print(myfunc(40, 60, 100, 1, 34))


# kwargs
# kwargs = keyword arguments. Always use *kwargs. ** kwargs returns a dictionary
def myfunc_kwargs(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit there')


myfunc_kwargs(fruit='apple', veggie='lettuce')


def myfunc(*args, **kwargs):
    print(args)
    print(kwargs)
    print('I would like {} {}'.format(args[0], kwargs['food']))


myfunc(10, 20, 30, fruit='orange', food='eggs', animal='dog')


# test:
def myfunc(s):
    passed_string = []
    counter = 0
    print('len is', len(s))
    print('range len is', range(len(s)))
    for char in range(len(s)):
        if char % 2 == 0:
            passed_string.append(s[char].lower())
        else:
            passed_string.append(s[char].upper())
        char += 1
    print(''.join(passed_string))
    return ''.join(passed_string)


myfunc('Antrhropomorphism')

# map function - apply every element to function
print('Map example')


def square(num):
    return num ** 2


my_nums = [1, 2, 3, 4, 5]

# 1
for item in map(square, my_nums):
    print(item)

# 2
print(list(map(square, my_nums)))


# 3
def splicer(mystring):
    if len(mystring) % 2 == 0:
        return 'EVEN'
    else:
        return mystring[0]


names = ['Andy', 'Eve', 'Sally']

print(list(map(splicer, names)))


# filter - filter values based on functions condition
def check_even(num):
    return num % 2 == 0


mynums = [1, 2, 3, 4, 5, 6]

print(list(filter(check_even, mynums)))

# lambda
#
# 1:
# def square(num):
#     result = num**2
#     return result
#
# 2:
# def square(num):
#     return num**2
#
# 3:
# def square(num): return num**2
#
# 4 (to lambda - anonymous function):
# lambda num: num ** 2

print(list(map(lambda num: num ** 2, mynums)))

print(list(filter(lambda num: num % 2 == 0, mynums)))

print(list(map(lambda name: name[0], names)))

print(list(map(lambda name: name[::-1], names)))
