# functions as first class object
# def cube(x):
#     return x*x*x

# my_cube = cube
# print(cube(3))
# print(type(cube))

# list = [cube]
# print(list[0](3))


# def name():
#     def surname():
#         print("surname is rajput")
#     return surname

# v = name()
# v()


# def run_it(f, val):
#     return f(val)

# print(run_it(cube,3))

# closures
# def make_multiplier(n):
#     def multiply(x):
#         return x*n
#     return multiply

# product = make_multiplier(4)
# print(product(5))

# # q2
# def counter():
#     count = 0
#     def increment():
#         nonlocal count
#         count += 1
#         return count
#     return increment

# co = counter()
# print(co())
# print(co())
# print(co())
# print(co())
# print(co())

# # q3
# def greeting_maker(greeting_word):
#     def greet(name):
#         return greeting_word + ", " + name
#     return greet

# word = greeting_maker("Namaskaram")
# print(word("siddhika"))

# writing a simple decorator
# q1
def shout(func):
    def wrapper():
        print("LOUD MODE ON")
        func()
        print("LOUD MODE OFF")
    return wrapper


@shout
def greet():
    print("Hi there")

greet()

# q2
def add_border(func):
    def border():
        print("---------------")
        func()
        print("---------------")
    return border

@add_border
def show_message():
    print("Welcome to Python!")

show_message()

# q3
def count_calls(call):
    def count():
        print("Function is running")
        call()
        print("Function finished")
    return count

@count_calls
def add_numbers():
    print(2+3)

add_numbers()

# q4



