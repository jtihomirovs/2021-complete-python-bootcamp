from random import randint


# Problem 1
def gensquares(n):
    for i in range(n):
        yield i ** 2


for x in gensquares(10):
    print(x)


# Problem 2
def rand_num(low, high, n):
    for i in range(n):
        yield randint(low, high)


for num in rand_num(1, 10, 12):
    print(num)

# Problem 3
s = 'hello'
s = iter(s)
print(next(s))

# Problem 4
# We should use yield when we want to iterate over a sequence, but don’t want to store the entire sequence in memory.

#  Extra Credit!
