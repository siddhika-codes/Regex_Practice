# decorator with arguments (*args, **kwargs)
# q1
def log_call(func):
    def log(*args, **kwargs):
        print("Calling function...")
        func(*args, **kwargs)
        print("Call finished.")
    return log

@log_call
def add(a, b):
    print(a+b)

add(5, 3)

# q2
def check_type(func):
    def type(*args, **kwargs):
        print("Checking inputs...")
        func(*args, **kwargs)
        print("Check complete.")
    return type

@check_type
def multiply(a, b, c):
    print(a*b*c)

multiply(2, 3, 4)

# q3
def call_log(func):
    def wrapper(*args, **kwargs):
        print("information of student is")
        func(*args, **kwargs)
        print("information is already given.")
    return wrapper

@call_log
def student_info(name,age,city):
    print(f"{name} is {age} years old, living in {city}")

student_info(name="siddhika",age=22,city="jodhpur")
