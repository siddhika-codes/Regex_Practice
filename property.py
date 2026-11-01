# q1
class balance:

    def __init__(self,bal):
        self._bal = bal

    @property
    def bal(self):
        return self._bal

    @bal.setter
    def bal(self,new_bal):
        if new_bal < 0:
            print("Balance is Negative!")
        else:
            self._bal = new_bal

acc = balance(4500)
print(acc.bal)
acc.bal = -2000
print(acc.bal)

# q2
class Person:

    def __init__(self,age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self,new_age):
        if new_age < 0:
            print("Age can't be Negative")
        else:
            self._age = new_age

a = Person(45)
print(a.age)
a.age = -27
print(a.age)

# q3
class Weather:

    def __init__(self,temp):
        self._temp = temp

    @property
    def temp(self):
        return self._temp

    @temp.setter
    def temp(self,new_temp):
        if new_temp > 60:
            print("Temperature is too high!")
        else:
            self._temp = new_temp

w = Weather(34)
print(w.temp)
w.temp = 75
print(w.temp)
