# Task 4 Calculate year or birth
# Part 1
# name = "Saim"
# age = 24
# import datetime
#  year = (datetime.date.today().year) - int(age)
#  print(f"OMG {name}, you are {age} years old so you were born in {year}")

# Part 2
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
