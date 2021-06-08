# s9_two.py
import s9_one

print('Top level in s9_two.py')

s9_one.func()

if __name__ == '__main__':
    print('s9_two.py is being run directly!')
else:
    print('s9_two.py has been imported')
