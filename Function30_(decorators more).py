'''A decorator is a function that takes another function and extends 
the behavior of this function without explicitly modifying it. 
It is a very powerful tool that allows to add new functionality to an existing function.

There are 2 kinds of decorators:
- Function decoratos
- Class decorators
A function is decorated with the @ symbol:
'''

# A decorator function takes another function as argument, wraps its behaviour inside
# an inner function, and returns the wrapped function.
def start_end_decorator(func):

    def wrapper():
        print('Start')
        func()
        print('End')
    return wrapper

def print_name():
    print('Alex')
print_name()
print()
# Now wrap the function by passing it as argument to the decorator function
# and asign it to itself -> Our function has extended behaviour!
print_name = start_end_decorator(print_name)
print_name()
print()
#Instead of wrapping our function and asigning it to itself, we can achieve 
# the same thing simply by decorating our function with an @.

@start_end_decorator
def print_name():
    print('Alex')
print_name()
print()

'''If our function has input arguments and we try to wrap it with our decorator above,
it will raise a TypeError since we have to call our function
inside the wrapper with this arguments, too.
However, we can fix this by using *args and **kwargs in the inner function:'''

def start_end_decorator_2(func):
    def wrapper(*args,**kwargs): #args store the arguments 
        #kwargs store them in dictionary with variable names
        print('Start')
        result=func(*args,**kwargs)
        print('End')
        return result #ei line ta na dile return None
    return wrapper
@start_end_decorator_2
def add_5(x):
    return x + 5
result = add_5(10)
print(result)

#what happens is the function identity is lost 
#it thinks our function is the wrapper function
print(add_5.__name__) 
help(add_5)

'''To fix this, use the functools.wraps decorator, 
which will preserve the information about the original function. 
This is helpful for introspection purposes,
 i.e. the ability of an object to know about its own attributes at runtime:'''

import functools
def start_end_decorator_4(func):

    @functools.wraps(func) #preserves original identity
    def wrapper(*args, **kwargs):
        print('Start')
        result = func(*args, **kwargs)
        print('End')
        return result
    return wrapper

@start_end_decorator_4
def add_5(x):
    return x + 5
result = add_5(10)
print(result)
print(add_5.__name__)
help(add_5)
print()
'''
#deco syntax
import functools
def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Do something before
        result = func(*args, **kwargs)
        # Do something after
        return result
    return wrapper'''

'''A repeat decorator that takes a number as input. Within this function, 
we have the actual decorator function that wraps our function and extends 
its behaviour within another inner function.
 In this case, it repeats the input function the given number of times.
'''
def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def greet(name):
    print(f"Hello {name}")
greet('Bindi')