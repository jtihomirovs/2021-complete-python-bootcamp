# Math operations

print(2 + 2)
print(2 - 1)
print(2 * 3)
print(3 / 2)
print(5 % 2)

# Check mod
print(50 % 5)

# Check if it is even or odd number
print(23 % 2)

# pow(2, 3)
print(2 ** 3)

# Why doesn't 0.1+0.2-0.3 equal 0.0
print(0.1 + 0.2 - 0.3)

# Assign variables
a = 5
print(a)
print(a + a)
a = a + a
print('a is', a)

a = 30.1
print(type(a))

my_income = 20
tax_rate = 0.1
my_taxes = my_income * tax_rate
print('My taxes are:', my_taxes)

# Strings
print('hello \nworld!')
print('hello \tworld!')

# Length
print(len('I am'))

# Indexing
mystring = 'Hello world'
print(mystring[0])

# mystring[-1]

mystring = 'Hello world'
print(mystring[-1])

# "Up to, but not including"

mystring = 'Hello world'
print(mystring[2:])

mystring = 'Hello world'
print(mystring[:2])

mystring = 'Hello world'
print(mystring[2:6])

mystring = 'Hello world'
print(mystring[::])

mystring = 'Hello world'
print(mystring[::2])

mystring = 'Hello world'
print(mystring[2:7:2])

mystring = 'Hello world'
print(mystring[::-1])

# String concat
name = 'Sam'
last_letters = name[1:]
print('P' + last_letters)

x = 'Hello world'
x = x + " it's beautiful outside"
print(x)

# Multiplication with letters
letter = 'z'
letter = letter * 10
print(letter)

# String methods
x = 'Hello world'
testx = x.upper()
print(testx)

testx = x.lower()
print(testx)

testx = x.split()
print(testx)

# Print formatting with strings
print('This is a string {}'.format('INSERTED'))

print('The {} {} {}'.format('fox', 'brown', 'quick'))

print('The {2} {1} {0}'.format('fox', 'brown', 'quick'))

print('The {q} {b} {f}'.format(f='fox', b='brown', q='quick'))

result = 100 / 777
print(result)

# v1
print('The result was {}'.format(result))

# v2 {value:width.precision f}
print('The result was {r:1.3f}'.format(r=result))

name = 'Jose'
age = 3
print(f'Hello, his name is {name} and ir {age} years old')

# Lists
my_list = ['STRING', 100, 23.2]
print(len(my_list))
print(my_list[0])

# Indexing work just like the string
print(my_list[1:])

another_list = ['four', 'five', 'six']

print(my_list, another_list)

# We need to assign theese lists to a variable to sum them together
print(my_list + another_list)

my_list[0] = 'ONE ALL CAPS'
print(my_list)

my_list.append('six')
print(my_list)

my_list.pop()
print(my_list)

my_list.pop(0)
print(my_list)

new_list = ['a', 'e', 'x', 'b', 'c']
num_list = [4, 1, 8, 3]

# This one does not return anything. That's null
new_list.sort()
print(new_list)

num_list.sort()
num_list.reverse()
print(num_list)

# Dictionaries
my_dict = {'key1': 'value1', 'key2': 'value2'}
print(my_dict['key1'])

prices_lookup = {'apple': 2.99, 'oranges': 1.99, 'milk': 5.8}
print(prices_lookup['apple'])

d = {'k1': 123, 'k2': [0, 1, 2], 'k3': {'insideKey': 100}}
print(d['k3'])
print(d['k3']['insideKey'])

d = {'key1': ['a', 'b', 'c']}
letter = d['key1'][2]
print(letter.upper())

# Or do the previous step in one line
print(d['key1'][2].upper())

# Add values to dictionary
d = {'k1': 100, 'k2': 200}
d['k3'] = 300
print(d)
d['k1'] = 'New value'
print(d)

# Some useful methods
d = {'k1': 100, 'k2': 200, 'k3': 300}
print(d.keys())
print(d.values())
print(d.items())

# Tuple - immutable. Example t = (1,2,3)
# Tuple does not allow change state of object
# There are only 2 methods for tuples
# List - mutable. Example l = [1,2,3]
# Dictionary. Example d = {'v1':1, 'v2':2, 'v3':3}
t = ('a', 'a', 'b')
print(t.count('a'))
print(t.index('a'))

# Sets
myset = set()
myset.add(1)
myset.add(2)
print(myset)

mylist = [1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3]
print(set(mylist))
print(set('Mississippi'))

# Booleans
b = True
b = False
b = None
