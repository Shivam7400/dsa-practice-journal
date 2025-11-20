"""
In Python, a decorator is a special type of function that is used to change the behavior of another function, method, or class. 
It wraps a function and adds extra functionality to it without changing it directly. 
Decorators are applied before the definition of the function.
"""

# Decorator without arguments(2 levels)
def simple_decorator(func):
    def wrapper(name):
        print("Before the function call")
        say = func(name)
        print("After the function call")
        return say
    return wrapper

@simple_decorator
def say_hello(name):
    print("Function being excuted")
    return f"Hello {name}!"

print(say_hello('Rohit'))

# Decorator with arguments (3 levels)
def repeat_decorator(times):
    def decorator(func):
        def wrapper(name):
            for _ in range(times):
                print("Before the function call")
                result = func(name)
                print("After the function call")
            return result
        return wrapper
    return decorator

@repeat_decorator(times=3)
def say_hello(name):
    print("Function being excuted")
    return f"Hello {name}!"

print(say_hello('Rohit'))