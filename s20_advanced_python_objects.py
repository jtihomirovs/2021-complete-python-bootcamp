# Advanced numbers

# Hex representation
print(hex(12))

# Binary representation
print(bin(12))

# Equivalent of 2**4
print(pow(2, 4))

# Absolute value
print(abs(-3))

# Round
print(round(3.141, 2))

# Advanced strings
s = 'hello world'

print(s.capitalize())

print(s.upper())

print(s.lower())

# Count o in the string
print(s.count('o'))

# Print index of the first 'o'
print(s.find('o'))

# Center 'hello world' between z's
print(s.center(20, 'z'))

'hello\thi'.expandtabs()

st = 'hello'

# Check if the string is aplhanumeric
print(st.isalnum())

# Check if the string is alpha
print(st.isalpha())

# Check if it is in lowercase
print(s.islower())

# Check if there is whitespace
print(s.isspace())

txt = "Hello, And Welcome To My World!"
print(txt.istitle())

st = 'HELLO'
print(st.isupper())

print(st.endswith('O'))

# Split will do on every instance
print(s.split('e'))

# Partition - on first instance
print(s.partition('e'))

# Advanced sets
s = set()

s.add(1)
s.add(2)
s.add(2)

print(s)

sc = s.copy()
print(sc)
s.add(4)
print(s.difference(sc))

s1 = {1, 2, 3}
s2 = {1, 4, 5}
s1.difference_update(s2)
print(s1)

s1.discard(1)
print(s1)

s1 = {1, 2, 3}
s2 = {1, 2, 5}

# Elements common for both of the sets
s1.intersection(s2)

# Update s1 with common elements of both sets
s1.intersection_update(s2)
print(s1)

s1 = {1, 2}
s2 = {1, 2, 4}
s3 = {5}

print(s1.isdisjoint(s2))
print(s1.isdisjoint(s3))

print(s1.issubset(s2))
print(s2.issuperset(s1))

print(s1.symmetric_difference(s2))

print(s1.union(s2))

# Dictionaries
d = {'k1': 1, 'k2': 2}

print({x: x ** 2 for x in range(10)})
print({k: v ** 2 for k, v in zip(['a', 'b'], range(2))})

for k in d.items():
    print(k)

for k in d.values():
    print(k)

# Advanced list
l = [1, 2, 3]
l.append(4)
print(l)

print(l.count(10))
print(l.count(1))

# append - [1, 2, 3, [4, 5]]
x = [1, 2, 3]
x.append([4, 5])
print(x)

# extend - [1, 2, 3, 4, 5]
x = [1, 2, 3]
x.extend([4, 5])
print(x)

print(x.index(2))

l.insert(2, 'inserted')
print(l)

print(l.reverse())
