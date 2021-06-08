# 1
# Use for, .split(), and if to create a Statement that will print out words that start with 's':
st = 'Print only the words that start with s in this sentence'
splitlist = st.split()
for word in splitlist:
    if word[0] == 's':
        print(word)

# 2
# Use range() to print all the even numbers from 0 to 10.
for num in range(0, 11):
    if num % 2 == 0:
        print(num)

# 3
# Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
mylist = [x for x in range(0, 51) if x % 3 == 0]
print(mylist)

# 4
# Go through the string below and if the length of a word is even print "even!"

st = 'Print every word in this sentence that has an even number of letters'
splitlist = st.split()

for word in splitlist:
    if len(word) % 2 == 0:
        print(word)

# 5 Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the
# number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print
# "FizzBuzz".
numberlist = list(range(0, 101))
for number in numberlist:
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz: ", number)
    elif number % 3 == 0:
        print("Fizz: ", number)
    elif number % 5 == 0:
        print("Buzz: ", number)

# 6
# Use List Comprehension to create a list of the first letters of every word in the string below:
st = 'Create a list of the first letters of every word in this string'
splitlist = st.split()

newlist = []
for word in splitlist:
    newlist.append(word[0])
print(newlist)

# more efficient way
st = 'Create a list of the first letters of every word in this string'
splitlist = st.split()
mylist = [word[0] for word in splitlist]
print(mylist)
