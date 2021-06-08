def hello(name='Jose'):
    print('This hello() function has been executed!')

    def greet():
        return '\t This is the greet() func inside hello!'

    def welcome():
        return '\t This is welcome() inside hello'

    # print(greet())
    # print(welcome())
    # print('This is the end of the hello function')

    print('I am going to return a function')

    if name == 'Jose':
        return greet()
    else:
        return welcome()


my_new_func = hello('Jose')

print(my_new_func)


# Example nr.1 - return function
def cool():
    def super_cool():
        return 'I am very cool!'

    return super_cool


some_func = cool()
print(some_func())


# Example nr.2 - function as an argument
def hello():
    return 'Hi Jose!'


def other(some_def_func):
    print('Other code runs there!')
    print(some_def_func())


other(hello)


def new_decorator(original_func):
    def wrap_func():
        print('Some extra code, before the original function')
        original_func()
        print('Some extra code, after the original function!')

    return wrap_func


def func_needs_decorator():
    print('I want to be decorated!')


decorated_func = new_decorator(func_needs_decorator)

decorated_func()

# Example with @ sintax
# Decorators often are usen in web frameworks like django and flask
# Decorators - decorate your function with some extra code
print('Example with @ sintax')


@new_decorator
def func_needs_decorator():
    print('I want to be decorated!')


func_needs_decorator()
