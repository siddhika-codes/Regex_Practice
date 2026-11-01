# q1
def multiply_print(n):
    def product(func):
        def wrapper():
            for i in range(n):
                func()
        return wrapper
    return product

@multiply_print(8)
def answer():
    print("your answer")

answer()
# q2

def min_age_check(age_limit):
    def checkage(func):
        def wrapper(user_age):
            if user_age >= age_limit:
                func(user_age)
            else:
                print("NOT ALLOWED!")
        return wrapper
    return checkage

@min_age_check(23)
def age_is(user_age):
    print("AGE")

age_is(18)
age_is(24)

# q3
def add_unit(unit):
    def addition(func):
        def wrapper():
            result = func()
            print(result, unit)
        return wrapper
    return addition

@add_unit("kg")
def weight():
    return 23

weight()



