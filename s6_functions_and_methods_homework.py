# 1 - Write a function that computes the volume of a sphere given its radius.

def vol(rad):
    return (4 / 3) * 3.14 * rad ** 3


print(vol(2))


# 2 - Write a function that checks whether a number is in a given range (inclusive of high and low)


def ran_check(num, low, high):
    if num in range(low, high):
        return '{} is in range between {} and {}'.format(num, low, high)
        # f'{num} is in range of {low} and {high}'
    else:
        return '{} is not in range between {} and {}'.format(num, low, high)


print(ran_check(5, 2, 7))
print(ran_check(9, 2, 7))


# 3 - Write a Python function that accepts a string and calculates the number of upper case letters and lower case
# letters.
def up_low(s):
    lower_count = 0
    upper_count = 0
    for char in s:
        if char.islower():
            lower_count += 1
        elif char.isupper():
            upper_count += 1
        else:
            pass
    print('Original string:', s)
    print('No. of Upper case characters', upper_count)
    print('No. of Lower case Characters', lower_count)


s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)


# 4 - Write a Python function that takes a list and returns a new list with unique elements of the first list.
def unique_list(lst):
    return list(set(lst))


print(unique_list([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5]))


# 4 - Write a Python function to multiply all the numbers in a list.
def multiply(numbers):
    sum = 1
    for num in numbers:
        sum = sum * num
    return sum


print(multiply([1, 2, 3, -4]))


# def multiply(n):
#     total = 1
#     for i in range(0, len(n)):
#         total *= n[i]
#     print total


# 5 - Write a Python function that checks whether a word or phrase is palindrome or not
def palindrome(s):
    s = s.replace(' ', '')
    return s == s[::-1]


print(palindrome('helleh'))
print(palindrome('not palindrome'))

# 6 - Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have
# any punctuation)
import string


def ispangram(str):
    # create a set of alphabet
    alphabet = set(string.ascii_lowercase)

    # remove any spaces from the input string
    str = str.replace(' ', '')
    # convert into all lowercase
    str = str.lower()
    # grab all unique numbers from the string set()
    str = set(str)
    # alphabet set == string set input
    return str == alphabet


print(ispangram("The quick brown fox jumps over the lazy dog"))
print(ispangram("Tsadf"))
