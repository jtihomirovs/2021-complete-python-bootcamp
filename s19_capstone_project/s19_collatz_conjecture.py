# File name: collatzConjecture.py
# Description:  Start with a number n > 1. Find the number of steps it takes to reach
# 1 using the following process: If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1.
# Author: Juris Tihomirovs
# Date: 28-05-2021


def get_collatz():
    user_input = 0

    while True:
        try:
            user_input = int(input("Please enter number n > 1: "))
        except ValueError:
            print("Not an integer!")
            continue
        else:
            print("Number accepted")
            break

    steps = 0

    # If n is even, divide it by 2
    while user_input != 1:
        if user_input % 2 == 0:
            user_input = user_input / 2
            steps += 1

        # If n is odd, multiply it by 3 and add 1
        else:
            user_input = (user_input * 3) + 1
            steps += 1

    print('Steps taken', steps)


def main():
    get_collatz()


if __name__ == '__main__':
    main()
