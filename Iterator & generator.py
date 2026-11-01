# q1

fruits = ["apple", "banana", "mango"]
frulists = iter(fruits)

print(next(frulists))
print(next(frulists))
print(next(frulists))

# q2

numbers = (5, 10, 15, 20)
seenum = iter(numbers)

print(next(seenum))
print(next(seenum))
print(next(seenum))
print(next(seenum))

# q3

word = "cat"
letters = iter(word)

print(next(letters))
print(next(letters))
print(next(letters))

# iter() and next()
# q1
colors = ["red", "green", "blue"]
c = iter(colors)

print(next(c))
print(next(c))
print(next(c))
print(next(c, "no more colors"))

# q2
word = "python"
n = iter(word)

print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))

# q3
nums = [100,200]
itr1 = iter(nums)
itr2 = iter(nums)

print(next(itr1))
print(next(itr1))
print(next(itr2))
print(next(itr2))

# STOPITERATION
# q1
nums = [7, 14, 21]
n = iter(nums)
while True:
    try:
        values = next(n)
        print(values)
    except StopIteration:
        print("DONE!")
        break

#q2
name = "AI"
words = iter(name)

while True:
    try:
        val = next(words)
        print(val)
    except StopIteration:
        print("NO MORE LETTERS!!")
        break

# CUSTOM ITERATOR CLASS
# q1
class Evennumbers:

    def __init__(self,limit):
        self.limit = limit
        self.current = 2

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.limit:
            raise StopIteration
        value = self.current
        self.current += 2
        return value

e = Evennumbers(10)
for num in e:
    print(num)

# q2
class CountdownIterator:

    def __init__(self,start):
        self.start = start
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 1:
            raise StopIteration
        v = self.current
        self.current -= 1
        return v

c = CountdownIterator(5)
for num in c:
    print(num)

# q3
class SquareIterator:

    def __init__(self,limit):
        self.limit = limit
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.limit:
            raise StopIteration
        value = self.current
        answer = self.current * self.current
        self.current += 1
        return answer

s = SquareIterator(5)
for square in s:
    print(square)

# GENERATOR FUNCTIONS AND YIELD
# q1
def even_numbers(limit):
    current = 2
    while current <= limit:
        yield current
        current += 2

num = even_numbers(10)
for n in num:
    print(n)
    
# q2
def countdown(start):
    current = start
    while current >= 1:
        yield current
        current -= 1

c = countdown(5)
for num in c:
    print(num)

# q3
def squares(limit):
    current = 1
    while current <= limit:
        sqanswer = current * current
        yield sqanswer
        current += 1

sq = squares(5)
for square in sq:
    print(square)

# GENERATOR PAUSE AND RESUME
# q1
def mystery():
    print("A")
    yield 10
    print("B")
    yield 20
    print("C")

m = mystery()
next(m)
next(m)

# GENERATOR EXPRESSION VS LIST COMPREHENSION
# q1
a = [x for x in range(5) if x % 2 == 0]
b = (x for x in range(5) if x % 2 == 0)

print(type(a))
print(type(b))
for values in b:
    print(values)

# q2
import sys
list_version = [x * 2 for x in range(100000)]
gen_version = (x * 2 for x in range(100000))

print(sys.getsizeof(list_version))
print(sys.getsizeof(gen_version))

# q3
gen_expression = (x for x in range(20) if x % 3 == 0)
for value in gen_expression:
    print(value)

# q4
list_c = [x**3 for x in range(1, 11)]
print(list_c)
print(type(list_c))

gen_e = (x for x in range(1,31)if x % 5 == 0)
for val in gen_e:
    print(val)
print(type(gen_e))

# YIELD FROM
# q1
def odds():
    yield 1
    yield 3
    yield 5

def evens():
    yield 2
    yield 4
    yield 6

def all_numbers():
    yield from odds()
    yield from evens()

for nums in all_numbers():
    print(nums)



# q2
def fruits():
    yield "apple"
    yield "banana"

def veggies():
    yield "carrot"
    yield "potato"

def grains():
    yield "rice"
    yield "wheat"

def grocery_list():
    yield from fruits()
    yield from veggies()
    yield from grains()

for values in grocery_list():
    print(values)















