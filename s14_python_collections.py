from collections import Counter
from collections import defaultdict
from collections import namedtuple

# 1 - Counter
mylist = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3]

print(Counter(mylist))

mylist_char = ['a', 'a', 'a', 10, 10, 10]

print(Counter(mylist_char))

mylist_string = 'aaaaabbbbbshshsppppp'

print(Counter(mylist_string))

sentence = 'How many times does each word show up in this sentence with a word'
split_sentence = sentence.lower().split()
print(Counter(split_sentence))

letters = 'aaabbbbccccccccddddddd'
c = Counter(letters)
print(c.most_common(2))

# 2 - default dictionary
d = defaultdict(lambda: 0)
dx = {'a': 10}
print(dx['a'])

d['correct'] = 100
print(d['correct'])
print(d['wrong key!'])

# 3 - named tuple
mytuple = (10, 20, 30)
print(mytuple[0])

Dog = namedtuple('Dog', ['age', 'breed', 'name'])

sammy = Dog(age=5, breed='Husky', name='Sam')

print(sammy.age)
print(sammy.breed)
print(sammy.name)
