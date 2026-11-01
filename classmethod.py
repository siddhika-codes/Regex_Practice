# q1
class Company:
    comp_name = "TechCorp"

    @classmethod
    def rename_company(cls,new_name):
        cls.comp_name = new_name

Company.rename_company("Microsoft")
print(Company.comp_name)

# q2
class Employee:
    total_employees = 0

    @classmethod
    def employees(cls,name):
        cls.name = name
        cls.total_employees += 1

    @classmethod
    def get_total(cls):
        return cls.total_employees

Employee.employees("siddhika")
print(Employee.total_employees)

# q3
class Product:

    def __init__(self,title,price):
        self.title = title
        self.price = int(price)

    @classmethod
    def from_string(cls,prod_string):
        Sitems = prod_string.split("-")
        return cls(title = Sitems[0], price = Sitems[1])

p1 = Product.from_string("siddhika-77000")
print(p1.title)
print(p1.price)

# q4
class Book:

    def __init__(self,title,author):
        self.title = title
        self.author = author

    @classmethod
    def from_string(cls,book_string):
        b =  book_string.split("-")
        return cls(title = b[0],author = b[1])

book = Book.from_string("Harry Potter-JK Rowling")
print(book.title)
print(book.author)

# q5
class Movie:

    def __init__(self,name,year):
        self.name = name
        self.year = year

    @classmethod
    def string(cls,movie_string):
        i = movie_string.split(":")
        return cls(name = i[0], year = i[1])

m1 = Movie.string("ham sath sath hain:1983")
print(m1.name)
print(m1.year)







