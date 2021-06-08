hungry = False

if hungry:
    print('Hungry - Its true!')
else:
    print('Im not hungry')

loc = 'Auto shop2'
if loc == 'Auto shop':
    print("Cars are cool!")
elif loc == 'Bank':
    print("Money is cool!")
else:
    print("I do not know much")

# Variable "Num" can be whatever I want
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in mylist:
    print(num)

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in mylist:
    if num % 2 == 0:
        print(num)
    else:
        print(f'Odd number: {num}')

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_sum = 0
for num in mylist:
    list_sum = list_sum + num
print(list_sum)

mystring = 'Hello World'
for letter in mystring:
    print(letter)

for letter in 'Hello World':
    print(letter)

for _ in 'Hello World':
    print('cool!')

tup = (1, 2, 3)
for item in tup:
    print(item)

mylist = [(1, 2), (3, 4), (5, 6), (7, 8)]
print(len(mylist))

for item in mylist:
    print(item)

# Tuple unpacking v1
for (a, b) in mylist:
    print(a)
    print(b)

# Tuple unpacking v2
for a, b in mylist:
    print(a)
    print(b)

# By default in dictionary we iterate trough keys
d = {'k1': 1, 'k2': 2, 'k3': 3}
for item in d:
    print(item)

# If we need iterate trough items, we need use items()
d = {'k1': 1, 'k2': 2, 'k3': 3}
for item in d.items():
    print(item)

# If we need iterate trough values, we need use values()
d = {'k1': 1, 'k2': 2, 'k3': 3}
for value in d.values():
    print(value)

# If we need iterate trough items, than use unpacking
d = {'k1': 1, 'k2': 2, 'k3': 3}
for key, value in d.items():
    print(key)

# While loops
x = 0
while x < 5:
    print(f'The current value of x is {x}')
    x = x + 1
    # v2: x += 1
else:
    print('X is not less then 5')

x = [1, 2, 3]
for item in x:
    # pass and dont do anything
    pass
print('end of script')

mystring = 'Sammy'
for letter in mystring:
    if letter == 'a':
        continue  # skip
    print(letter)

mystring = 'Sammy'
for letter in mystring:
    if letter == 'a':
        break  # stop
    print(letter)

x = 0
while x < 5:
    if x == 2:
        break
    print(x)
    x += 1

# 12.03.2021
# Useful operators
print('Useful operators')
for num in range(0, 10, 2):
    print(num)

# cast this to list
casted_list = list(range(0, 11, 2))
print(casted_list)

# Print index count
index_count = 0
for letter in 'abcde':
    print('At index {} the letter is {}'.format(index_count, letter))
    # index_count = index_count +1
    index_count += 1

word = 'abcde'
for item in enumerate(word):
    print(item)

word = 'abcde'
for index, letter in enumerate(word):
    print(index)
    print(letter)
    print('\n')

# zip
mylist1 = [1, 2, 3, 4, 5]
mylist2 = ['a', 'b', 'c']
mylist3 = [100, 200, 300]
zip(mylist1, mylist2)

for item in zip(mylist1, mylist2, mylist3):
    print(item)

print(list(zip(mylist1, mylist2)))

print('x' in ['x', 'y', 'z'])

d = {'mykey': 345}
print(345 in d.values())

mylist = [10, 20, 30, 40, 100]
print(min(mylist))
print(max(mylist))

# shufffle
from random import shuffle

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
shuffle(mylist)

for letter in mylist:
    print(letter)

# random
from random import randint

print(randint(0, 100))

# input
# result = int(input('Hey, input a number here: '))
# print('The input is', result)
# print(type(result))

# 15.03.2021
# List Comprehensions in Python
# beginners way
mystring = 'hello'
mylist = []
for letter in mystring:
    mylist.append(letter)
print(mylist)

# more efficient way
mylist = [letter for letter in 'numnum']
print(mylist)

# and another one example
mylist = [num for num in range(0, 11)]
print(mylist)

# first argument - what code must do
mylist = [num ** 2 for num in range(0, 11)]
print(mylist)

# With if statement
mylist = [x for x in range(0, 11) if x % 2 == 0]
print(mylist)

# more complex math
celcius = [0, 10, 20, 24.5]
fahrenheit = [(9 / 5) * temp + 32 for temp in celcius]
print(fahrenheit)

# nested for
mylist = []
for x in [2, 4, 6]:
    for y in [1, 10, 1000]:
        mylist.append(x * y)
print(mylist)

# nested for one line code
mylist = [x * y for x in [2, 4, 6] for y in [1, 10, 1000]]
print(mylist)
