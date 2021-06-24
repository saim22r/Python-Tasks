import math

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def division(self):
        return self.num1 / self.num2

    def area_of_circle(self):
        return math.pi * self.num1 ** 2

    def area_of_square(self):
        return self.num1 ** 2

    def area_of_triangle(self):
        return (self.num1 * self.num2) / 2

calc = Calculator(2, 3)
print(calc.area_of_square())