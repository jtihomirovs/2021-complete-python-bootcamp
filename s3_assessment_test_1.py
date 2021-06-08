# Strings are ordered sequence of characters
# Strings: s = 'Hello world'
# String methods: Upper(), Lower(), Split()
# v1 print('The result was {}'.format(3.14))
# v2 {value:width.precision f} print('The result was {r:1.3f}'.format(r=3.14))

# Lists are ordered sequence of objects (mutable)
# Lists: l = ['STRING', 100, 23.2]
# List methods: Append(), Pop(), Sort(), Reverse()

# Tuples are ordered sequence of objects (immutable)
# Tuples: t = ('a', 'a', 'b')
# Tuple methods: Count() and Index()

# Dictionary is Key-Value pairing that is unordered
# Dictionaries: d = {'v1':1, 'v2':2, 'v3':3}
# Dictionaries methods: Keys(), Values(), Items()
# print(d['v1'])

# 1 - Numbers
print('What is the value of the expression', 4 * (6 + 5))
print('What is the value of the expression', 4 * 6 + 5)
print('What is the value of the expression', 4 + 6 * 5)

print(type(3 + 1.5 + 4))

# Square root
print(4 ** 0.5)
# Square
print(4 ** 2)

# 2 - Strings
s = 'hello'
print(s[1])
# Go from beginning all the way till the end with the step size negative 1
print(s[::-1])
print(s[4])
print(s[-1])

# 3 - Lists
l = ['0', '0', '0']
l2 = [0] * 3

list3 = [1, 2, [3, 4, 'hello']]
print(list3[2][2])

list4 = [5, 3, 4, 6, 1]
list4.sort()
print(list4)
print(sorted(list4))

# 4 - Dictionaries
d = {'simple_key': 'hello'}
print(d['simple_key'])

d = {'k1': {'k2': 'hello'}}
print(d['k1']['k2'])

d = {'k1': [{'nest_key': ['this is deep', ['hello']]}]}
print(d['k1'][0]['nest_key'][1][0])

d = {'k1': [1, 2, {'k2': ['this is tricky', {'tough': [1, 2, ['hello']]}]}]}
print(d['k1'][2]['k2'][1]['tough'][2][0])

# 5 - Tuples
t = ('a', 'a', 'b')

# 6 - Sets
list5 = [1, 2, 2, 33, 4, 4, 11, 22, 3, 3, 2]
print(set(list5))
