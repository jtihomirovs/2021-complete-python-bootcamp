import math
import random

value = 4.35
print(math.floor(value))
print(math.ceil(value))
print(round(4.35))

print(math.pi)
print(math.e)
print(math.inf)
print(math.nan)
print(math.log(100, 10))
print(math.sin(10))
print(math.degrees(math.pi / 2))
print(math.radians(180))

print(random.randint(0, 100))
# random.seed(101)
print(random.randint(0, 100))
print(random.randint(0, 100))
print(random.randint(0, 100))
print(random.randint(0, 100))
print(random.randint(0, 100))

mylist = list(range(0, 20))
print(random.choice(mylist))

# Sample with replacement
print(random.choices(population=mylist, k=10))

# Sample without replacement
print(random.sample(population=mylist, k=10))

random.shuffle(mylist)
print(mylist)

print(random.uniform(a=0, b=100))

print(random.gauss(mu=0, sigma=1))
