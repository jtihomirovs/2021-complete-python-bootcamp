import time
import timeit


def func_one(n):
    return [str(num) for num in range(n)]


print(func_one(10))


def func_two(n):
    return list(map(str, range(n)))


print(func_two(10))

# Current time before
start_time = time.time()
# Run code
result = func_one(10000)
# Current time after running code
end_time = time.time()
# Elapsed time
elapsed_time = end_time - start_time
print('Func one elapsed time:', elapsed_time)

# Current time before
start_time = time.time()
# Run code
result = func_two(10000)
# Current time after running code
end_time = time.time()
# Elapsed time
elapsed_time = end_time - start_time
print('Func two elapsed time:', elapsed_time)

stmt = '''
func_one(100)
'''

setup = '''
def func_one(n):
    return [str(num) for num in range(n)]
'''

print('Func one elapsed time timeit:', timeit.timeit(stmt, setup, number=1000000))

stmt2 = '''
func_two(100)
'''

setup2 = '''
def func_two(n):
    return list(map(str, range(n)))
'''

print('Func two elapsed time timeit:', timeit.timeit(stmt2, setup2, number=1000000))
