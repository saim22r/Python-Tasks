# Task 1
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
