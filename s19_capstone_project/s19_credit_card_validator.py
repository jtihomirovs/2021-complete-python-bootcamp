# File name: creditCardValidator.py
# Description: Script for credit card validation
# Author: Juris Tihomirovs
# Date: 28-05-2021


def check_luhn(number):
    num_list = []

    # Create digit list - iterate through string and add items to list
    for num in number:
        num_list.append(int(num))

    # From end first num till beginning with step size 2
    odd_digits = num_list[-1::-2]

    # From end second num till beginning with step size 2
    even_digits = num_list[-2::-2]

    #  Starting from the rightmost digit, double the value of every second digit
    even_digits = [x * 2 for x in even_digits]

    # If doubling of a number results in a two digit number i.e greater than 9(e.g., 6 × 2 = 12), then add the digits
    # of the product
    even_digits = [x - 9 if x > 9 else x for x in even_digits]

    # Now take the sum of all digits
    total_sum = sum(even_digits) + sum(odd_digits)

    if total_sum % 10 == 0:
        print('[Validation OK]:', number)
    else:
        print('[Validation not OK]', number)


def main():
    card_number = input('Enter the card number: ')
    check_luhn(card_number)


if __name__ == '__main__':
    main()
