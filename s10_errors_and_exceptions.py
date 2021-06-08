# Problem 1
try:
    for i in ['a', 'b', 'c']:
        print(i ** 2)
except:
    print('Woops, seems thatt there is an error')

# Problem 2
try:
    x = 5
    y = 0
    z = x / y
except:
    print('Division by zero is not possible')
finally:
    print('All Done')


# Problem 3
def ask():
    while True:
        try:
            usr_inpt = int(input('Please enter a number: '))
            result = usr_inpt ** 2
        except:
            print('An error occurred! Please try again!')
            continue
        else:
            print('Thank you, your number squared is:', result)
            break


ask()
