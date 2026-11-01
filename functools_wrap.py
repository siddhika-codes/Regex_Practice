import functools

def add_border(func):
    @functools.wraps(func)
    def wrapper():
        print("---------------")
        func()
        print("---------------")
    return wrapper

@add_border
def show_message():
    """Shows a welcome message"""
    print("Welcome")

print(show_message.__name__)
print(show_message.__doc__)

# q2
import functools

def log_call(func):
    @functools.wraps(func)
    def log(*args, **kwargs):
        print("Calling function...")
        func(*args, **kwargs)
        print("Call finished.")
    return log

@log_call
def add(a, b):
    """Adds two numbers"""
    print(a+b)

add(5, 3)
print(add.__name__)
print(add.__doc__)

        
