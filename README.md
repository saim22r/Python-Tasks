# Python Tasks
## Task 1 Variables
```
 name = "name"
 name = input("what is your first name? ")
 first_name = name.capitalize()
 print("Hello, "+ first_name)
```
## Task 2 Variables data collection
```
 full_name = "full_name"
 full_name = input("What is your full name including middle names? ")
 Full_Name = full_name.title()
 print("Welcome, " + Full_Name.strip())
```
## Task 3 Control Flow
```
 age_rating = input("What age rating is the movie? ")
 age_rating = str(age_rating)

 if age_rating == "universal":
     print("Everyone can watch!")
 elif age_rating == "pg":
     print("General viewing with some scenes unsuitable for young children")
 elif age_rating == "12":
     print("Films classified 12A and video works classified 12 contain material that is not generally suitable for children aged under 12. No one younger than 12 may see a 12A film in a cinema unless accompanied by an adult")
 elif age_rating == "15":
     print("No one younger than 15 may see a 15 film in a cinema")
 elif age_rating == "18":
     print("No one younger than 18 may see an 18 film in cinema")
 else:
     print("Incorrect age rating has been entered!")
```
## Task 4 Calculate year or birth
### Part 1
```
 name = "Saim"
 age = 24
 import datetime
 year = (datetime.date.today().year) - int(age)
 print(f"OMG {name}, you are {age} years old so you were born in {year}")
```
### Part 2
```
name = input("What is your name? ")
while True:
    age = input("What is your age? ")
    if age.isdigit() == True:
        while True:
            birth_month = int(input("What month, 1 to 12, were you born in? Please use digits "))
            if  birth_month > 6:
                print(f"{name} your birthday is still to come this year! Type exit to leave")
                break
            elif birth_month < 6:
                print(f"{name} your birthday has already passed. Type exit to leave")
                break
            elif birth_month == 6:
                    birth_number_day = int(input("What day, from 1 to 31, were you born in? "))
                    if birth_number_day <= 23:
                        print("Your Birthday has passed. Type exit to leave.")
                        break
                    elif birth_number_day > 23:
                        print("Your Birthday is this month! Type exit to leave")
                        break
    elif age == "exit":
        print("Goodbye!")
        break
```
## Task 5 Loops
```
# Part 1
for i in range(10):
    print("Hello")

# Task 2
names = []
for i in range(5):
    name = input ("What is your name?" )
    names.append(name)
print(names)

# Task 3
list_names_lower = []
for name in names:
    list_names_lower.append(name.lower())
print(list_names_lower)

# Task 4
for names in list_names_lower:
    if len(names) % 2 == 0:
        print(f"{names} is even")
    else:
        print(f"{names} is odd")
```
## Task 6 FizzBuzz
```
for i in range(100):
    if i % 3 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
```
## Task 7 Dict Story
```
story1 = {
    "start":"The journey starts here...",
    "Middle":"A big battle occurs...",
    "End":"It was all a dream."
}

print(story1)
print(type(story1))
print(story1.keys())
print(story1.values())

print(story1.get("Start"))
print(story1.get("Middle"))
print(story1.get("End"))

for i in story1.values():
    print(i)

story1.update({"Hero":"Steel man"})
print(story1)
```
## Task 8 OOP Driving and Voting
```
class Individual:
    def __init__(self, age, driver_license):

        if age >= 18 and driver_license == True:
            print("You can vote and drive!")
        elif age >= 18 and driver_license == False:
            print("You can vote!")
        elif age == 17 and driver_license == True:
            print("You can drive and legally you cant drink but your friends will have your back!")
        elif age == 16:
            print("You can't legally drink but your uncles might have your back!")
        else:
            print("Go back to school")

person1 = Individual(19, True)
```
## Task 9 OOP Calculator
```
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
```
