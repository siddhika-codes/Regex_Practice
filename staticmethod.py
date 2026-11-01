# @staticmethod
# q1
class Calculator:
    @staticmethod
    def add(a, b):
         return a+b

print(Calculator.add(5, 3))

# q2
class Tempconverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

print(Tempconverter.celsius_to_fahrenheit(23))

# q3
class StringUtils:
    @staticmethod
    def isPalindrome(text):
        return text == text[::-1]

print(StringUtils.isPalindrome("madam"))
print(StringUtils.isPalindrome("queue"))
