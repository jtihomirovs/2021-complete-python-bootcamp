def add(n1, n2):
    print(n1 + n2)


add(10, 20)

# number1 = 10
# number2 = input('PLease provide a number: ')

# add(number1, number2)

try:
    result = 10 + 10
    # want to attempt this code
    # may have an error
except:
    print("Hey, it looks like you aren't adding correctly!")
else:
    print("Add went well!")
    print(result)

try:
    f = open('testfile', 'w')
    f.write('Write a test line')
# except TypeError:
#    print('There was a type error!')
# except OSError:
#    print('Hey you have an OS Error')
except:
    print('All other exceptions!')
finally:
    print('I always run')


def ask_for_int():
    while True:
        try:
            result = int(input('Please provide number: '))
        except:
            print('Woops, that is not a number')
            continue  # just to make this more readable
        else:  # there is no exception
            print('Yes, thank you!')
            break
        finally:
            print('End of try/except/finally')


ask_for_int()
