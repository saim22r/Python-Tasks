# Task 1
# name = "name"
# name = input("what is your first name? ")
# first_name = name.capitalize()
# print("Hello, "+ first_name)
#
# # Task 2
# full_name = "full_name"
# full_name = input("What is your full name including middle names? ")
# Full_Name = full_name.title()
# print("Welcome, " + Full_Name.strip())

# Task 3
age_rating = 13

if age_rating == "universal":
    print("Everyone can watch!")
elif age_rating == "pg":
    print("General viewing with some scenes unsuitable for young children")
elif age_rating == 12:
    print("Films classified 12A and video works classified 12 contain material that is not generally suitable for children aged under 12. No one younger than 12 may see a 12A film in a cinema unless accompanied by an adult")
elif age_rating == 15:
    print("No one younger than 15 may see a 15 film in a cinema")
elif age_rating == 18:
    print("No one younger than 18 may see an 18 film in cinema")
else:
    print("Incorrect age rating has been entered!")